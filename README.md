# Microserviço de Geração Automática de Relatórios (LaTeX com PyLaTeX e FastAPI)

Este projeto é um microserviço desenvolvido em Python que utiliza FastAPI, PyLaTeX, Jinja2 e Docker Compose para gerar automaticamente relatórios formatados em PDF, usando templates LaTeX com o pacote abnTeX2. A aplicação principal pode consumir esse serviço via chamadas REST, permitindo integração fácil com frameworks como Django.

---

## 🚀 Tecnologias utilizadas

- **Python 3.11**
- **FastAPI** (framework web/API)
- **PyLaTeX** (geração dinâmica de documentos LaTeX)
- **Jinja2** (templates dinâmicos)
- **Docker e Docker Compose** (containerização e ambiente replicável)
- **abnTeX2** (padrão ABNT para documentos técnicos em LaTeX)

---

## 📁 Estrutura do projeto

```bash
relatorio_microservico/
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── templates/
│   └── exemplo.tex
└── docker-compose.yml
```

---

## 🛠️ Configuração e execução

### 1. Clone este repositório

```bash
git clone <url_do_repositório>
cd relatorio_microservico
```

### 2. Execute com Docker Compose

```bash
docker-compose up --build
```

O microserviço estará disponível em: [http://localhost:8000](http://localhost:8000)

---

## 📌 Uso da API

Para gerar um relatório, faça uma requisição GET para o endpoint:

```http
GET /gerar-relatorio?nome=SeuNome&data=dd-mm-aaaa&informacao=Texto
```

Exemplo:
```bash
curl "http://localhost:8000/gerar-relatorio?nome=João&data=21-03-2025&informacao=Teste"
```

---

## 🔍 Sobre o template `exemplo.tex`

O template está configurado para o padrão ABNT (abnTeX2). Você pode customizar este arquivo para ajustar o relatório conforme necessário.

```latex
\documentclass{abntex2}
\usepackage[utf8]{inputenc}
\usepackage[brazil]{babel}

% conteúdo LaTeX com Jinja2 para variáveis dinâmicas
```

---

## ⚙️ Integração com Django

Para integrar com Django, faça chamadas HTTP simples para consumir este microserviço usando bibliotecas como `requests` ou `httpx`.

Exemplo rápido com Django:

```python
import requests

def gerar_relatorio(nome, data, info):
    response = requests.get(
        f"http://localhost:8000/gerar-relatorio?nome={nome}&data={data}&informacao={info}"
    )
    if response.ok:
        with open('relatorio.pdf', 'wb') as pdf:
            pdf.write(response.content)
    else:
        raise Exception("Falha na geração do relatório")
```

---

## ✅ Licença

Este projeto está disponível sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.