from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(
    bootstrap_servers="localhost:9094",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

evento = {
    "evento": "CLIENTE_CADASTRADO",
    "cliente_id": 1001,
    "nome": "Cliente Exemplo",
    "status": "ativo"
}

producer.send("clientes-events", evento)
producer.flush()

print("Evento enviado com sucesso.")