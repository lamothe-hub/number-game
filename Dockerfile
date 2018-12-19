FROM python:3

ADD client.py /
ADD event.py /

CMD [ "python", "./client.py" ]