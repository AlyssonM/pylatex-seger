#!/bin/bash

# Lista dos códigos de instalação
codigos=(
  9500753       # apenas 3 Faturas
  160107308     # 0 Faturas  
  160140245     # apenas 6 Faturas
)

# Datas de início e fim
DATA_INICIO="MAI-2025"
DATA_FIM="JUN-2020"

# Endpoint da API
URL="http://localhost:5000/api/seger/faturas"

# Loop pelos códigos e faz a requisição
for codigo in "${codigos[@]}"; do
  echo "⏳ Baixando faturas para código: $codigo"
  curl -s -X POST "$URL" \
    -H "Content-Type: application/json" \
    -d "{\"instalacoes\":[\"$codigo\"], \"data_inicio\":\"$DATA_INICIO\", \"data_fim\":\"$DATA_FIM\"}"
  echo -e "\n✅ Finalizado para código: $codigo"
done