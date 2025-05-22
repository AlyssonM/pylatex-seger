#!/bin/bash

# Lista dos códigos de instalação
codigos=(
  144762
  1126065
  1358178
  1371609
  1423527
  160140245
  160215346
  824412
  9501246
  161139107
  9502403
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
