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


## Evidências de Execução

### Infraestrutura Docker

O ambiente foi executado localmente utilizando Docker Compose contendo:

* Apache Kafka
* PostgreSQL
* Apache Zookeeper

### Processamento de Eventos

O Producer publica eventos em um tópico Kafka.

Exemplo:

```json
{
  "evento": "CLIENTE_CADASTRADO",
  "cliente_id": 1001,
  "nome": "Cliente Exemplo",
  "status": "ativo"
}
```

O Consumer recebe e processa o evento em tempo real.

### Resultado

Validação prática do fluxo:

PostgreSQL → Kafka → Consumer → Processamento

demonstrando uma arquitetura de streaming de dados baseada em eventos.
