# Streaming de Dados com Apache Kafka

Projeto focado na construção de uma arquitetura moderna de Engenharia de Dados baseada em streaming e eventos.

A solução demonstra como sistemas corporativos podem capturar alterações em bancos transacionais, distribuir eventos em tempo real através do Apache Kafka e alimentar aplicações analíticas e Data Lakes de forma escalável.

## Objetivo

Construir uma arquitetura orientada a eventos utilizando:

- Apache Kafka
- Kafka Connect
- PostgreSQL
- Schema Registry
- ksqlDB
- Docker
- Docker Compose
- Data Lake

## Arquitetura

```mermaid
flowchart TD
    A[PostgreSQL] --> B[Kafka Connect]
    B --> C[Apache Kafka]
    C --> D[Consumers Python]
    C --> E[ksqlDB]
    D --> F[Data Lake]
    E --> F