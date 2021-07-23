import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}".format(
    os.environ.get("username", 'root'),
    os.environ.get("password", 'password'),
    os.environ.get("host", 'test.onechannel.one'),
    os.environ.get("port", '3306'),
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


