FROM python:3.11-slim

WORKDIR /app
ADD . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "app.py"]