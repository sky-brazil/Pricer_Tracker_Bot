# Automação de Enriquecimento de Leads (Python)

English version: [README.md](./README.md)

## Problema de negócio

Times de vendas recebem listas de leads em CSV com baixa padronização e pouca priorização.

## Solução

Este projeto enriquece e ranqueia leads de uma planilha simples:

- normaliza nome de empresas;
- extrai domínio de email;
- calcula score de lead;
- exporta CSV pronto para prospecção.

## Valor comercial no Upwork

- Entrega rápida e objetiva para times de vendas.
- Resultado fácil de demonstrar (antes/depois).
- Base simples para evoluir com integrações e automações recorrentes.

## Stack

- Python 3
- pandas

## Estrutura

```text
01-lead-enrichment-automation/
├── data/
│   └── leads.csv
├── src/
│   └── enrich_leads.py
└── requirements.txt
```

## Execução

```bash
cd portfolio-projects/01-lead-enrichment-automation
pip install -r requirements.txt
python src/enrich_leads.py
```

Saída gerada:

- `data/leads_enriched.csv`

## Pacotes sugeridos

- **Básico:** limpeza e normalização de lista CSV;
- **Intermediário:** enriquecimento + score + exportação;
- **Avançado:** pipeline agendado com notificações.
