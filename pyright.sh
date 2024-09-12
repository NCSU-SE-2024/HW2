#!/bin/bash
# Save this script as `pylint_all.sh` and run it from your repository root.

output_file="/mnt/d/ncsu_se_fall_24/HW2/pyright_report.txt"

# Clear or create the output file
> $output_file

# Find and lint each Python file
for file in $(find . -name "*.py"); do
    echo "Checking $file" >> $output_file
    pyright "$file" >> $output_file
    echo -e "\n" >> $output_file  # Add a new line after each file's report
done