import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Goods(SqlAlchemyBase):
    __tablename__ = 'goods'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    trader_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    category = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    photo_name = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    amount = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    sell_amount = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)

    user = orm.relationship('User')

