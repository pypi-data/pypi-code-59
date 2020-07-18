from functools import wraps


def tbc_query_params(*args):
    def wrapper(f):
        @wraps(f)
        def wrapped(*a, **kw):
            # print(a)
            # print(kw)
            klass = a[0]
            # print(klass.desc)
            payload = dict(p=5)
            if 'payload' in kw:
                payload = kw.pop('payload')
            # for param in args:
            #     if param not in kw:
            #         raise ValueError(
            #             f'Invalid params, {param} is a required param'
            #         )

                # payload[param] = kw[param]

            return f(payload=payload, *a, **kw)
        return wrapped
    return wrapper


def simple(f):
    @wraps(f)
    def w(*args, **kwargs):
        print('simple')
        return f(*args, **kwargs)
    return w


@tbc_query_params('a','b','c')
@simple
def o(payload=None, *args, **kw):
    print('OOO ')
    print('ar ', args)
    print('Kw ', kw)
    print('Pay ', payload)


# r = o(payload='', a=1, b=2)


def simple1(**kw):
    print('kw ', kw)
    def w(f):
        @wraps(f)
        def we(*args, **kwargs):
            print('simple')
            print('simple a', args)
            print('simple kw', kwargs)
            return f(*args, **kwargs)
        return we
    return w


class A:

    @property
    def desc(self):
        return "okay"

    def td(f, *a, **kw):
        print('F ', f)
        print('a ', a)
        print('kw ', kw)
        @wraps(f)
        def w(*args, **kwargs):
            print('simple')
            return f(*args, **kwargs)

        return w

    @tbc_query_params('a', 'v', 'c')
    @simple1(veridy=False, timeout=(3, 10))
    def c(self, payload=None, *a, **kwargs):
        print('hah c')
        return 1


if __name__ == '__main__':
    a = A()
    print(a.c())


from geopayment.providers.tbc.provider import TBCProvider


class MyBrandTBCProvider(TBCProvider):

    @property
    def description(self) -> str:
        return 'mybrand'

    @property
    def client_ip(self) -> str:
        return '127.0.0.1'

    @property
    def merchant_url(self) -> str:
        return 'http://127.0.0.1:8000/trans/'

    @property
    def cert(self):
        return None


if __name__ == '__main__':
    provider = MyBrandTBCProvider()
    trans_id = provider.get_trans_id(amount=23.45, currency='GEL')
    print('TRANS ID: ', provider.trans_id)
    print(trans_id)
    check_trans_status = provider.check_trans_status(
        trans_id=provider.trans_id
    )
    print(check_trans_status)
    rev = provider.reversal_trans(trans_id=provider.trans_id, amount=12.20)
    print(rev)
    ref = provider.refund_trans(trans_id=provider.trans_id, amount=15.00)
    print(ref)
    dms_a = provider.pre_auth_trans(amount=15.00, currency=981)
    print(dms_a)
    dms_c = provider.confirm_pre_auth_trans(
        trans_id=provider.trans_id, amount=15.00, currency=981
    )
    print(dms_c)
    eof = provider.end_of_business_day()
    print(eof)
    print(MyBrandTBCProvider.quick_end_of_business_day())
