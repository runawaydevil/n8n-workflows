# n8n Workflows Collection

Coleção de workflows de automação n8n traduzida para português brasileiro.

**Site:** https://runawaydevil.github.io/n8n-workflows/

[![n8n Workflows](https://img.shields.io/badge/n8n-Workflows-orange?style=flat-square&logo=n8n)](https://n8n.io)
[![Workflows](https://img.shields.io/badge/Workflows-2061+-blue?style=flat-square)](https://github.com/runawaydevil/n8n-workflows)
[![Integrations](https://img.shields.io/badge/Integrations-311+-green?style=flat-square)](https://github.com/runawaydevil/n8n-workflows)
[![License](https://img.shields.io/badge/License-MIT-purple?style=flat-square)](LICENSE)

## Sobre

Este projeto é um fork traduzido do repositório original [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows).

**Principais características:**
- Tradução completa para português brasileiro (interface, títulos e descrições)
- Mantém todas as funcionalidades do projeto original
- Atualizado com os últimos workflows do repositório original

**Créditos:** Baseado no trabalho de [@Zie619](https://github.com/Zie619). Considere dar uma estrela ao [repositório original](https://github.com/Zie619/n8n-workflows).

## Estatísticas

**Workflows:**
- 2.061 workflows prontos para produção
- 311 integrações únicas
- 30.774 nós no total
- 15 categorias organizadas
- 100% taxa de sucesso de importação

**Performance:**
- < 100ms tempo de resposta de busca
- < 50MB uso de memória
- 700x menor que v1
- 10x tempos de carregamento mais rápidos
- 40x menor uso de RAM

## Instalação

### Pré-requisitos

- Python 3.9+
- pip
- 100MB de espaço livre em disco

### Instalação Local

```bash
# Clonar o repositório
git clone https://github.com/runawaydevil/n8n-workflows.git
cd n8n-workflows

# Instalar dependências
pip install -r requirements.txt

# Iniciar o servidor
python run.py

# Acessar em http://localhost:8000/docs/
```

### Docker

```bash
# Usando Docker Hub
docker run -p 8000:8000 runawaydevil/n8n-workflows:latest

# Ou construir localmente
docker build -t n8n-workflows .
docker run -p 8000:8000 n8n-workflows
```

## API

### Endpoints

| Endpoint | Método | Descrição |
|----------|--------|-----------|
| `/` | GET | Interface web |
| `/docs/` | GET | Interface principal do site |
| `/api/search` | GET | Buscar workflows |
| `/api/stats` | GET | Estatísticas do repositório |
| `/api/workflow/{id}` | GET | Obter JSON do workflow |
| `/api/categories` | GET | Listar todas as categorias |
| `/api/export` | GET | Exportar workflows |

### Funcionalidades de Busca

- Busca de texto completo em nomes, descrições e nós
- Filtro por categoria (Marketing, Vendas, DevOps, etc.)
- Filtro por complexidade (Baixa, Média, Alta)
- Filtro por tipo de trigger (Webhook, Agendado, Manual, etc.)
- Filtro por serviço (311+ integrações)

## Arquitetura

```
Usuário -> Interface Web -> Servidor FastAPI -> SQLite FTS5 -> Banco de Dados
                                              -> Arquivos Estáticos -> JSONs dos Workflows
```

### Stack Tecnológico

- **Backend:** Python, FastAPI, SQLite com FTS5
- **Frontend:** Vanilla JS, CSS
- **Banco de Dados:** SQLite com Busca de Texto Completo
- **Deploy:** Docker, GitHub Actions, GitHub Pages
- **Segurança:** Escaneamento Trivy, proteção CORS, validação de entrada

## Estrutura do Repositório

```
n8n-workflows/
├── workflows/           # 2.061 arquivos JSON de workflows
│   └── [categoria]/     # Organizados por integração
├── docs/               # Site do GitHub Pages
├── src/                # Código-fonte Python
├── scripts/            # Scripts utilitários
├── api_server.py       # Aplicação FastAPI
├── run.py              # Iniciador do servidor
├── workflow_db.py      # Gerenciador de banco de dados
└── requirements.txt    # Dependências Python
```

## Contribuindo

Contribuições são bem-vindas. Formas de contribuir:

- Reportar bugs via [Issues](https://github.com/runawaydevil/n8n-workflows/issues)
- Sugerir funcionalidades em [Discussions](https://github.com/runawaydevil/n8n-workflows/discussions)
- Melhorar documentação
- Enviar correções de workflows

### Configuração de Desenvolvimento

```bash
# Fazer fork e clonar
git clone https://github.com/runawaydevil/n8n-workflows.git

# Criar branch
git checkout -b feature/nova-funcionalidade

# Fazer alterações e testar
python run.py --dev

# Commit e push
git add .
git commit -m "feat: adicionar nova funcionalidade"
git push origin feature/nova-funcionalidade

# Abrir Pull Request
```

## Segurança

### Funcionalidades de Segurança

- Proteção contra path traversal
- Validação e sanitização de entrada
- Proteção CORS
- Limitação de taxa (rate limiting)
- Hardening de segurança Docker
- Usuário de container não-root
- Escaneamento regular de segurança

### Reportar Problemas de Segurança

Reporte vulnerabilidades de segurança aos mantenedores via [Security Advisory](https://github.com/runawaydevil/n8n-workflows/security/advisories/new).

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

```
MIT License

Copyright (c) 2025 RunawayDevil

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Agradecimentos

- **n8n** - Plataforma de automação
- **[@Zie619](https://github.com/Zie619)** - Criador do projeto original [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows)
- **Contribuidores** - Todos que ajudaram a melhorar esta coleção
- **Comunidade** - Por feedback e suporte

---

Fork do projeto original: [Zie619/n8n-workflows](https://github.com/Zie619/n8n-workflows)
