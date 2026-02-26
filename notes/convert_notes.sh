#!/bin/bash

echo "Batch converting .ipynb notes to LaTeX..."

ipynb_files=(*.ipynb)

if [ ${#ipynb_files[@]} -eq 0 ] || [ ! -e "${ipynb_files[0]}" ]; then
    echo "No .ipynb files found in this directory."
    exit 1
fi

for file in "${ipynb_files[@]}"; do
    echo "Converting $file to LaTeX..."
    jupyter nbconvert --to latex "$file"
done

echo "All files converted. Combining everything into master.tex..."

# Inline Python script to safely combine LaTeX document bodies
python3 - << 'EOF'
import sys, glob

tex_files = [f for f in sorted(glob.glob("*.tex")) if f != "master.tex"]

if not tex_files:
    sys.exit(0)

preamble = []
with open(tex_files[0], 'r', encoding='utf-8') as f:
    for line in f:
        preamble.append(line)
        if r'\begin{document}' in line:
            break

with open('master.tex', 'w', encoding='utf-8') as out:
    for line in preamble:
        out.write(line)
    
    for tex in tex_files:
        out.write("\n% --- " + tex + " ---\n")
        body = False
        with open(tex, 'r', encoding='utf-8') as f_in:
            for line in f_in:
                if r'\end{document}' in line:
                    break
                if body:
                    out.write(line)
                if r'\begin{document}' in line:
                    body = True
        out.write("\n\\newpage\n")
        
    out.write("\\end{document}\n")
EOF

if [ -f "master.tex" ]; then
    echo "Compiling master.tex into PDF..."
    pdflatex -interaction=nonstopmode master.tex
    # Double pass for indices / references (optional but recommended for LaTeX)
    pdflatex -interaction=nonstopmode master.tex
    
    # Clean up
    rm -f *.aux *.log *.out
    echo "============================="
    echo "Done! Created master.pdf"
    echo "============================="
else
    echo "Error creating master.tex"
fi
