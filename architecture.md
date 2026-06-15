# Arquitetura do Projeto

A arquitetura proposta utiliza Apache Kafka como barramento central de eventos.

## Componentes

- PostgreSQL: banco transacional de origem
- Kafka Connect: responsável por capturar dados
- Apache Kafka: barramento de eventos
- Consumers: aplicações consumidoras
- ksqlDB: processamento e transformação de eventos
- Data Lake: armazenamento analítico

## Diagrama

```mermaid
flowchart LR
    A[PostgreSQL] --> B[Kafka Connect]
    B --> C[Apache Kafka]
    C --> D[Consumer Python]
    C --> E[ksqlDB]
    D --> F[Data Lake]
    E --> F