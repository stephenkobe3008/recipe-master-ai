FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ポート5000を公開
EXPOSE 5000

# 起動コマンド
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]