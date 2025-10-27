FROM python:3.11-slim
WORKDIR /app

COPY backend/requirements.txt /app/requirements.txt
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

COPY backend/app /app/app
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
