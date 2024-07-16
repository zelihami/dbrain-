import json
from kafka import KafkaConsumer

# Kafka tüketicisini başlat
consumer = KafkaConsumer(
    'kafkatopic',  # Kafka konunuzu buraya yazın
    bootstrap_servers='localhost:9092',  # Kafka broker adresinizi buraya yazın
    auto_offset_reset='earliest',  # En eski mesajlardan başlayarak tüket
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

output_file = 'kafka_data.txt'

# Gelen verileri dosyaya kaydetme
with open(output_file, 'a') as file:
    try:
        for message in consumer:
            data = message.value
            print(f"Alınan veri: {data}")
            file.write(json.dumps(data) + '\n')

    except KeyboardInterrupt:
        print("Kullanıcı tarafından sonlandırıldı")

    finally:
        consumer.close()
