from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from eo_lib.config.config import engine
from eo_lib.model.core.models import ApplicationReference

class BaseService():
    
    def __init__(self, object):

        self.object = object
        self.type = self.object.__tablename__
    
    def __create_session_connection(self):
        session = sessionmaker(bind=engine,autocommit=True)
        self.session = session()
        self.session.begin(subtransactions=True)

    def __close_session_connection(self):
        self.session.close()

    def get_all(self):
        self.__create_session_connection()
        results = self.session.query(self.object).order_by(self.object.id).all()
        self.__close_session_connection()
        return results
    
    def find_by_uuid(self, uuid):
        self.__create_session_connection()
        return self.session.query(self.object).filter(self.object.uuid == uuid).first()
        
    def create(self, object):
        self.__create_session_connection()
        try:
            self.session.begin(subtransactions=True)
            self.session.add(object)
            self.session.commit()
        except:
            self.session.rollback() 
            raise
        #self.__close_session_connection()

    def update (self, object):
        self.__create_session_connection()
        try:
            self.session.query(self.object).filter(self.object.id == object.id).update({column: getattr(object, column) for column in self.object.__table__.columns.keys()})
            self.session.commit()
        except:
            self.session.rollback() 
            raise
        #self.__close_session_connection()

    def delete(self, object):
        self.__create_session_connection()
        try:
            self.session.delete(object)
            self.session.commit()
        except:
            self.session.rollback() 
            raise
        #self.__close_session_connection()

