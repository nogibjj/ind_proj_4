FROM python:3.8

WORKDIR /webapp

COPY ./requirements.txt /webapp/requirements.txt

RUN pip install -r requirements.txt

COPY . /webapp

EXPOSE 8088

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8088"]

