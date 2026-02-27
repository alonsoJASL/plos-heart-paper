#!/bin/bash

# ImageMagick Figure Conversion Script
# Converts figures to journal specifications:
# - Format: TIFF or EPS
# - Resolution: 300-600 dpi (using 300 dpi as default)
# - Width: 789-2250 pixels at 300 dpi
# - Height: max 2625 pixels at 300 dpi
# - File size: <10 MB

INPUT_DIR="$1"
OUTPUT_DIR=$1"_formatted"
DPI=300
MAX_WIDTH=2250
MAX_HEIGHT=2625
MAX_SIZE_MB=10

# Create output directory
mkdir -p "$OUTPUT_DIR"

# Function to convert and optimize a single figure
process_figure() {
    local input_file="$1"
    local base_name=$(basename "$input_file")
    local file_name="${base_name%.*}"
    local output_file="${OUTPUT_DIR}/${file_name}.tif"
    
    echo "Processing: $input_file"
    
    # Convert to TIFF with proper specifications
    magick "$input_file" \
        -density ${DPI} \
        -units PixelsPerInch \
        -resize "${MAX_WIDTH}x${MAX_HEIGHT}>" \
        -compress lzw \
        -depth 8 \
        "$output_file"
    
    # Check file size
    file_size=$(stat -f%z "$output_file" 2>/dev/null || stat -c%s "$output_file" 2>/dev/null)
    file_size_mb=$(echo "scale=2; $file_size / 1024 / 1024" | bc)
    
    echo "  Output: $output_file"
    echo "  Size: ${file_size_mb} MB"
    echo "  Resolution: ${DPI} dpi"
    
    # Warn if file size exceeds limit
    if (( $(echo "$file_size_mb > $MAX_SIZE_MB" | bc -l) )); then
        echo "  WARNING: File size exceeds ${MAX_SIZE_MB} MB!"
        echo "  Consider reducing quality or dimensions"
    fi
    
    echo ""
}

# Process all common image formats in the figures directory
for ext in jpg jpeg png tif tiff eps pdf; do
    for file in "$INPUT_DIR"/*.$ext "$INPUT_DIR"/*.$( echo $ext | tr '[:lower:]' '[:upper:]' ); do
        if [ -f "$file" ]; then
            process_figure "$file"
        fi
    done
done

echo "Conversion complete! Check the $OUTPUT_DIR directory."
echo ""
echo "To rename files to Fig1.tif, Fig2.tif format, run:"
echo "cd $OUTPUT_DIR && ls -1 *.tif | cat -n | while read n f; do mv \"\$f\" \"Fig\$n.tif\"; done"