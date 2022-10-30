FROM python:3

WORKDIR /app

COPY ./service.py service.py
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

CMD ["python3", "service.py"]