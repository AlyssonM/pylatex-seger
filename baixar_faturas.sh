#!/bin/bash

# Lista dos códigos de instalação
codigos=(
  144021
  144488
  144701
  144762
  145344
  147057
  147170
  147446
  148559
  150806
  612893
  642149
  731853
  824411
  934167
  1126065
  1242296
  1259652
  1273999
  1358178
  1363069
  1371609
  1423527
  1684060
  1744282
  1746874
  1788583
  1928057
  1978139
  9500002
  9500016
  9500743
  9500753
  9500986
  9501531
  9501532
  9501547
  9501960
  9502261
  9502340
  9502403
  9502682
  9502723
  9502790
  9502839
  160005420
  160011997
  160027592
  160032749
  160065894
  160094307
  160098260
  160101225
  160107308
  160107889
  160132427
  160140245
  160185468
  160185476
  160185479
  160209416
  160215346
  160639774
  160663680
  160675865
  160694592
  160774728
  160993362
  161078408
  161080585
  161091963
  161139107
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
