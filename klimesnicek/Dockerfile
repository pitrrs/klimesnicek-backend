FROM python:3.11-slim

WORKDIR /app

COPY main.py /app/
COPY requirements.txt /app/
COPY klimesnicek.db /app/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8124"]