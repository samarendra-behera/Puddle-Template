FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

EXPOSE 5500

CMD [ "python" , "manage.py", "runserver", "0.0.0.0:5500" ]