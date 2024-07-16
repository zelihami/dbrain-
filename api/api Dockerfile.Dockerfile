# Python 3.9 imajını kullanıyoruz
FROM python:3.9-slim

# Çalışma dizinini oluşturuyoruz
WORKDIR /app

# Gerekli bağımlılıkları yüklüyoruz
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Uygulama kodunu kopyalıyoruz
COPY app.py .

# Komutları çalıştırıyoruz
CMD ["python", "app.py"]
