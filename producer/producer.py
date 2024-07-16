import json
import time
import requests
from bs4 import BeautifulSoup
from kafka import KafkaProducer

# Kafka üreticisini başlat
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',  # Kafka broker adresinizi buraya yazın
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic_name = 'kafkatopic'  # Kafka konunuzu buraya yazın

# Web sitesinden veri çekme fonksiyonu
def scrape_data():
    url = 'https://scrapeme.live/shop/Bulbasaur/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    product_name = soup.find('h1', class_='product_title entry-title').text
    product_price = soup.find('p', class_='price').text
    product_desc = soup.find('div', class_='woocommerce-product-details__short-description').text.strip()
    product_stock = soup.find('p', class_='stock in-stock').text

    data = {
        'product_name': product_name,
        'product_price': product_price,
        'product_desc': product_desc,
        'product_stock': product_stock
    }
    return data

try:
    while True:
        data = scrape_data()
        producer.send(topic_name, value=data)
        print(f"Gönderilen veri: {data}")
        time.sleep(1)  # Bir sonraki mesajı göndermeden önce 1 saniye bekleyin

except KeyboardInterrupt:
    print("Kullanıcı tarafından sonlandırıldı")

finally:
    producer.close()
