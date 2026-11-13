#!/bin/bash
# uso: run_reel3.sh <pasta> <escala> [workers]  -> renderiza 1050 quadros (60 fps) em paralelo
D=$1; SC=$2; W=${3:-7}; N=1050; PER=$(( (N + W - 1) / W ))
mkdir -p "$D"
for ((i=0;i<W;i++)); do
  FROM=$((i*PER)); TO=$(( (i+1)*PER )); [ $TO -gt $N ] && TO=$N
  FROM=$FROM TO=$TO node "$(dirname "$0")/render_reel4.mjs" "$D" "$SC" > "$D/log_$i.txt" 2>&1 &
done
wait
echo DONE
