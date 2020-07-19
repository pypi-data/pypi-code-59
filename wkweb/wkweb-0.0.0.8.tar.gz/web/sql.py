import time,uuid


class EmptyArgument:
    pass
class sql:
    from sqlalchemy import Column, Integer, Text, String, DateTime, Sequence, Date, Boolean, Float
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker, scoped_session
    Model = declarative_base()
    __engines__=[]

    class PrettyPrint:

        def __repr__(self):
            from sqlalchemy import inspect
            mapper = inspect(self.__class__)
            keys = []
            for column in mapper.attrs:
                keys.append(column.key)
            return '''<%s object : %s>''' % (
                self.__class__.__name__, ' , '.join(['%s=%s' % (key, getattr(self, key)) for key in keys]))

    class BaseMixin(PrettyPrint):
        __engine__=None
        @classmethod
        def get_session(cls,*args,**kwargs):
            return cls.get_bound_engine().get_session(*args,**kwargs)
        def to_dict(self):
            d = {}
            for column in self.__table__.columns:
                d[column.name] = str(getattr(self, column.name))
            return d
        @classmethod
        def get_primary_keys(cls):
            return list(cls.__table__.primary_key)
        @classmethod
        def get_first_primary_key(cls):
            pk_name = cls.get_primary_keys()[0].name
            return getattr(cls,pk_name)
        @classmethod
        def get(cls,pk,default=EmptyArgument):
            pk_field=cls.get_first_primary_key()
            obj=cls.query().filter(pk_field==pk).one_or_none()
            if obj is None:
                if default is EmptyArgument:
                    raise KeyError('Cannot find such key %s in table %s'%(pk_field,cls.__tablename__))
                return default
            return obj
        @classmethod
        def add(cls,instance):
            with cls.get_session() as sess:
                sess.add(instance)
        @classmethod
        def all(cls):
            return cls.query().all()


        @classmethod
        def query(cls):
            engine=cls.get_bound_engine()
            with engine.get_session() as sess:
                return sess.query(cls)
        @classmethod
        def get_bound_engine(self):
            engine=self.__engine__
            if engine is not None:
                assert isinstance(engine,sql.Engine)
            return engine

        def print_info(self):
            x=self.get_bound_engine()

            print('Engine:',x)
            pass
    class Engine:
        def __init__(self, engine_uri, echo=True, *args, **kwargs):
            self.engine = sql.create_engine(engine_uri, echo=echo, *args, **kwargs)
            sql.__engines__.append(self)
            RealSession = sql.scoped_session(sql.sessionmaker(bind=self.engine))

            class Session:
                def __init__(self, autocommit=True, autoclose=True, autoexpunge=False, autofill=False):
                    self.autocommit = autocommit
                    self.autoclose = autoclose
                    self.autoexpunge = autoexpunge
                    self.autofill = autofill
                    self.real_sess = RealSession()
                def add_all(self,*args):
                    return self.real_sess.add_all(*args)
                def expunge(self, x):
                    return self.real_sess.expunge(x)

                def expunge_all(self):
                    return self.real_sess.expunge_all()

                def query(self, model):
                    return self.real_sess.query(model)

                def rollback(self):
                    return self.real_sess.rollback()

                def close(self):
                    return self.real_sess.close()

                def add(self, obj):
                    if self.autofill:
                        if hasattr(obj, 'auto_fill'):
                            obj.auto_fill()
                    return self.real_sess.add(obj)

                def commit(self):
                    return self.real_sess.commit()

                def __enter__(self):
                    return self

                def __exit__(self, exc_type, exc_val, exc_tb):
                    try:

                        if self.autocommit:
                            self.commit()
                    except:
                        self.rollback()
                        raise
                    finally:
                        if self.autoexpunge:
                            self.expunge_all()
                        if self.autoclose:
                            self.close()

            self.Session = Session
            self.BaseMixin=sql.BaseMixin
            self.Model = sql.Model

        def get_session(self, autocommit=True, autoclose=True, autoexpunge=False, autofill=False):
            sess = self.Session(autoclose=autoclose, autocommit=autocommit, autoexpunge=autoexpunge, autofill=autofill)
            return sess

        def create_all(self):
            res=self.Model.metadata.create_all(self.engine)
            for cls_name,model in self.Model._decl_class_registry.items():
                if isinstance(model,type) and issubclass(model,self.BaseMixin):
                    model.__engine__=self
            return res


class StateStore(sql.BaseMixin,sql.Model):
    __tablename__ = 'state_store'
    id = sql.Column(sql.String(80), primary_key=True, default=lambda: uuid.uuid4().hex, nullable=False)
    c1 = sql.Column(sql.String(80))
    c2 = sql.Column(sql.String(80))
    c3 = sql.Column(sql.String(80))
    c4 = sql.Column(sql.String(80))
    c5 = sql.Column(sql.String(80))
    expire_time = sql.Column(sql.Float)


class StateManger:
    def __init__(self, engine, Model):
        assert isinstance(engine, sql.Engine)
        assert Model is StateStore
        self.engine = engine
        self.Model = Model

    def produce_key(self, timedelta=30 * 60):
        uid = uuid.uuid4().hex
        self.push('key', uid, timedelta=timedelta)
        return uid

    def delete(self, id):
        with self.engine.get_session() as sess:
            return sess.query(self.Model).filter(self.Model.id == id).delete()

    def check_key(self, key):
        self.get('key', key)

    def push(self, *args, timedelta=5 * 60, ):
        assert len(args) <= 5
        t = time.time()
        keys = ['c1', 'c2', 'c3', 'c4', 'c5']
        keys = keys[:len(args)]
        dic = dict(zip(keys, args))
        state = self.Model(**dic, expire_time=t + timedelta)
        with self.engine.get_session() as sess:
            sess.add(state)

    def flush(self):
        '''这个函数需要被定期地调用，但是目前还没有'''
        t = time.time()
        sess = self.engine.get_session()
        sess.query(self.Model).filter(self.Model.expire_time < t).delete()
        sess.commit()

    def get(self, *args):
        keys = [
            self.Model.c1, self.Model.c2, self.Model.c3, self.Model.c4, self.Model.c5
        ]
        t = time.time()
        keys = keys[:len(args)]
        dic = dict(zip(keys, args))
        dic = [k == v for k, v in dic.items()]
        with self.engine.get_session(autocommit=False) as sess:
            res = sess.query(self.Model).filter(*dic).filter(self.Model.expire_time > t).all()
            return res
