#!/bin/bash

# Lista dos códigos de instalação
codigos=(
  9502790
  160005420
  160027592
  160107889
  160132427
  160140245
  160185468
  160185476
  160185479
  160209416
  160215346
  160032749
  1928057
  1684060
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
