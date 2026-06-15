from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "clientes-events",
    bootstrap_servers="localhost:9094",
    auto_offset_reset="earliest",
    value_deserializer=lambda m: json.loads(m.decode("utf-8"))
)

print("Aguardando eventos...")

for mensagem in consumer:
    evento = mensagem.value
    print("Evento recebido:", evento)