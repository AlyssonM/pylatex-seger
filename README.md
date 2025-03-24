# 📄 Microserviço de Geração de Relatórios em PDF (LaTeX + FastAPI + Jinja2)

Este projeto é um microserviço desenvolvido em **Python** que utiliza **FastAPI**, **LaTeX (abnTeX2)**, **Jinja2** e **Docker Compose** para gerar automaticamente relatórios formatados em PDF a partir de templates dinâmicos.

É ideal para integração com sistemas como **Django**, **plataformas de análise de dados** ou **dashboards interativos**.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.11**
- **FastAPI** – Framework para APIs modernas
- **Jinja2** – Template engine para LaTeX
- **LaTeX (abnTeX2)** – Padrão ABNT para relatórios
- **Docker + Docker Compose**
- **Uvicorn** – ASGI server

---

## 📁 Estrutura do Projeto

```
relatorio_microservico/
├── app/
│   ├── main.py               # Código principal FastAPI
│   └── requirements.txt      # Dependências Python
├── templates/
│   └── exemplo.tex           # Template LaTeX com Jinja2
├── docker-compose.yml
└── README.md
```

---

## 🛠️ Como Executar

1. **Clone o projeto:**

```bash
git clone <url_do_repositório>
cd relatorio_microservico
```

2. **Execute com Docker Compose:**

```bash
docker-compose up --build
```

Acesse em: [http://localhost:8000](http://localhost:8000)

---

## 📌 Como Usar a API

### Endpoint
```
POST /gerar-relatorio
```

### Exemplo de uso com Python (sem frontend):

```python
import requests

dados = {
    # Dados de título/cabeçalho
    "Unidade": "KFC Technologies",
    "Autores": "Caio Verani \\\\ Lívia Montelo \\\\ Estela Nobre",
    "data": "24-03-2025",
    # Dados da aplicação
    "tabela_consumo": [
        {"data": "mai/23", "valor_total": "7.074,85"}
    ]
    #... 
}

res = requests.post("http://localhost:8000/gerar-relatorio", json=dados)

if res.status_code == 200:
    with open("relatorio.pdf", "wb") as f:
        f.write(res.content)
    print("✅ Relatório salvo!")
else:
    print("❌ Erro:", res.status_code)
```

---

## 💡 Templates LaTeX com Jinja2

Exemplo de uso dentro do `.tex`:

```latex
\begin{tabular}{|c|c|}
\hline
Data & Valor \\
\hline
{% for linha in tabela_consumo %}
{{ linha.data }} & {{ linha.valor_total }} \\
{% endfor %}
\hline
\end{tabular}
```

---

## 🌐 Integração com Frontend

O frontend pode fazer requisição e abrir o PDF com:

```javascript
const response = await fetch("http://localhost:8000/gerar-relatorio", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(dados)
      });

      if (!response.ok) {
        alert("Erro ao gerar o PDF");
        return;
      }
const blob = await response.blob();
const url = window.URL.createObjectURL(blob);
window.open(url, "_blank");
```

---

## ✅ Licença

Este projeto está licenciado sob a Licença MIT.
