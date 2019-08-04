from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.pool import StaticPool
from models import Base
import os

# Database
engine = None
engine = create_engine('sqlite:///drones.db',
                    convert_unicode=True,
                    connect_args={'check_same_thread': False})
                    
db_session = scoped_session(sessionmaker(autocommit=False,
                                        autoflush=False,
                                        bind=engine))
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models

    Base.metadata.create_all(bind=engine)

def in_memory_db():
    # Database
    engine = None
    engine = create_engine('sqlite://',
                        convert_unicode=True,
                        connect_args={'check_same_thread': False},
                        poolclass=StaticPool)
                        
    session = scoped_session(sessionmaker(autocommit=False,
                                            autoflush=False,
                                            bind=engine))
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import models

    Base.metadata.create_all(bind=engine)

    return session
