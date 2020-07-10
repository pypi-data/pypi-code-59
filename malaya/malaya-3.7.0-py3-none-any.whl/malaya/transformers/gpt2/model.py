import numpy as np
import tensorflow as tf


class HParams:
    def __init__(self, n_vocab, n_ctx, n_embd, n_head, n_layer):
        self.n_vocab = n_vocab
        self.n_ctx = n_ctx
        self.n_embd = n_embd
        self.n_head = n_head
        self.n_layer = n_layer

    def override_from_dict(self, param_dict):
        try:
            self.n_vocab = param_dict['n_vocab']
        except:
            pass
        try:
            self.n_ctx = param_dict['n_ctx']
        except:
            pass
        try:
            self.n_embd = param_dict['n_embd']
        except:
            pass
        try:
            self.n_head = param_dict['n_head']
        except:
            pass
        try:
            self.n_layer = param_dict['n_layer']
        except:
            pass


def default_hparams():
    return HParams(
        n_vocab = 0, n_ctx = 1024, n_embd = 768, n_head = 12, n_layer = 12
    )


def shape_list(x):
    """Deal with dynamic shape in tensorflow cleanly."""
    static = x.shape.as_list()
    dynamic = tf.shape(input = x)
    return [dynamic[i] if s is None else s for i, s in enumerate(static)]


def softmax(x, axis = -1):
    x = x - tf.reduce_max(input_tensor = x, axis = axis, keepdims = True)
    ex = tf.exp(x)
    return ex / tf.reduce_sum(input_tensor = ex, axis = axis, keepdims = True)


def gelu(x):
    return (
        0.5
        * x
        * (1 + tf.tanh(np.sqrt(2 / np.pi) * (x + 0.044715 * tf.pow(x, 3))))
    )


def norm(x, scope, *, axis = -1, epsilon = 1e-5):
    """Normalize to mean = 0, std = 1, then do a diagonal affine transform."""
    with tf.compat.v1.variable_scope(scope):
        n_state = x.shape[-1].value
        g = tf.compat.v1.get_variable(
            'g', [n_state], initializer = tf.compat.v1.constant_initializer(1)
        )
        b = tf.compat.v1.get_variable(
            'b', [n_state], initializer = tf.compat.v1.constant_initializer(0)
        )
        u = tf.reduce_mean(input_tensor = x, axis = axis, keepdims = True)
        s = tf.reduce_mean(
            input_tensor = tf.square(x - u), axis = axis, keepdims = True
        )
        x = (x - u) * tf.math.rsqrt(s + epsilon)
        x = x * g + b
        return x


def split_states(x, n):
    """Reshape the last dimension of x into [n, x.shape[-1]/n]."""
    *start, m = shape_list(x)
    return tf.reshape(x, start + [n, m // n])


def merge_states(x):
    """Smash the last two dimensions of x into a single dimension."""
    *start, a, b = shape_list(x)
    return tf.reshape(x, start + [a * b])


def conv1d(x, scope, nf, *, w_init_stdev = 0.02):
    with tf.compat.v1.variable_scope(scope):
        *start, nx = shape_list(x)
        w = tf.compat.v1.get_variable(
            'w',
            [1, nx, nf],
            initializer = tf.compat.v1.random_normal_initializer(
                stddev = w_init_stdev
            ),
        )
        b = tf.compat.v1.get_variable(
            'b', [nf], initializer = tf.compat.v1.constant_initializer(0)
        )
        c = tf.reshape(
            tf.matmul(tf.reshape(x, [-1, nx]), tf.reshape(w, [-1, nf])) + b,
            start + [nf],
        )
        return c


def attention_mask(nd, ns, *, dtype):
    """1's in the lower triangle, counting from the lower right corner.
    Same as tf.matrix_band_part(tf.ones([nd, ns]), -1, ns-nd), but doesn't produce garbage on TPUs.
    """
    i = tf.range(nd)[:, None]
    j = tf.range(ns)
    m = i >= j - ns + nd
    return tf.cast(m, dtype)


def attn(x, scope, n_state, *, past, hparams):
    assert x.shape.ndims == 3  # Should be [batch, sequence, features]
    assert n_state % hparams.n_head == 0
    if past is not None:
        assert (
            past.shape.ndims == 5
        )  # Should be [batch, 2, heads, sequence, features], where 2 is [k, v]

    def split_heads(x):
        # From [batch, sequence, features] to [batch, heads, sequence, features]
        return tf.transpose(
            a = split_states(x, hparams.n_head), perm = [0, 2, 1, 3]
        )

    def merge_heads(x):
        # Reverse of split_heads
        return merge_states(tf.transpose(a = x, perm = [0, 2, 1, 3]))

    def mask_attn_weights(w):
        # w has shape [batch, heads, dst_sequence, src_sequence], where information flows from src to dst.
        _, _, nd, ns = shape_list(w)
        b = attention_mask(nd, ns, dtype = w.dtype)
        b = tf.reshape(b, [1, 1, nd, ns])
        w = w * b - tf.cast(1e10, w.dtype) * (1 - b)
        return w

    def multihead_attn(q, k, v):
        # q, k, v have shape [batch, heads, sequence, features]
        w = tf.matmul(q, k, transpose_b = True)
        w = w * tf.math.rsqrt(tf.cast(v.shape[-1].value, w.dtype))

        w = mask_attn_weights(w)
        w = softmax(w)
        a = tf.matmul(w, v)
        return a

    with tf.compat.v1.variable_scope(scope):
        c = conv1d(x, 'c_attn', n_state * 3)
        q, k, v = map(split_heads, tf.split(c, 3, axis = 2))
        present = tf.stack([k, v], axis = 1)
        if past is not None:
            pk, pv = tf.unstack(past, axis = 1)
            k = tf.concat([pk, k], axis = -2)
            v = tf.concat([pv, v], axis = -2)
        a = multihead_attn(q, k, v)
        a = merge_heads(a)
        a = conv1d(a, 'c_proj', n_state)
        return a, present


def mlp(x, scope, n_state, *, hparams):
    with tf.compat.v1.variable_scope(scope):
        nx = x.shape[-1].value
        h = gelu(conv1d(x, 'c_fc', n_state))
        h2 = conv1d(h, 'c_proj', nx)
        return h2


def block(x, scope, *, past, hparams):
    with tf.compat.v1.variable_scope(scope):
        nx = x.shape[-1].value
        a, present = attn(
            norm(x, 'ln_1'), 'attn', nx, past = past, hparams = hparams
        )
        x = x + a
        m = mlp(norm(x, 'ln_2'), 'mlp', nx * 4, hparams = hparams)
        x = x + m
        return x, present


def past_shape(*, hparams, batch_size = None, sequence = None):
    return [
        batch_size,
        hparams.n_layer,
        2,
        hparams.n_head,
        sequence,
        hparams.n_embd // hparams.n_head,
    ]


def expand_tile(value, size):
    """Add a new axis of given size."""
    value = tf.convert_to_tensor(value = value, name = 'value')
    ndims = value.shape.ndims
    return tf.tile(tf.expand_dims(value, axis = 0), [size] + [1] * ndims)


def positions_for(tokens, past_length):
    batch_size = tf.shape(input = tokens)[0]
    nsteps = tf.shape(input = tokens)[1]
    return expand_tile(past_length + tf.range(nsteps), batch_size)


def model(hparams, X, past = None, scope = 'model', gpus = [], reuse = False):
    with tf.compat.v1.variable_scope(scope, reuse = reuse):
        results = {}
        batch, sequence = shape_list(X)

        wpe = tf.compat.v1.get_variable(
            'wpe',
            [hparams.n_ctx, hparams.n_embd],
            initializer = tf.compat.v1.random_normal_initializer(stddev = 0.01),
        )
        wte = tf.compat.v1.get_variable(
            'wte',
            [hparams.n_vocab, hparams.n_embd],
            initializer = tf.compat.v1.random_normal_initializer(stddev = 0.02),
        )
        past_length = 0 if past is None else tf.shape(input = past)[-2]
        h = tf.gather(wte, X) + tf.gather(wpe, positions_for(X, past_length))

        # Transformer
        presents = []
        pasts = (
            tf.unstack(past, axis = 1)
            if past is not None
            else [None] * hparams.n_layer
        )
        assert len(pasts) == hparams.n_layer
        gpu_stack = (
            np.floor(hparams.n_layer / len(gpus)) if len(gpus) > 0 else 0
        )
        d = 0
        for layer, past in enumerate(pasts):
            if gpu_stack < 1:
                h, present = block(
                    h, 'h%d' % layer, past = past, hparams = hparams
                )
                tf.compat.v1.add_to_collection('checkpoints', h)
                presents.append(present)
            else:
                if layer != 0 and layer % gpu_stack == 0 and d + 1 != len(gpus):
                    d += 1
                with tf.device(gpus[d]):
                    h, present = block(
                        h, 'h%d' % layer, past = past, hparams = hparams
                    )
                    tf.compat.v1.add_to_collection('checkpoints', h)
                    presents.append(present)
        results['present'] = tf.stack(presents, axis = 1)
        h = norm(h, 'ln_f')

        h_flat = tf.reshape(h, [batch * sequence, hparams.n_embd])
        logits = tf.matmul(h_flat, wte, transpose_b = True)
        logits = tf.reshape(logits, [batch, sequence, hparams.n_vocab])
        results['logits'] = logits
        return results
