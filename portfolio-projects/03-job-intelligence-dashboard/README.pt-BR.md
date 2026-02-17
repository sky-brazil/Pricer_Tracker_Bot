# Dashboard de Inteligência de Vagas (Python + Pandas)

English version: [README.md](./README.md)

## Problema de negócio

Times de recrutamento e inteligência de mercado recebem dados de vagas em formato bruto e sem visão executiva.

## Solução

Este projeto transforma um CSV bruto em entregáveis de negócio:

- relatório Excel com múltiplas abas;
- agregações por empresa e localização;
- resumo executivo em Markdown.

## Valor comercial no Upwork

- Demonstra pipeline ponta a ponta (ingestão -> transformação -> saída).
- Entrega de leitura fácil para gestão.
- Pode ser adaptado para monitoramento de mercado e contratação.

## Stack

- Python 3
- pandas
- openpyxl

## Execução

```bash
cd portfolio-projects/03-job-intelligence-dashboard
pip install -r requirements.txt
python src/build_report.py
```

Saídas:

- `data/job_intelligence_report.xlsx`
- `data/executive_summary.md`

## Pacotes sugeridos

- **Básico:** limpeza e agregação de 1 dataset;
- **Intermediário:** relatório recorrente com múltiplas abas;
- **Avançado:** pipeline completo com dashboard e automação de entrega.
