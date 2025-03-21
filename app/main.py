from fastapi import FastAPI, Response, HTTPException
from jinja2 import Environment, FileSystemLoader
import subprocess
import os

app = FastAPI()
env = Environment(loader=FileSystemLoader('templates'))

@app.get("/gerar-relatorio")
async def gerar_relatorio(nome: str = "Maria", data: str = "21/03/2025", informacao: str = "Informação padrão"):
    
    template = env.get_template('exemplo.tex')
    tex_renderizado = template.render(nome=nome, data=data, informacao=informacao)

    tex_path = "/tmp/relatorio.tex"
    pdf_path = "/tmp/relatorio.pdf"

    with open(tex_path, "w") as tex_file:
        tex_file.write(tex_renderizado)

    try:
        subprocess.run(["pdflatex", "-output-directory=/tmp", tex_path], check=True)
        subprocess.run(["pdflatex", "-output-directory=/tmp", tex_path], check=True) # executado duas vezes para TOC
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail="Erro ao compilar o LaTeX.")

    with open(pdf_path, "rb") as pdf_file:
        pdf_bytes = pdf_file.read()

    # Limpa arquivos temporários
    for ext in ['.tex', '.log', '.aux', '.toc', '.pdf']:
        try:
            os.remove(f"/tmp/relatorio{ext}")
        except FileNotFoundError:
            pass

    return Response(content=pdf_bytes, media_type="application/pdf")
