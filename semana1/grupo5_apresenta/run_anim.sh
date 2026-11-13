#!/bin/bash
# uso: run_anim.sh <pasta> <escala> <workers> <fps>   (servidor em 127.0.0.1:8765 com raiz em semana1/)
D=$1; SC=$2; W=${3:-4}; F=${4:-30}; N=$((18*F)); PER=$(( (N + W - 1) / W ))
mkdir -p "$D"
for ((i=0;i<W;i++)); do
  FROM=$((i*PER)); TO=$(( (i+1)*PER )); [ $TO -gt $N ] && TO=$N
  FPSV=$F FROM=$FROM TO=$TO node "$(dirname "$0")/render_anim.mjs" "$D" "$SC" > "$D/log_$i.txt" 2>&1 &
done
wait
echo DONE
