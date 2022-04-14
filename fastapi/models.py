from datetime import date, datetime

from matplotlib.pyplot import title

from db import Base

from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.sql.functions import current_timestamp
from sqlalchemy.dialects.mysql import INTEGER, BOOLEAN

import hashlib

SQLITE3_NAME = "./db.sqlite3"


class User(Base):
    """
    Userテーブル

    id       : 主キー
    username : ユーザネーム
    password : パスワード
    mail     : メールアドレス
    """
    __tablename__ = 'user'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )
    username = Column('username', String(256))
    password = Column('password', String(256))
    mail = Column('mail', String(256))

    def __init__(self, username, password, mail):
        self.username = username
        # パスワードはハッシュ化して保存
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.mail = mail

    def __str__(self):
        return str(self.id) + ':' + self.username


class Task(Base):
    """
    toDoタスク

    id               : 主キー
    user_id          : 外部キー
    title            : taskの名前
    goaldatte        :目標日
    deadline         : 締め切り
    notification     : 通知日
    memo             : メモ
    done             : タスクを終了したか
    """
    __tablename__ = 'task'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    user_id = Column('user_id', ForeignKey('user.id'))
    title = Column("title", String(256))
    goalDate = Column(
        'goalData',
        DateTime,
        default=None,
        nullable=False,
    )
    limitDate = Column(
        'limitDate',
        DateTime,
        default=None,
        nullable=False,
    )
    notification = Column(
        'notification',
        DateTime,
        default=None,
        nullable=False,
    )
    date = Column("date", DateTime, default=None)
    memo = Column('memo', String(256))
    done = Column('done', BOOLEAN, default=False, nullable=False)

    def __init__(self, user_id: int, title: str, memo: str, goalDate: datetime, limitDate: datetime, notificaiton: datetime):
        self.user_id = user_id
        self.title = title
        self.goalDate = goalDate
        self.limitDate = limitDate
        self.notification = notificaiton
        self.memo = memo
        self.done = False

