# Auditoria Profissional: GitHub + Upwork

Data da análise: 17/02/2026

## 1) Diagnóstico objetivo do GitHub (conta `sky-brazil`)

### Dados públicos observados

- Nome exibido: **Diogo**
- Localização: **Spain**
- Bio atual: _"I see programming as a tool for social change, I'm at the beginning of the path."_
- Repositórios públicos: **6**
- Seguidores: **0**
- Repositórios fixados (pinned): **0**
- Campo `blog` no perfil: **vazio**

### Portfólio atual (linha técnica)

Seus projetos estão bem alinhados com uma trilha comercial de automação:

- scraping de vagas;
- bot para Telegram;
- monitoramento de preço;
- dashboard de leads;
- geração de relatórios.

Essa direção é boa para Upwork porque existem muitos jobs de:

- data collection;
- web scraping;
- small business automation;
- reporting pipelines.

### Gaps que reduzem percepção profissional/comercial

1. **Posicionamento fraco no perfil**
   - Bio transmite início de carreira, mas não comunica proposta de valor para cliente.

2. **Sem repositórios fixados**
   - O visitante não enxerga rapidamente seus melhores trabalhos.

3. **Sem licença e sem tópicos (topics) nos repositórios**
   - Reduz confiança e descoberta orgânica.

4. **Sem CI básica e sem padronização de documentação**
   - Falta sinal de maturidade de entrega.

5. **Artefatos de geração automática em READMEs (`[web:xx]`, `[file:xx]`)**
   - Passa impressão de material não revisado para uso comercial.

---

## 2) Diagnóstico Upwork (com base no que foi possível validar)

Não foi encontrado link público do Upwork dentro do perfil GitHub analisado.  
Mesmo sem esse link, dá para evoluir muito com os ajustes abaixo (seção prática) e com os templates deste repositório.

### O que clientes de Upwork tendem a priorizar

- resultado mensurável (tempo/custo economizado);
- escopo claro de MVP;
- comunicação em inglês objetiva;
- provas de execução (repos, vídeos curtos, screenshots);
- velocidade de entrega com risco controlado.

---

## 3) Melhorias prioritárias (72 horas)

### GitHub

1. **Atualizar bio para versão comercial**
   - Exemplo:
   - _"Python Automation Developer | Web Scraping, Dashboards and Telegram Bots for SMBs | Fast MVP delivery."_

2. **Criar repositório de perfil (`sky-brazil/sky-brazil`)**
   - Usar o template em `docs/GITHUB_PROFILE_README_TEMPLATE_EN.md`.

3. **Fixar 3 repositórios**
   - `Pricer_Tracker_Bot`
   - `B2b-Leads-Dashboard`
   - `Jobs_Telegram_Bot`

4. **Padronizar READMEs**
   - Remover artefatos (`[web:..]`, `[file:..]`).
   - Incluir: problema, solução, stack, setup, resultado.

5. **Adicionar LICENSE e topics**
   - Topics sugeridos: `python`, `automation`, `web-scraping`, `telegram-bot`, `dashboard`, `data-pipeline`.

### Upwork

1. **Headline de valor**
   - Evitar genérico ("Python Developer").
   - Focar em dor + resultado + stack.

2. **Overview com números**
   - Ex.: "I build automations that reduce manual reporting by 60-80%."

3. **Project Catalog com escopo fechado**
   - Básico / Standard / Premium.

4. **Portfólio com prova visual**
   - GIF curto ou screenshot de input -> output.

5. **CTA final**
   - Convite claro para call curta de alinhamento.

---

## 4) Plano de 30 dias para ganhar tração

### Semana 1

- Ajustar perfil GitHub e Upwork com os templates.
- Publicar 1 case completo com vídeo de 60-90s.

### Semana 2

- Publicar mais 2 cases (os três projetos em `portfolio-projects/`).
- Criar propostas reutilizáveis por nicho.

### Semana 3

- Aplicar para 5-10 vagas/dia com proposta personalizada.
- Melhorar README a partir das perguntas recebidas dos clientes.

### Semana 4

- Reforçar provas (antes/depois, métricas, depoimentos iniciais).
- Ajustar preços por pacote com base na conversão.

---

## 5) KPIs para acompanhar

- Taxa de resposta em propostas (%)
- Taxa de entrevistas por 10 propostas
- Conversão entrevista -> contrato
- Ticket médio por projeto
- Tempo médio de entrega do MVP

Se quiser, na próxima iteração eu posso transformar cada projeto em um repositório separado com estrutura de produção (testes, CI e Docker).
