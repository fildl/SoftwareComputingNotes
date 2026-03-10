# Software Computing Notes

This repository contains the notes for the Software and Computing course.

The notes are written in Jupyter Notebook (`.ipynb`) format.

## How to compile to PDF

To get the notes formatted into a PDF file, you can use the provided script.

### Requirements
- **LaTeX** (e.g. MacTeX)
- **Jupyter** (`jupyter nbconvert`)
- **Pandoc** (required to convert `.ipynb` files)

### Using the conversion script

To convert all files to LaTeX and then automatically generate a single, unified PDF:

```bash
./convert_notes.sh
```

The script will take care of converting the source format to the intermediate `.tex` format, generating a unified `master.tex`, compiling it using `pdflatex` to a single `master.pdf` file, and finally cleaning up unnecessary secondary auxiliary files (such as `.aux`, `.log`, `.out`).
