from ast import For
from fastapi import FastAPI, Depends, HTTPException, Form 
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED 
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import db 
from models import User, Task 
from auth import auth
from datetime import datetime
import hashlib
from pydantic import BaseModel

app = FastAPI()
security = HTTPBasic()

class Body(BaseModel):
    title: str
    goalDate: str
    limitDate: str
    notification: str
    memo: str

origins = [
    "http://localhost",
    "http://localhost:8080",
    'http://localhost:8000',
    'http://localhost:3000',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



def index(request: Request):
    return {'Hello': 'World'}

def admin(request: Request):

    task = db.session.query(Task).all()
    db.session.close()
    task = [{
        'id': t.id,
        'title': t.title,
        'goalDate': t.goalDate.strftime('%Y-%m-%d %H:%M:%S'),
        'limitDate': t.limitDate.strftime('%Y-%m-%d %H:%M:%S'),
        'notification': t.notification.strftime('%Y-%m-%d %H:%M:%S'),
        'done': t.done,
    } for t in task]
    
    return JSONResponse(content = task)



def detail(request: Request, t_id):

    t = db.session.query(Task).filter(Task.id == t_id).first()
    db.session.close()
    
    task = {
        'id': t.id,
        'title': t.title,
        'goalDate': t.goalDate.strftime('%Y-%m-%d %H:%M:%S'),
        'limitDate': t.limitDate.strftime('%Y-%m-%d %H:%M:%S'),
        'notification': t.notification.strftime('%Y-%m-%d %H:%M:%S'),
        'done': t.done,
    }
    
    return JSONResponse(content = task)

async def add(body: Body):
    title = Body.title
    goalDate = datetime.strptime(Body.goalDate, '%Y-%m-%d %H:%M:%S')
    limitDate = datetime.strptime(Body.limitDate, '%Y-%m-%d %H:%M:%S')
    notification = datetime.strptime(Body.notification, '%Y-%m-%d %H:%M:%S')
    memo = Body.memo
    
    # 新しくタスクを生成しコミット
    task = Task(title, goalDate, limitDate, notification, memo)
    db.session.add(task)
    db.session.commit()
    db.session.close()

    return RedirectResponse('/admin')

def delete(request: Request, t_id):

    task = db.session.query(Task).filter(Task.id == t_id).first()

    db.session.delete(task)
    db.session.commit()
    db.session.close()

    return RedirectResponse('/admin')


"""
def get(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # 認証
    username = auth(credentials)

    # ユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()

    # タスクを取得
    task = db.session.query(Task).filter(Task.user_id == user.id).all()

    db.session.close()

    # JSONフォーマット
    task = [{
        'id': t.id,
        'content': t.content,
        'taskname': t.taskname,
        'deadline': t.deadline.strftime('%Y-%m-%d %H:%M:%S'),
        'date': t.date.strftime('%Y-%m-%d %H:%M:%S'),
        'done': t.done,
    } for t in task]

    return JSONResponse(task)

async def insert(request: Request, taskname: str = Form(...), 
                content: str = Form(...), deadline: str = Form(...), date: str = Form(...), 
                credentials: HTTPBasicCredentials = Depends(security)):
    
    # 認証
    username = auth(credentials)

    # ユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()

    # タスクを追加
    task = Task(user.id, taskname, content, datetime.strptime(deadline, '%Y-%m-%d_%H:%M:%S'), date.strptime(deadline, '%Y-%m-%d_%H:%M:%S'))

    db.session.add(task)
    db.session.commit()

    # テーブルから新しく追加したタスクを取得する
    task = db.session.query(Task).all()[-1]
    db.session.close()

    # 新規タスクをJSONで返す
    return {
        'id': task.id,
        'taskname':task.taskname,
        'content': task.content,
        'deadline': task.deadline.strftime('%Y-%m-%d %H:%M:%S'),
        'date': task.date.strftime('%Y-%m-%d %H:%M:%S'),
        'done': task.done,
    }
"""