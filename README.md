# Software Computing Notes

Questa repository contiene gli appunti del corso di Software and Computing.

Gli appunti sono stesi sia in formato Jupyter Notebook (`.ipynb`) sia in formato Markdown (`.md`).

## Come compilare in PDF

Per poter avere gli appunti formattati in un bel file PDF pronto per la stampa o lo studio, è possibile utilizzare lo script presente nella cartella.

### Requisiti
- **LaTeX** (ad es. MacTeX)
- **Jupyter** (`jupyter nbconvert`)
- **Pandoc** (necessario per convertire sia i `.md` sia i `.ipynb`)

### Utilizzo dello script di conversione

Per convertire un file in LaTeX e poi generare automaticamente il PDF:

```bash
./converti_appunti.sh NOME_FILE.ipynb
# oppure
./converti_appunti.sh NOME_FILE.md
```

Lo script si occuperà di convertire da formato sorgente al formato intermedio `.tex`, compilare tramite `pdflatex` ed infine pulire i file ausiliari secondari non necessari (come `.aux`, `.log`, `.out`).
