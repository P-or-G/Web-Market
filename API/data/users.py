import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    login = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    email = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    status = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    telegram_id = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    current_id = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    history_id = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)

    goods = orm.relationship("Goods", back_populates='user')

    def __repr__(self):
        return f'{self.id} *** {self.login} *** {self.email} *** {self.hashed_password} *** {self.status} *** ' \
               f'{self.telegram_id} *** f{self.current_id} *** f{self.history_id}'
