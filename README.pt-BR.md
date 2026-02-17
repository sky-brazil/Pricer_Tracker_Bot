# Price Tracker Bot para E-commerce (USD)

[![CI](https://github.com/sky-brazil/Pricer_Tracker_Bot/actions/workflows/ci.yml/badge.svg)](https://github.com/sky-brazil/Pricer_Tracker_Bot/actions/workflows/ci.yml)
[![Licença: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-yellow.svg)](./LICENSE)

Automação em Python para monitorar preços de produtos e enviar alertas quando atingirem o valor-alvo.

Este repositório foi estruturado para servir como portfólio profissional para freelas de:

- web scraping;
- automações de monitoramento;
- notificações (bots e alertas);
- ferramentas Python de entrega rápida para cliente.

English version: [README.md](./README.md)

## Funcionalidades

- Lê produtos via CSV (`name`, `url`, `target_price`, `currency`, `enabled`).
- Suporta URLs HTTP e arquivos HTML locais para demonstração.
- Extrai preço de elementos `span.price`.
- Compara preço atual com preço-alvo.
- Envia alerta via Telegram quando o alvo é atingido.
- Executa continuamente com intervalo configurável.

## Stack

- Python 3
- requests
- beautifulsoup4
- pyyaml
- python-dotenv

## Estrutura

```text
.
├── main.py
├── scraper.py
├── notifier.py
├── config.yaml
├── urls.example.csv
├── test_product.html
└── requirements.txt
```

## Como rodar

1. Clonar e entrar na pasta:

   ```bash
   git clone https://github.com/sky-brazil/Pricer_Tracker_Bot.git
   cd Pricer_Tracker_Bot
   ```

2. Criar ambiente virtual (opcional):

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instalar dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Criar config local:

   ```bash
   cp config.example.yaml config.yaml
   ```

5. Criar arquivo de variáveis:

   ```bash
   cp .env.example .env
   ```

   Preencher no `.env`:

   - `TELEGRAM_BOT_TOKEN`
   - `TELEGRAM_CHAT_ID`

6. Executar:

   ```bash
   python main.py
   ```

## Formato do CSV

```csv
name,url,target_price,currency,enabled
"Local Test Product","test_product.html",250.00,"USD",true
```

## Configuração

O `config.yaml` controla:

- intervalo de checagem;
- caminho da fonte de dados;
- moeda padrão;
- canais de notificação.

## Evoluções para projetos pagos

Este projeto pode ser expandido com:

- seletores por site;
- retry/backoff;
- proxies;
- mecanismos anti-bloqueio;
- Docker;
- persistência em banco;
- notificações por email/Slack/webhook.

## Expansão de portfólio para Upwork

Este repositório também inclui 3 projetos prontos para publicar como repositórios separados:

- [portfolio-projects/01-lead-enrichment-automation](./portfolio-projects/01-lead-enrichment-automation)
- [portfolio-projects/02-price-monitoring-api](./portfolio-projects/02-price-monitoring-api)
- [portfolio-projects/03-job-intelligence-dashboard](./portfolio-projects/03-job-intelligence-dashboard)

Índice da documentação:

- [docs/README.md](./docs/README.md)

## Licença

Distribuído sob MIT. Veja [LICENSE](./LICENSE).
