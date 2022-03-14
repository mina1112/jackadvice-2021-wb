from ast import For
from fastapi import FastAPI, Depends, HTTPException, Form 
from fastapi.security import HTTPBasic, HTTPBasicCredentials  # new
from starlette.responses import RedirectResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request
from starlette.status import HTTP_401_UNAUTHORIZED  # new
from  ..frontend.src import pages
import db  # new
from models import User, Task 
from auth import auth
from datetime import datetime
import hashlib
app = FastAPI()
security = HTTPBasic()

def index(request: Request):
    return {'Hello': 'World'}

def admin(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    username = auth(credentials)
    # Basic認証で受け取った情報
    user = db.session.query(User).filter(User.username == username).first()
    task = db.session.query(Task).filter(Task.user_id == user.id).all()
    db.session.close()

    return pages.TemplateResponse('TodoShowPage.vue',
                                    {'request': request,
                                    'task': task})

def detail(request: Request, username, taskid, credentials: HTTPBasicCredentials = Depends(security)):
    username_tmp = auth(credentials)
    
    if username_tmp != username:
        return RedirectResponse("/")
    
    user = db.session.query(User).filter(User.username == username).first()
    task = db.session.query(Task).filter(Task.id == taskid).all()
    db.session.close()
    return pages.TemplateResponse('Todoindex.vue',
                                        {'request': request,
                                        'task': task,
                                        })

async def add(request: Request, credentials: HTTPBasicCredentials = Depends(security)):
    # 認証
    username = auth(credentials)

    # ユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()

    # フォームからデータを取得
    data = await request.form()
    year = int(data['year'])
    month = int(data['month'])
    day = int(data['day'])
    hour = int(data['hour'])
    minute = int(data['minute'])

    deadline = datetime(year=year, month=month, day=day,
                        hour=hour, minute=minute)

    # 新しくタスクを生成しコミット
    task = Task(user.id, data['content'], deadline)
    db.session.add(task)
    db.session.commit()
    db.session.close()

    return RedirectResponse('/admin')

def delete(request: Request, t_id, credentials: HTTPBasicCredentials = Depends(security)):
    # 認証
    username = auth(credentials)

    # ログインユーザ情報を取得
    user = db.session.query(User).filter(User.username == username).first()

    # 該当タスクを取得
    task = db.session.query(Task).filter(Task.id == t_id).first()

    # もしユーザIDが異なれば削除せずリダイレクト
    if task.user_id != user.id:
        return RedirectResponse('/admin')

    # 削除してコミット
    db.session.delete(task)
    db.session.commit()
    db.session.close()

    return RedirectResponse('/admin')

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

    return task

async def insert(request: Request, taskname: str = Form(...), 
                content: str = Form(...), deadline: str = Form(...), date: str = Form(...), 
                credentials: HTTPBasicCredentials = Depends(security)):
    """
    タスクを追加してJSONで新規タスクを返す。「deadline」は%Y-%m-%d_%H:%M:%S (e.g. 2019-11-03_12:30:00)の形式
    """
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
