from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text)
from scrapy.utils.project import get_project_settings
import os

from sqlalchemy.sql.sqltypes import Numeric


Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))


def create_table(engine):
    Base.metadata.create_all(engine)

class Ingatlanok(Base):
    __tablename__ ="Ingatlanok"
    
    puid=Column(Integer,primary_key=True)
    address=Column('address',Text)
    price=Column('price',Text)
    url=Column('url',Text)
    salesman=Column('salesman',Text)
    #phone_num=Column('phone_num',Text)
    iroda=Column('iroda',Text)

