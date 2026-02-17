# Guia de separação dos projetos em repositórios independentes

Objetivo: publicar cada projeto de `portfolio-projects/` como repositório próprio no GitHub.

## Pré-requisitos

- Git instalado
- GitHub CLI autenticado (`gh auth status`)

## Opção 1 (automática)

Execute:

```bash
bash scripts/split_portfolio_projects.sh sky-brazil
```

Esse script:

- copia cada projeto para uma pasta temporária;
- inicializa git local;
- cria o repositório no GitHub (se não existir);
- envia o primeiro commit.

## Opção 2 (manual)

Para cada projeto:

1. Criar repo no GitHub
2. Copiar conteúdo da pasta do projeto
3. Commit inicial
4. Push para `main`

## Nomes sugeridos de repositório

- `lead-enrichment-automation`
- `price-monitoring-api`
- `job-intelligence-dashboard`

## Pós-publicação (curadoria)

1. Adicionar topics
2. Ajustar descrição curta
3. Habilitar GitHub Actions
4. Fixar os 3 repositórios no perfil
5. Linkar no Upwork com prova visual (GIF/screenshot)
