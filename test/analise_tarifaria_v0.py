import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.optimize import minimize
# Tarifas da Tarifa Verde (linha "Atual" da planilha)
tarifas_verde_mes_a_mes = {
    'mai/23': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'abr/23': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'mar/23': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'fev/23': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'jan/23': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'dez/22': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'nov/22': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'out/22': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'set/22': {'TUSD_ponta': 1.24002, 'TE_ponta': 0.42260, 'TUSD_fora_ponta': 0.13433, 'TE_fora_ponta': 0.26380, 'Demanda': 30.44, 'ERE': 0.27703},
    'ago/22': {'TUSD_ponta': 1.25223871, 'TE_ponta': 0.42496129, 'TUSD_fora_ponta': 0.12453839, 'TE_fora_ponta': 0.26405548, 'Demanda': 31.02645161, 'ERE': 0.27746161},
    'jul/22': {'TUSD_ponta': 1.30315, 'TE_ponta': 0.4348, 'TUSD_fora_ponta':0.08374, 'TE_fora_ponta': 0.26512, 'Demanda': 33.47, 'ERE': 0.27926},
    'jun/22': {'TUSD_ponta': 1.30315, 'TE_ponta': 0.4348, 'TUSD_fora_ponta': 0.08374, 'TE_fora_ponta': 0.26512, 'Demanda': 33.47, 'ERE': 0.279263}
}

tarifas_azul_mes_a_mes = {
    'mai/23': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'abr/23': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'mar/23': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'fev/23': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'jan/23': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'dez/22': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'nov/22': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'out/22': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'set/22': {'TUSD_ponta': 0.13, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.13, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 45.59, 'Demanda_fora_ponta': 30.44 ,'ERE': 0.28},
    'ago/22': {'TUSD_ponta': 0.12, 'TE_ponta': 0.42, 'TUSD_fora_ponta': 0.12, 'TE_fora_ponta': 0.26, 'Demanda_ponta': 46.48, 'Demanda_fora_ponta': 31.03 ,'ERE': 0.28},
    'jul/22': {'TUSD_ponta': 0.08, 'TE_ponta': 0.46, 'TUSD_fora_ponta': 0.08, 'TE_fora_ponta': 0.29, 'Demanda_ponta': 50.45, 'Demanda_fora_ponta': 18.93 ,'ERE': 0.28},
    'jun/22': {'TUSD_ponta': 0.08, 'TE_ponta': 0.46, 'TUSD_fora_ponta': 0.08, 'TE_fora_ponta': 0.29, 'Demanda_ponta': 50.45, 'Demanda_fora_ponta': 18.93 ,'ERE': 0.28}
}

# Dados mensais reais (jun/22 a mai/23)
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

df = pd.DataFrame(dados_mensais)

media_pis = df['PIS'].mean()
media_cofins = df['COFINS'].mean()

# Função para calcular o custo anual com base na demanda contratada
def calcular_custo_anual(demanda_contratada, demanda_p_contratada, demanda_fp_contratada, media_imp, modalidade):
    total = 0
    total_mes_sem_imposto = 0
    ultrapassagem_p = 0
    ultrapassagem_fp = 0
    demanda_fp = 0
    demanda_p = 0

    for mes in dados_mensais:

        if (media_imp == False):
            if(modalidade == 0):
                tarifas = tarifas_verde_mes_a_mes[mes['mes']]
            else:
                tarifas = tarifas_azul_mes_a_mes[mes['mes']]
        else:
            if(modalidade == 0):
                tarifas = tarifas_verde_mes_a_mes['mai/23']
            else:
                tarifas = tarifas_azul_mes_a_mes['mai/23']
        cp = mes['EAP']
        cfp = mes['EAFP']
        dmp = mes['DMP']
        dmfp = mes['DMFP']
        tusd_ponta = cp * tarifas['TUSD_ponta']
        te_ponta = cp * tarifas['TE_ponta']
        tusd_fora = cfp * tarifas['TUSD_fora_ponta']
        te_fora = cfp * tarifas['TE_fora_ponta']
        
        if modalidade == 0:
            if (max(dmp,dmfp) > demanda_contratada):
                demanda = max(dmp,dmfp) * tarifas['Demanda']
            else:
                demanda = demanda_contratada * tarifas['Demanda']
            if (max(dmp,dmfp) - demanda_contratada) > 0.05*demanda_contratada:
                ultrapassagem = (max(dmp,dmfp) - demanda_contratada) * 2 * tarifas['Demanda']
            else:
                ultrapassagem = 0
        else:
            if(dmp > demanda_p_contratada):
                demanda_p = dmp * tarifas['Demanda_ponta']
            else:
                demanda_p = demanda_p_contratada * tarifas['Demanda_ponta']
            if(dmfp > demanda_fp_contratada):
                demanda_fp = dmfp * tarifas['Demanda_fora_ponta']
            else:
                demanda_fp = demanda_fp_contratada * tarifas['Demanda_fora_ponta']
            demanda = demanda_p + demanda_fp
            if((dmp - demanda_p_contratada) > 0.05*demanda_p_contratada):
                ultrapassagem_p = (dmp - demanda_p_contratada)* 2 * tarifas['Demanda_ponta']
            else:
                ultrapassagem_p = 0
            if((dmfp - demanda_fp_contratada) > 0.05*demanda_fp_contratada):
                ultrapassagem_fp = (dmfp - demanda_fp_contratada)* 2 * tarifas['Demanda_fora_ponta']
            else:
                ultrapassagem_fp = 0
            ultrapassagem = ultrapassagem_p + ultrapassagem_fp
        # print(f"mes: {mes['mes']} - {demanda}")
        ere = mes['ERE'] * tarifas['ERE']
        total_mes = tusd_ponta + te_ponta + tusd_fora + te_fora + demanda + ultrapassagem + ere
        if (media_imp == False):
            pis = total_mes/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['PIS']/100
            cofins = total_mes/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['COFINS']/100
            icms = total_mes/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['ICMS']/100
        else:
            pis = total_mes/((1-(media_pis + media_cofins + mes['ICMS'])/100))*media_pis/100
            cofins = total_mes/((1-(media_pis + media_cofins + mes['ICMS'])/100))*media_cofins/100
            icms = total_mes/((1-(media_pis + media_cofins + mes['ICMS'])/100))*mes['ICMS']/100
        total_mes_imposto = total_mes + pis + cofins + icms
        total += total_mes_imposto
        total_mes_sem_imposto += total_mes
        # print(f"mes: {mes['mes']} - {total_mes}, {pis}, {cofins},")
    return total

# Otimização com scipy (mínimo global no intervalo) - Verde
resultado = minimize_scalar(lambda d: calcular_custo_anual(d, 0, 0, True, 0), bounds=(30, 60), method='bounded')

# Demanda ótima arredondada para inteiro
demanda_otima = round(resultado.x)
custo_minimo = calcular_custo_anual(demanda_otima, 0, 0, True, 0)

# Impressão dos resultados
print(f"Demanda contratada ótima (verde): {demanda_otima} kW")
print(f"Custo anual mínimo estimado: R$ {custo_minimo:,.2f}")

# Otimização com scipy (mínimo global no intervalo) - Azul
# Chute inicial (ponta e fora de ponta)
x0 = [30.0, 30.0]
# Restrições de intervalo: entre 20 e 60 kW
bounds = [(20, 60), (20, 60)]
resultado = minimize(lambda x: calcular_custo_anual(0,x[0], x[1], True, 1), x0=x0, bounds=bounds, method='L-BFGS-B')

# Demanda ótima arredondada para inteiro
demanda_p_otima = round(resultado.x[0])
demanda_fp_otima = round(resultado.x[1])
custo_minimo = calcular_custo_anual(0, demanda_p_otima, demanda_fp_otima, True, 1)

# Impressão dos resultados
print(f"Demanda contratada (ponta, fora ponta) ótima (azul): ({demanda_p_otima}, {demanda_fp_otima}) kW")
print(f"Custo anual mínimo estimado: R$ {custo_minimo:,.2f}")

# # Gráfico para visualização
# demandas_testadas = np.arange(30, 61)
# custos_testados = [calcular_custo_anual(d) for d in demandas_testadas]

# plt.plot(demandas_testadas, custos_testados, marker='o', color='orange')
# plt.axvline(demanda_otima, color='red', linestyle='--', label=f'Demanda ótima: {demanda_otima} kW')
# plt.title('Custo Anual x Demanda Contratada (Tarifa Verde)')
# plt.xlabel('Demanda (kW)')
# plt.ylabel('Custo Anual (R$)')
# plt.legend()
# plt.grid(True)
# plt.tight_layout()
# plt.show()
