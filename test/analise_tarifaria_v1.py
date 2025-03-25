import pandas as pd
import numpy as np
from scipy.optimize import minimize_scalar, minimize
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from mpl_toolkits.mplot3d import Axes3D

# Dados de consumo mensal
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

# Tarifas 
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
    'jul/22': {'TUSD_ponta': 1.30315, 'TE_ponta': 0.4348, 'TUSD_fora_ponta': 0.08374, 'TE_fora_ponta': 0.26512, 'Demanda': 33.47, 'ERE': 0.27926},
    'jun/22': {'TUSD_ponta': 1.30315, 'TE_ponta': 0.4348, 'TUSD_fora_ponta': 0.08374, 'TE_fora_ponta': 0.26512, 'Demanda': 33.47, 'ERE': 0.27926}
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

tarifas_bt_mes_a_mes = {
        'mai/23': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'abr/23': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'mar/23': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'fev/23': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'jan/23': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'dez/22': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'nov/22': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'out/22': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'set/22': {'consumo_unitario': 0.67384, 'ere': 0.27926},
        'ago/22': {'consumo_unitario': 0.63911064516129, 'ere': 0.27926},
        'jul/22': {'consumo_unitario': 0.61051, 'ere': 0.26292},
        'jun/22': {'consumo_unitario': 0.61051, 'ere': 0.26292},
    }


# Dados de impostos médios
df = pd.DataFrame(dados_mensais)
media_pis = df['PIS'].mean()
media_cofins = df['COFINS'].mean()

# Funções
def calcular_custo_tarifa_verde(demanda_contratada, media_imp=True):
    total = 0
    for mes in dados_mensais:
        if (media_imp == False):
            tarifas = tarifas_verde_mes_a_mes[mes['mes']]
        else:
            tarifas = tarifas_verde_mes_a_mes['mai/23']
        cp, cfp, dmp, dmfp = mes['EAP'], mes['EAFP'], mes['DMP'], mes['DMFP']
        tusd_ponta = cp * tarifas['TUSD_ponta']
        te_ponta = cp * tarifas['TE_ponta']
        tusd_fora = cfp * tarifas['TUSD_fora_ponta']
        te_fora = cfp * tarifas['TE_fora_ponta']
        demanda = max(dmp, dmfp) * tarifas['Demanda'] if max(dmp, dmfp) > demanda_contratada else demanda_contratada * tarifas['Demanda']
        ultrapassagem = (max(dmp, dmfp) - demanda_contratada) * 2 * tarifas['Demanda'] if (max(dmp, dmfp) - demanda_contratada) > 0.05 * demanda_contratada else 0
        ere = mes['ERE'] * tarifas['ERE']
        subtotal = tusd_ponta + te_ponta + tusd_fora + te_fora + demanda + ultrapassagem + ere
        if (media_imp == False):
            pis = subtotal/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['PIS']/100
            cofins = subtotal/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['COFINS']/100
            icms = subtotal/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['ICMS']/100
        else:
            pis = subtotal/((1-(media_pis + media_cofins + mes['ICMS'])/100))*media_pis/100
            cofins = subtotal/((1-(media_pis + media_cofins + mes['ICMS'])/100))*media_cofins/100
            icms = subtotal/((1-(media_pis + media_cofins + mes['ICMS'])/100))*mes['ICMS']/100

        total += subtotal + pis + cofins + icms
    return total

def calcular_custo_tarifa_azul(x, media_imp=True):
    demanda_p, demanda_fp = x
    total = 0
    for mes in dados_mensais:
        if (media_imp == False):
            tarifas = tarifas_azul_mes_a_mes[mes['mes']]
        else:
            tarifas = tarifas_azul_mes_a_mes['mai/23']
        cp, cfp, dmp, dmfp = mes['EAP'], mes['EAFP'], mes['DMP'], mes['DMFP']
        tusd_ponta = cp * tarifas['TUSD_ponta']
        te_ponta = cp * tarifas['TE_ponta']
        tusd_fora = cfp * tarifas['TUSD_fora_ponta']
        te_fora = cfp * tarifas['TE_fora_ponta']
        demanda_p_val = dmp * tarifas['Demanda_ponta'] if dmp > demanda_p else demanda_p * tarifas['Demanda_ponta']
        demanda_fp_val = dmfp * tarifas['Demanda_fora_ponta'] if dmfp > demanda_fp else demanda_fp * tarifas['Demanda_fora_ponta']
        ultrapassagem_p = (dmp - demanda_p) * 2 * tarifas['Demanda_ponta'] if (dmp - demanda_p) > 0.05 * demanda_p else 0
        ultrapassagem_fp = (dmfp - demanda_fp) * 2 * tarifas['Demanda_fora_ponta'] if (dmfp - demanda_fp) > 0.05 * demanda_fp else 0
        ere = mes['ERE'] * tarifas['ERE']
        subtotal = tusd_ponta + te_ponta + tusd_fora + te_fora + demanda_p_val + demanda_fp_val + ultrapassagem_p + ultrapassagem_fp + ere
        if (media_imp == False):
            pis = subtotal/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['PIS']/100
            cofins = subtotal/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['COFINS']/100
            icms = subtotal/((1-(mes['PIS'] + mes['COFINS'] + mes['ICMS'])/100))*mes['ICMS']/100
        else:
            pis = subtotal/((1-(media_pis + media_cofins + mes['ICMS'])/100))*media_pis/100
            cofins = subtotal/((1-(media_pis + media_cofins + mes['ICMS'])/100))*media_cofins/100
            icms = subtotal/((1-(media_pis + media_cofins + mes['ICMS'])/100))*mes['ICMS']/100
        total += subtotal + pis + cofins + icms
    return total

def calcular_custo_tarifa_bt(media_imp=True):
    total = 0
    if (media_imp == False):
        tarifa = tarifas_bt_mes_a_mes[mes['mes']]
    else:
        tarifa = tarifas_bt_mes_a_mes['mai/23']
    for mes in dados_mensais:
        nome_mes = mes['mes']
        consumo_total = mes['EAP'] + mes['EAFP']
        subtotal = consumo_total * tarifa['consumo_unitario'] + mes['ERE'] * tarifa['ere']

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

custo_bt = calcular_custo_tarifa_bt(media_imp=True)
# total_verde = calcular_custo_tarifa_verde(43,True)
# print(total_verde)
# total_azul = calcular_custo_tarifa_azul([30, 43],True)
# print(total_azul)

# Otimização
resultado_verde = minimize_scalar(calcular_custo_tarifa_verde, bounds=(30, 60), method='bounded')
demanda_verde_otima = round(resultado_verde.x)
custo_verde_minimo = calcular_custo_tarifa_verde(demanda_verde_otima)

resultado_azul = minimize(calcular_custo_tarifa_azul, x0=[30, 30], bounds=[(20, 60), (20, 60)], method='L-BFGS-B')
demanda_p_otima = round(resultado_azul.x[0])
demanda_fp_otima = round(resultado_azul.x[1])
custo_azul_minimo = calcular_custo_tarifa_azul([demanda_p_otima, demanda_fp_otima])

# Gráfico comparativo
labels = ['Tarifa Verde', 'Tarifa Azul', 'Tarifa BT']
custos = [custo_verde_minimo, custo_azul_minimo, custo_bt]

fig, ax = plt.subplots()
ax.bar(labels, custos, color=['green', 'blue', 'red'])
ax.set_title('Comparativo de Custo Anual por Modalidade Tarifária')
ax.set_ylabel('Custo Total (R$)')
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('R$ {x:,.0f}'))
plt.tight_layout()
# Salva como PNG
output_path = "./custo_modalidade_tarifaria.png"
plt.savefig(output_path)
plt.close()

demanda_range = np.linspace(20, 60, 100)
custos_verde = [calcular_custo_tarifa_verde(d, media_imp=True) for d in demanda_range]
plt.figure(figsize=(10, 6))
plt.plot(demanda_range, custos_verde, label='Custo Total', color='green')
plt.axvline(demanda_verde_otima, color='red', linestyle='--', label=f'Demanda ótima: {demanda_verde_otima} kW')
plt.xlabel('Demanda Contratada (kW)')
plt.ylabel('Custo Anual (R$)')
plt.title('Tarifa Verde - Custo vs Demanda Contratada')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("otimizacao_tarifa_verde.png")
plt.close()

# Geração de grade de valores
x = np.linspace(20, 60, 20)  # Demanda ponta
y = np.linspace(20, 60, 20)  # Demanda fora de ponta
X, Y = np.meshgrid(x, y)
Z = np.array([
    [calcular_custo_tarifa_azul([dp, dfp], media_imp=True) for dp in x]
    for dfp in y
])

# Gráfico 3D
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(Y, X, Z, cmap='viridis', edgecolor='k')
ax.set_ylabel('Demanda Ponta (kW)')
ax.set_xlabel('Demanda Fora Ponta (kW)')
ax.set_zlabel('Custo Anual (R$)')
ax.set_title('Tarifa Azul - Custo vs Demandas')
plt.tight_layout()
plt.savefig("otimizacao_tarifa_azul_3d.png")
plt.close()

# Gráfico de contorno
plt.figure(figsize=(10, 6))
cp = plt.contourf(X, Y, Z, cmap='plasma', levels=30)
plt.colorbar(cp, label='Custo Anual (R$)')
plt.xlabel('Demanda Ponta (kW)')
plt.ylabel('Demanda Fora Ponta (kW)')
plt.title('Tarifa Azul - Custo Anual (Contorno)')

# Ponto ótimo
plt.plot(demanda_p_otima, demanda_fp_otima, 'ro', label='Ótimo')

# Texto com coordenadas (em branco)
plt.text(demanda_p_otima + 0.5, demanda_fp_otima + 0.5,
         f'({demanda_p_otima}, {demanda_fp_otima})',
         color='white', fontsize=12, weight='bold')

plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("otimizacao_tarifa_azul_contorno.png")
plt.close()

# Tabela final
resumo_df = pd.DataFrame({
    'Modalidade': labels,
    'Custo Anual Total (R$)': [round(c, 2) for c in custos],
    'Demanda Contratada': [f'{demanda_verde_otima} kW', f'{demanda_p_otima}/{demanda_fp_otima} kW (ponta/fora)', '-']
})

print(resumo_df)
