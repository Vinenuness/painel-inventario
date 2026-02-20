# 🖥 Painel de Inventário e Execução Remota de Scripts

Sistema de inventário de computadores com agente Windows e painel web em Flask.

Permite:
- 📋 Inventariar máquinas automaticamente
- 🏷 Vincular TAG patrimonial
- 🖥 Visualizar hardware, software e rede
- 📝 Criar scripts `.bat`
- 🚀 Executar scripts remotamente
- 📊 Monitorar status de execução (jobs)

---

## 🔧 Tecnologias Utilizadas

- Python 3
- Flask
- SQLite
- JavaScript (Vanilla)
- HTML + CSS
- PyInstaller (agente Windows)
- Nginx (deploy)
- Ubuntu Server (VPS)

---

## 🏗 Arquitetura

Servidor Flask:
- API REST para agentes
- CRUD de scripts
- Sistema de jobs
- Painel web administrativo

Agente Windows:
- Envia inventário periódico
- Recebe jobs do servidor
- Executa scripts localmente
- Retorna stdout/stderr

---

## 📁 Estrutura do Projeto
