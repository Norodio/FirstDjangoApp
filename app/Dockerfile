
FROM python:3.8
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/


RUN pip3 install -r requirements.txt

COPY . /code/


EXPOSE 8000
CMD /code/start.sh
