FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app /app/app

# Railway uses dynamic PORT env variable
ENV PORT=8000
CMD uvicorn app.main:app --host 0.0.0.0 --port $PORT
