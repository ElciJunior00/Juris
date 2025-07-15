# Juris

Simple utilities for processing legal PDFs.

## analyze_pdfs.py

`analyze_pdfs.py` scans the `pdfs` directory for PDF files, extracts the text and
creates a short summary for each file. Summaries are stored in the
`summaries/` directory using the same file name with a `.summary.txt`
extension.

Run the script with:

```bash
python3 analyze_pdfs.py
```

The script requires `pypdf` or `PyPDF2` to be installed.
