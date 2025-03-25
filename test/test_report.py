import requests

# URL do microserviço
url = "https://8000-idx-pylatex-seger-1742562415094.cluster-kc2r6y3mtba5mswcmol45orivs.cloudworkstations.dev/gerar-relatorio"

headers = {
    "Content-Type": "application/json",
    "X-API-KEY": "chave-secreta-supersegura"
}	

# Dados diretamente embutidos (exemplo simplificado com apenas alguns campos)
dados = {
    "Unidade": "KFC Technologies",
    "Autores": "Alysson Machado",
    "data": "24-03-2025",
    "Endereco": "Rodovia Governador Sebastião Bonaparte,  s/nº, Jardim Camburi, Vitória-ES",
    "NivelTensao": "média tensão",
    "tensao": "11",
    "tensaoUnid": "kV",
    "distribuidora": "EDP ES",
    "instalacao": "9999999999",
    "TipoContrato": "cativo (Contrato de Compra de Energia Elétrica Regulada)",
    "grupoAtual": "A",
    "subGrupoAtual": "A4",
    "subGrupoNovo": "A4",
    "classe": "Poder Público",
    "TarifaAtual": "Tarifa Horária Verde",
    "TarifaAnalise": "Tarifa Horária Azul",
    "TarifaAnalisePonta": "30 kW",
    "TarifaAnaliseForaPonta": "43 kW",
    "TarifaNova": "Tarifa Horária Verde",
    "demandaAtual": "30 kW",
    "demandaNova": "43 kW",
    "numContas": "36",
    "baseDadosInic": "junho/2020",
    "baseDadosFinal": "maio/2023",
    "dadosAnaliseInic": "junho/2022",
    "dadosAnaliseFinal": "maio/2023",
    "custoContratoAtual": "95.945,25",
    "custoContratoNovo": "91.958,87",
    "economiaContrato": "3.986,38",
    "economiaPercentual": "4,2",
    "tabela_consumo": [
		  {
			"data": "mai/23",
			"demanda_ponta": "26,17",
			"demanda_fora_ponta": "40,49",
			"energia_ponta": "861,93",
			"energia_fora_ponta": "8.862,09",
			"ere": "0,95",
			"valor_total": "7.074,85"
		  },
		  {
			"data": "abr/23",
			"demanda_ponta": "32,32",
			"demanda_fora_ponta": "52,10",
			"energia_ponta": "1.093,16",
			"energia_fora_ponta": "11.336,58",
			"ere": "0,80",
			"valor_total": "9.657,80"
		  },
		  {
			"data": "mar/23",
			"demanda_ponta": "32,08",
			"demanda_fora_ponta": "54,86",
			"energia_ponta": "1.626,68",
			"energia_fora_ponta": "15.570,34",
			"ere": "0,06",
			"valor_total": "12.653,70"
		  },
		  {
			"data": "fev/23",
			"demanda_ponta": "32,91",
			"demanda_fora_ponta": "60,86",
			"energia_ponta": "1.187,33",
			"energia_fora_ponta": "13.253,72",
			"ere": "0,00",
			"valor_total": "11.509,52"
		  },
		  {
			"data": "jan/23",
			"demanda_ponta": "25,93",
			"demanda_fora_ponta": "44,28",
			"energia_ponta": "1.133,37",
			"energia_fora_ponta": "11.960,48",
			"ere": "0,00",
			"valor_total": "10.249,06"
		  },
		  {
			"data": "dez/22",
			"demanda_ponta": "27,36",
			"demanda_fora_ponta": "44,92",
			"energia_ponta": "1.006,83",
			"energia_fora_ponta": "10.513,06",
			"ere": "0,00",
			"valor_total": "8.347,57"
		  },
		  {
			"data": "nov/22",
			"demanda_ponta": "26,76",
			"demanda_fora_ponta": "37,34",
			"energia_ponta": "955,65",
			"energia_fora_ponta": "10.722,27",
			"ere": "2,45",
			"valor_total": "7.637,68"
		  },
		  {
			"data": "out/22",
			"demanda_ponta": "24,31",
			"demanda_fora_ponta": "32,14",
			"energia_ponta": "897,78",
			"energia_fora_ponta": "10.616,97",
			"ere": "0,80",
			"valor_total": "7.061,13"
		  },
		  {
			"data": "set/22",
			"demanda_ponta": "21,89",
			"demanda_fora_ponta": "31,73",
			"energia_ponta": "804,36",
			"energia_fora_ponta": "7.492,03",
			"ere": "1,59",
			"valor_total": "5.816,13"
		  },
		  {
			"data": "ago/22",
			"demanda_ponta": "21,01",
			"demanda_fora_ponta": "27,45",
			"energia_ponta": "856,19",
			"energia_fora_ponta": "7.225,33",
			"ere": "0,00",
			"valor_total": "5.600,62"
		  },
		  {
			"data": "jul/22",
			"demanda_ponta": "19,58",
			"demanda_fora_ponta": "28,44",
			"energia_ponta": "830,94",
			"energia_fora_ponta": "7.851,42",
			"ere": "0,36",
			"valor_total": "5.346,39"
		  },
		  {
			"data": "jun/22",
			"demanda_ponta": "18,15",
			"demanda_fora_ponta": "22,78",
			"energia_ponta": "778,11",
			"energia_fora_ponta": "6.946,11",
			"ere": "1,32",
			"valor_total": "4.920,74"
		  }
		],
		"total_energia": "95.446,12",
		"tabela_tarifas": [
		  {
			"grupo": "A VERDE A4",
			"consumo_ponta": "1,6628",
			"consumo_fora_ponta": "0,39813",
			"demanda_ponta": "30,44",
			"demanda_fora": "30,44",
			"ere": "0,27703",
			"pis": "1,03916",
			"cofins": "4,78583",
			"icms": "0,00"
		  },
		  {
			"grupo": "A AZUL A4",
			"consumo_ponta": "0,55693",
			"consumo_fora_ponta": "0,39813",
			"demanda_ponta": "45,59",
			"demanda_fora": "30,44",
			"ere": "0,27703",
			"pis": "1,03916",
			"cofins": "4,78583",
			"icms": "0,00"
		  },
		  {
			"grupo": "BT Optante B3",
			"consumo_ponta": "0,67384",
			"consumo_fora_ponta": "0,67384",
			"demanda_ponta": "-",
			"demanda_fora": "-",
			"ere": "0,27703",
			"pis": "1,03916",
			"cofins": "4,78583",
			"icms": "0,00"
		  }
		],
		"tabela_ajuste": [
		  { "mes": "mai/23", "realizado": "7.074,85", "atualizado": "7.127,68" },
		  { "mes": "abr/23", "realizado": "9.657,80", "atualizado": "9.662,42" },
		  { "mes": "mar/23", "realizado": "12.653,70", "atualizado": "12.608,27" },
		  { "mes": "fev/23", "realizado": "11.509,28", "atualizado": "11.455,95" },
		  { "mes": "jan/23", "realizado": "10.249,06", "atualizado": "10.211,43" },
		  { "mes": "dez/22", "realizado": "8.347,57", "atualizado": "8.487,40" },
		  { "mes": "nov/22", "realizado": "7.637,68", "atualizado": "7.763,23" },
		  { "mes": "out/22", "realizado": "7.771,91", "atualizado": "7.871,35" },
		  { "mes": "set/22", "realizado": "5.816,13", "atualizado": "5.624,76" },
		  { "mes": "ago/22", "realizado": "5.500,62", "atualizado": "5.438,74" },
		  { "mes": "jul/22", "realizado": "5.346,39", "atualizado": "5.377,45" },
		  { "mes": "jun/22", "realizado": "4.920,74", "atualizado": "5.187,26" },
		  { "mes": "TOTAL", "realizado": "95.446,12", "atualizado": "95.945,25" }
		],
		"ajuste_acrescimo": "499,14",
		"ajuste_percentual" : "0,52",
		"tabela_12meses_otimizados": [
		  { "data": "mai/23", "verde": "6.541,04", "azul": "6.892,21", "bt": "6.835,40" },
		  { "data": "abr/23", "verde": "8.836,83", "azul": "9.230,27", "bt": "9.066,56" },
		  { "data": "mar/23", "verde": "11.782,68", "azul": "11.485,91", "bt": "12.087,99" },
		  { "data": "fev/23", "verde": "10.630,37", "azul": "10.982,49", "bt": "10.150,78" },
		  { "data": "jan/23", "verde": "8.347,34", "azul": "8.357,95", "bt": "9.218,00" },
		  { "data": "dez/22", "verde": "7.539,91", "azul": "7.708,89", "bt": "8.099,55" },
		  { "data": "nov/22", "verde": "7.476,55", "azul": "7.703,18", "bt": "8.209,95" },
		  { "data": "out/22", "verde": "7.471,05", "azul": "7.671,65", "bt": "8.190,99" },
		  { "data": "set/22", "verde": "5.872,38", "azul": "6.301,99", "bt": "5.832,09" },
		  { "data": "ago/22", "verde": "5.851,53", "azul": "6.223,25", "bt": "6.081,03" },
		  { "data": "jul/22", "verde": "5.068,16", "azul": "6.463,47", "bt": "5.742,20" },
		  { "data": "jun/22", "verde": "5.600,05", "azul": "6.064,75", "bt": "5.429,82" },
		  { "data": "TOTAL APÓS 12 MESES", "verde": "91.958,87", "azul": "95.066,59", "bt": "94.510,91" }
		],
		"tabela_contrato_comparado": [
		  {
			"data": "mai/23", "consumo": "4.961,33", "demanda": "1.308,92", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,26", "impostos": "270,53", "total": "6.541,04"
		  },
		  {
			"data": "abr/23", "consumo": "6.330,95", "demanda": "1.586,01", "ultrapassagem": "554,18",
			"bip": "0,00", "ere": "0,22", "impostos": "365,48", "total": "8.836,83"
		  },
		  {
			"data": "mar/23", "consumo": "8.903,56", "demanda": "1.669,82", "ultrapassagem": "721,99",
			"bip": "0,00", "ere": "0,02", "impostos": "487,31", "total": "11.782,68"
		  },
		  {
			"data": "fev/23", "consumo": "7.250,78", "demanda": "1.852,59", "ultrapassagem": "1.087,34",
			"bip": "0,00", "ere": "0,06", "impostos": "439,60", "total": "10.630,37"
		  },
		  {
			"data": "jan/23", "consumo": "6.654,22", "demanda": "1.347,88", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,00", "impostos": "345,23", "total": "8.347,34"
		  },
		  {
			"data": "dez/22", "consumo": "6.271,53", "demanda": "1.347,88", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,00", "impostos": "328,16", "total": "7.947,57"
		  },
		  {
			"data": "nov/22", "consumo": "5.796,56", "demanda": "1.308,92", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,00", "impostos": "370,25", "total": "7.476,55"
		  },
		  {
			"data": "out/22", "consumo": "7.771,91", "demanda": "1.308,92", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,00", "impostos": "332,14", "total": "9.412,97"
		  },
		  {
			"data": "set/22", "consumo": "4.320,14", "demanda": "1.308,92", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,00", "impostos": "193,06", "total": "5.822,13"
		  },
		  {
			"data": "ago/22", "consumo": "4.300,14", "demanda": "1.308,92", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,00", "impostos": "242,48", "total": "5.851,53"
		  },
		  {
			"data": "jul/22", "consumo": "4.507,42", "demanda": "1.308,92", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,85", "impostos": "251,61", "total": "6.068,16"
		  },
		  {
			"data": "jun/22", "consumo": "5.600,05", "demanda": "1.308,92", "ultrapassagem": "0,00",
			"bip": "0,00", "ere": "0,85", "impostos": "306,04", "total": "7.215,86"
		  },
		  {
			"data": "\\textbf{CONTRATO PROPOSTO}", "consumo": "\\textbf{68.802,72}", "demanda": "\\textbf{16.986,15}", "ultrapassagem": "\\textbf{2.363,43}",
			"bip": "\\textbf{0,00}", "ere": "\\textbf{3,30}", "impostos": "\\textbf{3.803,27}", "total": "\\textbf{91.958,87}"
		  },
		  {
			"data": "\\textbf{CONTRATO ATUAL}", "consumo": "\\textbf{68.802,72}", "demanda": "\\textbf{15.029,30}", "ultrapassagem": "\\textbf{8.141,80}",
			"bip": "\\textbf{0,00}", "ere": "\\textbf{3,30}", "impostos": "\\textbf{3.968,14}", "total": "\\textbf{95.945,25}"
		  }
		],
		"resumo_proposta": [
		  {
			"titulo": "Modalidade",
			"atual": "Tarifa Horária Verde",
			"proposto": "Tarifa Horária Verde"
		  },
		  {
			"titulo": "Demanda Ponta",
			"atual": "-",
			"proposto": "-"
		  },
		  {
			"titulo": "Demanda Fora Ponta",
			"atual": "30 kW",
			"proposto": "43 kW"
		  },
		  {
			"titulo": "Custo anual",
			"atual": "R\\$ 95.945,25",
			"proposto": "R\\$ 91.958,87"
		  },
		  {
			"titulo": "Economia em relação à Atual",
			"atual": "-",
			"proposto": "(R\\$ 3.986,38/ano)"
		  }
		]
}

# Envia a requisição POST com os dados JSON
response = requests.post(url, json=dados, headers=headers)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    with open("relatorio_gerado.pdf", "wb") as f:
        f.write(response.content)
    print("✅ PDF salvo com sucesso: relatorio_gerado.pdf")
else:
    print(f"❌ Erro ao gerar relatório: {response.status_code} - {response.text}")
