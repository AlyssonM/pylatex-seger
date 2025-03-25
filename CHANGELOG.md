# 📦 CHANGELOG

## [1.0.0] - 25/03/2025

### 🚀 Funcionalidades Implementadas
- 📄 Geração de Relatórios PDF via LaTeX
  - Utilização do **PyLaTeX** com templates Jinja2.
  - Suporte a geração dinâmica de tabelas de análise de consumo, custo de energia, impostos e projeções.
  - Exportação automática de arquivos .PDF via endpoint da API.

- 🔧 Microserviço Isolado com FastAPI
  - Arquitetura desacoplada do sistema principal.
  - Implantação via **Docker Compose** com volume persistente e variáveis de ambiente.
  - Pronto para ser escalado como parte de uma arquitetura baseada em microsserviços.

- 🔐 Segurança e Controle de Recursos
  - Implementação de **Rate Limiting** por IP para proteção da API.
  - Autenticação por chave de API (API Key) com permissões limitadas.
  - Restrições de **uso de CPU e memória** via Docker para evitar sobrecarga do sistema.

- 📊 Lógica de Cálculo de Energia Elétrica
  - Suporte para análise tarifária **Convencional**, **Branca**, **Verde** e **Azul**.
  - Cálculo de otimização de demanda contratada.

### 🛠 Melhorias Realizadas
- Refatoração do código de renderização LaTeX para evitar conflitos com caracteres especiais.
- Otimização do tempo de geração do relatório.
- Logging detalhado com níveis ajustáveis para depuração (DEBUG, INFO, ERROR).
- Adição de testes automatizados para os principais fluxos de geração de relatório.

### 📦 Tecnologias Utilizadas
- Python 3.11
- FastAPI + Uvicorn
- PyLaTeX
- Docker + Docker Compose
- Jinja2 para templates LaTeX
