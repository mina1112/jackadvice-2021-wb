from datetime import date, datetime

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

    id       : 主キー
    user_id  : 外部キー
    taskname : taskの名前
    content  : 内容
    deadline : 締め切り
    date     : 通知日
    done     : タスクを終了したか
    """
    __tablename__ = 'task'
    id = Column(
        'id',
        INTEGER(unsigned=True),
        primary_key=True,
        autoincrement=True,
    )

    user_id = Column('user_id', ForeignKey('user.id'))
    taskname = Column("taskname", String(256))
    content = Column('content', String(256))
    deadline = Column(
        'deadline',
        DateTime,
        default=None,
        nullable=False,
    )
    date = Column("date", DateTime, default=None)
    done = Column('done', BOOLEAN, default=False, nullable=False)

    def __init__(self, user_id: int, taskname: str, content: str, deadline: datetime, date: datetime = datetime.now()):
        self.user_id = user_id
        self.taskname = taskname
        self.content = content
        self.date = date
        self.deadline = deadline
        self.done = False

