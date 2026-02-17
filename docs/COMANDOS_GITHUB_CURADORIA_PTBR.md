# Comandos de curadoria GitHub (executar na sua máquina)

No ambiente automatizado, a integração atual não tem permissão de escrita para metadados de repositório (topics/pinned/bio).  
Use os comandos abaixo no seu terminal local com sua conta autenticada.

## 1) Adicionar topics

```bash
gh repo edit sky-brazil/Pricer_Tracker_Bot --add-topic python --add-topic automation --add-topic web-scraping --add-topic telegram-bot --add-topic freelancer --add-topic upwork
gh repo edit sky-brazil/B2b-Leads-Dashboard --add-topic python --add-topic flask --add-topic dashboard --add-topic leads --add-topic freelancer --add-topic upwork
gh repo edit sky-brazil/Jobs_Telegram_Bot --add-topic python --add-topic telegram-bot --add-topic automation --add-topic job-search --add-topic freelancer --add-topic upwork
gh repo edit sky-brazil/remoteok-job-report --add-topic python --add-topic pandas --add-topic reporting --add-topic automation --add-topic freelancer --add-topic upwork
gh repo edit sky-brazil/remoteok-job-scraper --add-topic python --add-topic selenium --add-topic web-scraping --add-topic jobs --add-topic freelancer --add-topic upwork
```

## 2) Criar repositório de perfil (`sky-brazil/sky-brazil`)

```bash
mkdir sky-brazil && cd sky-brazil
git init
cp /CAMINHO/PARA/docs/GITHUB_PROFILE_README_TEMPLATE_EN.md README.md
git add README.md
git commit -m "docs: add profile README"
gh repo create sky-brazil/sky-brazil --public --source=. --remote=origin --push
```

## 3) Fixar repositórios no perfil (manual na interface)

No GitHub Web:

1. Acesse seu perfil
2. Clique em **Customize your pins**
3. Selecione:
   - `Pricer_Tracker_Bot`
   - `B2b-Leads-Dashboard`
   - `Jobs_Telegram_Bot`
