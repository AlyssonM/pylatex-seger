from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from fastapi import FastAPI, Response, HTTPException, Request, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from jinja2 import Environment, FileSystemLoader

import subprocess
from dotenv import load_dotenv
load_dotenv()
import os

API_KEY = os.getenv("API_KEY")
API_KEY_NAME = "X-API-KEY"

app = FastAPI()
origins = [
    "https://8000-idx-pylatex-seger-1742562415094.cluster-kc2r6y3mtba5mswcmol45orivs.cloudworkstations.dev",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

env = Environment(
    loader=FileSystemLoader('templates'), 
    autoescape=False,
    block_start_string='{%',
    block_end_string='%}',
    variable_start_string='{{',
    variable_end_string='}}'
    )

from pydantic import BaseModel
from typing import List, Optional

class LinhaTabela(BaseModel):
    data: str
    demanda_ponta: str
    demanda_fora_ponta: str
    energia_ponta: str
    energia_fora_ponta: str
    ere: str
    valor_total: str

class TarifaTabela(BaseModel):
    grupo: str
    consumo_ponta: str
    consumo_fora_ponta: str
    demanda_ponta: str
    demanda_fora: str
    ere: Optional[str] = ""
    pis: Optional[str] = ""
    cofins: Optional[str] = ""
    icms: Optional[str] = ""

class AjusteTabela(BaseModel):
    mes: str
    realizado: str
    atualizado: str

class LinhaOtimizacao12Meses(BaseModel):
    data: str
    verde: str
    azul: str
    bt: str

class LinhaContratoComparado(BaseModel):
    data: str
    consumo: str
    demanda: str
    ultrapassagem: str
    bip: str
    ere: str
    impostos: str
    total: str

class LinhaResumo(BaseModel):
    titulo: str
    atual: str
    proposto: str

class DadosRelatorio(BaseModel):
    mostrar_bt: Optional[bool] = False
    Unidade: str
    Autores: str
    data: str
    Endereco: str
    distribuidora: str
    instalacao: str
    TipoContrato: str
    NivelTensao: str
    tensao: str
    tensaoUnid: str
    grupoAtual: str
    subGrupoAtual: str
    subGrupoNovo: str
    classe: str
    TarifaAtual: str
    TarifaNova: str
    TarifaAnalise: str
    TarifaAnalisePonta: str
    TarifaAnaliseForaPonta: str
    demandaAtual: str
    demandaNova: str
    numContas: str
    baseDadosInic: str
    baseDadosFinal: str
    dadosAnaliseInic: str
    dadosAnaliseFinal: str
    custoContratoAtual: str
    custoContratoNovo: str
    economiaContrato: str
    economiaPercentual: str
    tabela_consumo: Optional[List[LinhaTabela]] = []
    total_energia: str
    tabela_tarifas: Optional[List[TarifaTabela]] = []
    tabela_ajuste: Optional[List[AjusteTabela]] = []
    ajuste_acrescimo: str
    ajuste_percentual: str
    tabela_12meses_otimizados: Optional[List[LinhaOtimizacao12Meses]] = [] 
    tabela_contrato_comparado: Optional[List[LinhaContratoComparado]] = []
    resumo_proposta: Optional[List[LinhaResumo]] = []

async def validar_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="API Key inválida")


limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

@app.post("/gerar-relatorio")
@limiter.limit("5/minute")  # máximo 5 requisições por minuto por IP
async def gerar_relatorio(request: Request, dados: DadosRelatorio, _: str = Depends(validar_api_key)):
    template = env.get_template('exemplo.tex')
    tex_renderizado = template.render(**dados.dict())

    tex_path = "/tmp/relatorio.tex"
    pdf_path = "/tmp/relatorio.pdf"

    with open(tex_path, "w") as tex_file:
        tex_file.write(tex_renderizado)

    try:
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-no-shell-escape", "-output-directory=/tmp", tex_path], check=True)
        subprocess.run(["pdflatex", "-interaction=nonstopmode", "-no-shell-escape", "-output-directory=/tmp", tex_path], check=True) # executado duas vezes para TOC
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

    if not pdf_bytes.startswith(b'%PDF'):
        raise HTTPException(500, detail="Arquivo gerado não é um PDF válido.")

    return Response(content=pdf_bytes, media_type="application/pdf")
