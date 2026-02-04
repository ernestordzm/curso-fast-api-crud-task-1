

from sqlalchemy import Table
from sqlalchemy.schema import Column, ForeignKey

from sqlalchemy.types import String, Integer, Text, Enum, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from database.database import Base

from schemes import StatusType

task_tag = Table('task_tag', Base.metadata, 
                Column('task_id', Integer, ForeignKey('tasks.id'), primary_key=True),
                Column('tag_id', Integer, ForeignKey('tags.id'), primary_key=True)
                )

#----------------------------------------------------
# Tabla_Prueba = Table('Tabla_Prueba', Base.metadata, 
#                 Column('prueba_id', Integer),
#                 Column('Prueba_Name', Text(20))
#                 )
#----------------------------------------------------

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True, index=True)
    # name = Column(String(20), unique=True)
    name = Column(String(20))
    description = Column(Text())
    status = Column(Enum(StatusType))
#    tipo = Column(Integer),
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    created = Column(DateTime(timezone=True), server_default=func.now() )
    upadated = Column(DateTime(timezone=True), onupdate=func.now() )

    # Modelo - tabla...
    category = relationship('Category', lazy = 'joined', back_populates='tasks')
    user = relationship('User', lazy = 'joined', back_populates='tasks')

    tags = relationship('Tag', secondary=task_tag, back_populates='tasks')
                        # overlaps="tags")


# class Task2(Base):
#     __tablename__ = "tasks2"
#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(20), unique=True)
#     description = Column(Text())
#     status = Column(Enum(StatusType))
#     tipo = Column(Integer)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    tasks = relationship('Task', back_populates='category', lazy='joined')

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    surname = Column(String(20))
    email = Column(String(50))
    website= Column(String(50))
    tasks = relationship('Task', back_populates='user', lazy='joined')

class Tag(Base):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(20))
    tasks = relationship('Task', secondary=task_tag)

