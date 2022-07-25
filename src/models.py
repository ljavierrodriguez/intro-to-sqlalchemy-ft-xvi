import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    #roles_id = Column(Integer, ForeignKey('roles.id'), nullable=False)
    #role = relationship('Role', uselist=False) # [<Role 1>] # Devolver Objecto directamente: uselist=False <Role 1>
    roles = relationship('Role', secondary="roles_users") # [<Role 1>, <Role 2>]

    def get_user_full_info(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": {
                "id": self.role.id,
                "name": self.role.name
            },
            "role": "http://api.com/api/role/" + self.role.id 
        }

class RoleUser(Base):
    __tablename__ = 'roles_users'
    roles_id = Column(Integer, ForeignKey('roles.id'), primary_key=True) 
    users_id = Column(Integer, ForeignKey('users.id'), primary_key=True)


class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    nane = Column(String(100), unique=True, nullable=False)
    #users = relationship('User', backref='role') # [<User 1>, <User 2>]
    users = relationship('User', secondary="roles_users") # [<User 1>, <User 2>]



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')