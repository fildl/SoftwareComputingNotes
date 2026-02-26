#!/bin/bash

# Controlla se è stato passato un argomento
if [ "$#" -ne 1 ]; then
    echo "Uso: $0 <nome_file.md_o_ipynb>"
    exit 1
fi

FILE=$1
ESTENSIONE="${FILE##*.}"
NOMEBASE="${FILE%.*}"

# Controlla l'estensione del file
if [ "$ESTENSIONE" == "ipynb" ]; then
    echo "Convertendo $FILE in LaTeX..."
    jupyter nbconvert --to latex "$FILE"
    
    if [ $? -eq 0 ]; then
        echo "Conversione completata: $NOMEBASE.tex creato."
        echo "Compilando $NOMEBASE.tex in PDF..."
        pdflatex -interaction=nonstopmode "$NOMEBASE.tex"
        
        if [ $? -eq 0 ]; then
            echo "Successo! File PDF creato: $NOMEBASE.pdf"
        else
            echo "Errore durante la compilazione del PDF."
        fi
    else
        echo "Errore durante la conversione del file IPYNB in LaTeX."
    fi

elif [ "$ESTENSIONE" == "md" ]; then
    echo "Convertendo $FILE in LaTeX..."
    # Presuppone che pandoc sia installato
    pandoc "$FILE" -s -o "$NOMEBASE.tex"
    
    if [ $? -eq 0 ]; then
        echo "Conversione completata: $NOMEBASE.tex creato."
        echo "Compilando $NOMEBASE.tex in PDF..."
        pdflatex -interaction=nonstopmode "$NOMEBASE.tex"
        
        if [ $? -eq 0 ]; then
            echo "Successo! File PDF creato: $NOMEBASE.pdf"
        else
            echo "Errore durante la compilazione del PDF."
        fi
    else
        echo "Errore durante la conversione del file Markdown in LaTeX."
    fi
else
    echo "Errore: Estensione del file non supportata. Usa file .md o .ipynb."
fi

# Pulisce i file ausiliari di LaTeX
rm -f "$NOMEBASE.aux" "$NOMEBASE.log" "$NOMEBASE.out"
echo "Pulizia file ausiliari completata."
