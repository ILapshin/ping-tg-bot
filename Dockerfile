FROM python:3.10

RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

CMD ["python", "src/main.py"]