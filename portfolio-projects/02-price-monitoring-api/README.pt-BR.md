# API de Monitoramento de Preços (Python + Flask)

English version: [README.md](./README.md)

## Problema de negócio

Operações de e-commerce e revenda perdem tempo com monitoramento manual de preços.

## Solução

Este projeto expõe uma API simples para verificar preços e identificar alertas.

### Endpoints

- `GET /health` -> status da API
- `POST /check-once` -> executa checagem de preços e retorna alertas

## Valor comercial no Upwork

- Estrutura API-first facilita integração com stack do cliente.
- Escopo claro de MVP com caminho de evolução para produção.
- Ótimo fit para monitoramento de concorrentes.

## Stack

- Python 3
- Flask
- requests
- beautifulsoup4

## Execução

```bash
cd portfolio-projects/02-price-monitoring-api
pip install -r requirements.txt
python src/app.py
```

Teste rápido:

```bash
curl http://127.0.0.1:8000/health
curl -X POST http://127.0.0.1:8000/check-once
```

## Pacotes sugeridos

- **Básico:** 1 fonte monitorada + alerta simples;
- **Intermediário:** múltiplas fontes + API;
- **Avançado:** API + painel + deploy.
