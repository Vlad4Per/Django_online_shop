FROM python:3.12.8

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBEFFERED 1

RUN pip install --upgrade pip

WORKDIR /app

RUN mkdir /app/static && mkdir /app/media

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "runserver"]