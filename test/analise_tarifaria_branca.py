import random
import pandas as pd

dados_mensais = [
    {'mes': 'mai/23', 'EAP': 0861.9348, 'EAFP': 08862.0885, 'DMP': 26.1744, 'DMFP': 40.4916, 'ERE': 0.9471, 'DREP': 22.26, 'DREFP': 34.72, 'bandeira': 0.00, 'PIS': 0.61, 'COFINS': 2.81, 'ICMS': 0.00},
    {'mes': 'abr/23', 'EAP': 1093.1625, 'EAFP': 11336.5779, 'DMP': 32.3244, 'DMFP': 52.1028, 'ERE': 0.7995, 'DREP': 29.12, 'DREFP': 46.56, 'bandeira': 0.00, 'PIS': 0.73, 'COFINS': 3.36, 'ICMS': 0.00},
    {'mes': 'mar/23', 'EAP': 1626.6750, 'EAFP': 15570.3363, 'DMP': 32.0784, 'DMFP': 54.8580, 'ERE': 0.0615, 'DREP': 28.38, 'DREFP': 48.13, 'bandeira': 0.00, 'PIS': 0.8, 'COFINS': 3.68, 'ICMS': 0.00},
    {'mes': 'fev/23', 'EAP': 1187.3313, 'EAFP': 13253.7174, 'DMP': 32.9148, 'DMFP': 60.8604, 'ERE': 0.0000, 'DREP': 27.83, 'DREFP': 51.29, 'bandeira': 0.00, 'PIS': 0.82, 'COFINS': 3.76, 'ICMS': 0.00},
    {'mes': 'jan/23', 'EAP': 1133.3712, 'EAFP': 11980.6551, 'DMP': 25.9285, 'DMFP': 44.2800, 'ERE': 0.0000, 'DREP': 26.60, 'DREFP': 38.53, 'bandeira': 0.00, 'PIS': 0.65, 'COFINS': 3.02, 'ICMS': 0.00},
    {'mes': 'dez/22', 'EAP': 1006.8288, 'EAFP': 10516.0326, 'DMP': 27.3552, 'DMFP': 44.9196, 'ERE': 0.0000, 'DREP': 24.40, 'DREFP': 39.08, 'bandeira': 0.00, 'PIS': 0.45, 'COFINS': 2.08, 'ICMS': 0.00},
    {'mes': 'nov/22', 'EAP': 0955.6485, 'EAFP': 10722.2667, 'DMP': 26.7648, 'DMFP': 37.3428, 'ERE': 2.4477, 'DREP': 23.06, 'DREFP': 36.93, 'bandeira': 0.00, 'PIS': 0.46, 'COFINS': 2.1, 'ICMS': 0.00},
    {'mes': 'out/22', 'EAP': 0944.2833, 'EAFP': 10616.0685, 'DMP': 24.1572, 'DMFP': 37.1460, 'ERE': 0.0000, 'DREP': 20.72, 'DREFP': 32.47, 'bandeira': 0.00, 'PIS': 0.94, 'COFINS': 4.33, 'ICMS': 0.00},
    {'mes': 'set/22', 'EAP': 0804.3585, 'EAFP': 07492.0284, 'DMP': 21.8940, 'DMFP': 31.7340, 'ERE': 1.5867, 'DREP': 19.56, 'DREFP': 27.85, 'bandeira': 0.00, 'PIS': 1.3, 'COFINS': 5.99, 'ICMS': 0.00},
    {'mes': 'ago/22', 'EAP': 0856.1907, 'EAFP': 07225.3275, 'DMP': 21.0084, 'DMFP': 27.4536, 'ERE': 1.6728, 'DREP': 15.92, 'DREFP': 25.69, 'bandeira': 0.00, 'PIS': 1.06, 'COFINS': 4.86, 'ICMS': 0.00},
    {'mes': 'jul/22', 'EAP': 0830.9388, 'EAFP': 07851.4221, 'DMP': 19.5816, 'DMFP': 28.4376, 'ERE': 3.0627, 'DREP': 17.21, 'DREFP': 24.78, 'bandeira': 0.00, 'PIS': 0.53, 'COFINS': 2.43, 'ICMS': 0.00},
    {'mes': 'jun/22', 'EAP': 0778.1103, 'EAFP': 06946.1052, 'DMP': 18.1548, 'DMFP': 22.7796, 'ERE': 1.3161, 'DREP': 14.44, 'DREFP': 19.07, 'bandeira': 0.00, 'PIS': 0.51, 'COFINS': 2.35, 'ICMS': 0.00}
]

tarifas_branca = {
    'mai/23': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'abr/23': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'mar/23': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'fev/23': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'jan/23': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'dez/22': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'nov/22': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'out/22': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'set/22': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'ago/22': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'jul/22': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28},
    'jun/22': {'ponta': 1.25, 'intermediario': 0.85, 'fora_ponta': 0.55, 'ERE': 0.28}
}

# Dados de impostos médios
df = pd.DataFrame(dados_mensais)
media_pis = df['PIS'].mean()
media_cofins = df['COFINS'].mean()


def gerar_dados_tarifa_branca(dados_mensais):
    dados_mensais_branca = []
    
    for mes in dados_mensais:
        # Define a proporção de energia intermediária (entre 40% e 60% do EAFP)
        proporcao_intermediario = random.uniform(0.0, 0.2)
        eai = mes['EAFP'] * proporcao_intermediario
        eafp_resto = mes['EAFP'] - eai  # restante vai para fora ponta

        dados_mensais_branca.append({
            'mes': mes['mes'],
            'EAP': mes['EAP'],
            'EAI': eai,
            'EAFP': eafp_resto,
            'ERE': mes['ERE'],
            'PIS': mes['PIS'],
            'COFINS': mes['COFINS'],
            'ICMS': mes['ICMS']
        })

    return dados_mensais_branca

def calcular_custo_tarifa_branca(media_imp=True):
    total = 0
    for mes in dados_mensais_branca:
        tarifas = tarifas_branca[mes['mes']]
        subtotal = (
            mes['EAP'] * tarifas['ponta'] +
            mes['EAI'] * tarifas['intermediario'] +
            mes['EAFP'] * tarifas['fora_ponta'] +
            mes['ERE'] * tarifas['ERE']
        )

        if not media_imp:
            pis = subtotal / (1 - (mes['PIS'] + mes['COFINS'] + mes['ICMS']) / 100) * mes['PIS'] / 100
            cofins = subtotal / (1 - (mes['PIS'] + mes['COFINS'] + mes['ICMS']) / 100) * mes['COFINS'] / 100
            icms = subtotal / (1 - (mes['PIS'] + mes['COFINS'] + mes['ICMS']) / 100) * mes['ICMS'] / 100
        else:
            pis = subtotal / (1 - (media_pis + media_cofins + mes['ICMS']) / 100) * media_pis / 100
            cofins = subtotal / (1 - (media_pis + media_cofins + mes['ICMS']) / 100) * media_cofins / 100
            icms = subtotal / (1 - (media_pis + media_cofins + mes['ICMS']) / 100) * mes['ICMS'] / 100

        total += subtotal + pis + cofins + icms

    return total

dados_mensais_branca = gerar_dados_tarifa_branca(dados_mensais)
custo_tarifa_branca = calcular_custo_tarifa_branca(media_imp=True)
print(custo_tarifa_branca)