#!/usr/bin/env bash
set -euo pipefail

MESH_DIR="/media/jsolisle/SEAGATEBACK/data/14_fda/10_final_models"
IFMT="carp_bin"
MESH_SUFFIX="myocardium_AV_FEC_BB_lvrv"
OUTPUT_CSV="reviews_data/mesh_quality_summary.csv"

THR_INVERTED=0.99
THR_DEGENERATE=0.90

echo "mesh_id,n_elements,min,max,mean,stddev,n_inverted,pct_inverted,n_degenerate,pct_degenerate" > "$OUTPUT_CSV"

for mesh_path in "$MESH_DIR"/*/; do
    mesh_id=$(basename "$mesh_path")
    msh="${mesh_path}${MESH_SUFFIX}"

    if [ ! -f "${msh}.pts" ] && [ ! -f "${msh}.pts.gz" ]; then
        echo "  [SKIP] $mesh_id — mesh not found"
        continue
    fi

    echo "Processing $mesh_id ..."

    # Base quality run
    quality_out=$(meshtool query quality \
        -msh="$msh" \
        -ifmt="$IFMT" \
        -thr=0.0 2>&1)

    # Parse — use tab-insensitive cut on the elements line
    n_elem=$(echo "$quality_out" | grep "^Number of elements:" | awk '{print $NF}')
    stats_line=$(echo "$quality_out" | grep "^Min:")
    min=$(echo  "$stats_line" | awk '{print $2}')
    max=$(echo  "$stats_line" | awk '{print $4}')
    mean=$(echo "$stats_line" | awk '{print $6}')
    std=$(echo  "$stats_line" | awk '{print $8}')

    # Inverted threshold run
    inv_out=$(meshtool query quality \
        -msh="$msh" \
        -ifmt="$IFMT" \
        -thr=${THR_INVERTED} 2>&1)
    n_inv=$(echo "$inv_out" | grep "quality above" | awk '{print $NF}')
    pct_inv=$(awk "BEGIN {printf \"%.4f\", ${n_inv}/${n_elem}*100}")

    # Degenerate threshold run
    deg_out=$(meshtool query quality \
        -msh="$msh" \
        -ifmt="$IFMT" \
        -thr=${THR_DEGENERATE} 2>&1)
    n_deg=$(echo "$deg_out" | grep "quality above" | awk '{print $NF}')
    pct_deg=$(awk "BEGIN {printf \"%.4f\", ${n_deg}/${n_elem}*100}")

    echo "${mesh_id},${n_elem},${min},${max},${mean},${std},${n_inv},${pct_inv},${n_deg},${pct_deg}" >> "$OUTPUT_CSV"
done

echo ""
echo "Done. Results written to $OUTPUT_CSV"

echo ""
echo "--- Global summary ---"
awk -F',' 'NR>1 {
    min_sum+=$3; max_sum+=$4; mean_sum+=$5; std_sum+=$6
    inv_sum+=$8; deg_sum+=$10; n++
} END {
    printf "Avg Min quality:       %.6f\n", min_sum/n
    printf "Avg Max quality:       %.6f\n", max_sum/n
    printf "Avg Mean quality:      %.6f\n", mean_sum/n
    printf "Avg Stddev:            %.6f\n", std_sum/n
    printf "Avg %% inverted:        %.4f%%\n", inv_sum/n
    printf "Avg %% near-degenerate: %.4f%%\n", deg_sum/n
}' "$OUTPUT_CSV"