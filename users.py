from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, ForeignKey

engine = create_engine('sqlite:///storage.db', echo = True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column (Integer, primary_key = True)
    name = Column (String)

    def __init__(self, name):
	self.name = name    

    def __repr__(self):
        return 'User (name: %s, fullname: %s)' %(self.name)

#create tables
Base.metadata.create_all(engine)
