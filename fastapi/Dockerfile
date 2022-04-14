FROM python:3.8-buster
EXPOSE 8000
WORKDIR /var/www/html
RUN pip install fastapi sqlalchemy uvicorn matplotlib pydantic
CMD ["python", "run.py"]