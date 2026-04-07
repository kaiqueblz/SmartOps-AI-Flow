SmartOps AI Flow – Orquestrador de IA estilo N8N

O SmartOps AI Flow é um orquestrador modular de automações inteligentes inspirado no N8N / Make.com, construído com FastAPI, OpenAI, Celery, Redis e arquitetura orientada a agentes.
Permite criar fluxos AI-first de forma simples, escalável e desacoplada.

🚀 Principais Funcionalidades
🔹 Orquestração de agentes especializados (NLP, Dados, Enriquecimento, Ação).
🔹 Execução assíncrona de tarefas com Celery + Redis.
🔹 API REST completa com documentação automática (Swagger).
🔹 Fluxos reutilizáveis, como Onboarding Inteligente.
🔹 Estrutura escalável para criação de novos agentes.
🔹 Pronto para deploy em Docker, Heroku, Render ou servidor próprio.

✔ Organização orientada a Agentes
NLP Agent → interpretação da intenção
Data Agent → coleta/validação de dados
Action Agent → executa ações finais do fluxo

⚙️ Como Rodar
1. Criar ambiente
python -m venv .venv
.venv\Scripts\activate
2. Instalar dependências
pip install -r requirements.txt
3. Rodar API
uvicorn app.main:app --reload
4. Iniciar o Worker
celery -A app.tasks.worker worker --loglevel=info

📝 Logs Avançados

Todos os agentes registram:

tempo de execução
intenção identificada
dados processados
decisões tomadas
falhas e reexecuções

📦 Tecnologias
FastAPI
OpenAI
Celery + Redis
Pydantic
SQLAlchemy
Python 3.10+
📌 Proposta de Uso na Vida Real

Este orquestrador pode ser usado para:

CRM automatizado com IA
Robôs de atendimento inteligente
Pipelines de enriquecimento de dados
Processamento de documentos
Pipelines multiagentes autônomos
