import h5py
import numpy as np
import tensorflow as tf
import math


def load_dataset(path_train_dataset, path_test_dataset, X_train_column, Y_train_column, X_test_column, Y_test_column, classes_list):

    train_dataset = h5py.File(str(path_train_dataset), "r")
    X_train_orig = np.array(train_dataset[str(X_train_column)][:])  # your train set features
    Y_train_orig = np.array(train_dataset[str(Y_train_column)][:])  # your train set labels

    test_dataset = h5py.File(str(path_test_dataset), "r")
    X_test_orig = np.array(test_dataset[str(X_test_column)][:])  # your test set features
    Y_test_orig = np.array(test_dataset[str(Y_test_column)][:])  # your test set labels

    classes = np.array(classes_list)  # the list of classes

    Y_train_orig = Y_train_orig.reshape((1, Y_train_orig.shape[0]))
    Y_test_orig = Y_test_orig.reshape((1, Y_test_orig.shape[0]))

    return X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes


def flatten(X_train_orig, Y_train_orig, X_test_orig, Y_test_orig, classes):

    # Flatten the training and test images
    X_train_flatten = X_train_orig.reshape(X_train_orig.shape[0], -1).T
    X_test_flatten = X_test_orig.reshape(X_test_orig.shape[0], -1).T

    # Normalize image vectors
    X_train = X_train_flatten/255.
    X_test = X_test_flatten/255.

    # Convert training and test labels to one hot matrices
    Y_train = np.eye(len(classes))[Y_train_orig.reshape(-1)].T
    Y_test = np.eye(len(classes))[Y_test_orig.reshape(-1)].T

    return X_train, Y_train, X_test, Y_test


def create_placeholders(n_x, n_y):
    """
    Creates the placeholders for the tensorflow session.

    Arguments:
    n_x -- scalar, size of an image vector (num_px * num_px = 64 * 64 * 3 = 12288)
    n_y -- scalar, number of classes (from 0 to 5, so -> 6)

    Returns:
    X -- placeholder for the data input, of shape [n_x, None] and dtype "tf.float32"
    Y -- placeholder for the input labels, of shape [n_y, None] and dtype "tf.float32"

    Tips:
    - You will use None because it let's us be flexible on the number of examples you will for the placeholders.
      In fact, the number of examples during test/train is different.
    """

    X = tf.placeholder(tf.float32, shape=(n_x, None), name="X")
    Y = tf.placeholder(tf.float32, shape=(n_y, None), name="Y")

    return X, Y


def initialize_parameters(layers_list, seed=1):
    """
    Initializes parameters to build a neural network with tensorflow.

    Returns:
    parameters -- a dictionary of tensors containing the weights and biases
    """

    W = []
    b = []
    parameters = {}

    for l in range(1, len(layers_list) + 1):

        W.append(tf.get_variable("W" + str(l), [layers_list[l], layers_list[l-1], initializer=tf.contrib.layers.xavier_initializer(seed)))

        b.append(tf.get_variable("b" + str(l),
                 [layers_list[l], 1], initializer=tf.zeros_initializer()))

        parameters["W" + str(l)]= W[l]
        parameters["b" + str(l)]= b[l]

    return parameters


def forward_propagation(X, parameters):
    """
    Implements the forward propagation for the model: LINEAR -> RELU -> LINEAR -> RELU -> LINEAR -> SOFTMAX

    Arguments:
    X -- input dataset placeholder, of shape (input size, number of examples)
    parameters -- python dictionary containing your parameters "W1", "b1", "W2", "b2", "W3", "b3"
                  the shapes are given in initialize_parameters

    Returns:
    Z_final_layer -- the output of the last LINEAR unit
    """

    Z= []
    A= []

    # Retrieve the parameters from the dictionary "parameters"
    for l in range(1, len(layers) + 1):

        Z.append(tf.add(tf.matmul(parameters["W" + str(l)], X), parameters["b" + str(l)]))
        A.append(tf.nn.relu(Z[l-1]))

    Z_final_layer= Z[-1]

    return Z_final_layer


def compute_cost(Z_final_layer, Y):
    """
    Computes the cost

    Arguments:
    Z_final_layer -- output of forward propagation (output of the last LINEAR unit)
    Y -- "true" labels vector placeholder, same shape as Z_final_layer

    Returns:
    cost - Tensor of the cost function
    """

    # to fit the tensorflow requirement for tf.nn.softmax_cross_entropy_with_logits(...,...)
    logits= tf.transpose(Z_final_layer)
    labels= tf.transpose(Y)

    cost= tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = logits, labels = labels))

    return cost


def random_mini_batches(X, Y, mini_batch_size=32, seed=0):
    """
    Creates a list of random minibatches from (X, Y)

    Arguments:
    X -- input data, of shape (input size, number of examples)
    Y -- true "label" vector
    mini_batch_size - size of the mini-batches, integer
    seed -- this is only for the purpose of grading, so that you're "random minibatches are the same as ours.

    Returns:
    mini_batches -- list of synchronous (mini_batch_X, mini_batch_Y)
    """

    m= X.shape[1]
    mini_batches= []
    np.random.seed(seed)

    # Step 1: Shuffle (X, Y)
    permutation= list(np.random.permutation(m))
    shuffled_X= X[:, permutation]
    shuffled_Y = Y[:, permutation].reshape((Y.shape[0], m))

    # Step 2: Partition (shuffled_X, shuffled_Y). Minus the end case.
    num_complete_minibatches= math.floor(m/mini_batch_size) # number of mini batches of size mini_batch_size in your partitionning
    for k in range(0, num_complete_minibatches):
        mini_batch_X = shuffled_X[:, k * mini_batch_size: k * mini_batch_size + mini_batch_size]
        mini_batch_Y = shuffled_Y[:, k * mini_batch_size: k * mini_batch_size + mini_batch_size]
        mini_batch= (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    # Handling the end case (last mini-batch < mini_batch_size)
    if m % mini_batch_size != 0:
        mini_batch_X = shuffled_X[:, num_complete_minibatches * mini_batch_size: m]
        mini_batch_Y = shuffled_Y[:, num_complete_minibatches * mini_batch_size: m]
        mini_batch= (mini_batch_X, mini_batch_Y)
        mini_batches.append(mini_batch)

    return mini_batches
