FROM python:3.13-slim

# Install dependensi sistem terbaru untuk LightGBM dan PaddleOCR
RUN apt-get update && apt-get install -y \
    libgomp1 \
    libgl1 \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . /app

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Sesuaikan dengan command startup aplikasi Anda (contoh gunicorn)
CMD ["gunicorn", "app:app"]