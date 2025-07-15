import os
from pathlib import Path
from typing import List

try:
    from pypdf import PdfReader
except ModuleNotFoundError:
    # PyPDF2 is a common alternative
    from PyPDF2 import PdfReader  # type: ignore


def extract_text_from_pdf(pdf_path: Path) -> str:
    """Extract text from a PDF using pypdf."""
    reader = PdfReader(str(pdf_path))
    text_parts: List[str] = []
    for page in reader.pages:
        text_parts.append(page.extract_text() or "")
    return "\n".join(text_parts)


def summarize_text(text: str, max_sentences: int = 5) -> str:
    """Simple summarization: return the first few sentences."""
    sentences = [s.strip() for s in text.split(".") if s.strip()]
    return ". ".join(sentences[:max_sentences]) + ("." if sentences else "")


def process_pdf(pdf_path: Path, out_dir: Path) -> None:
    text = extract_text_from_pdf(pdf_path)
    summary = summarize_text(text)
    out_file = out_dir / f"{pdf_path.stem}.summary.txt"
    out_file.write_text(summary, encoding="utf-8")
    print(f"Saved summary to {out_file}")


def main() -> None:
    pdf_dir = Path("pdfs")
    out_dir = Path("summaries")
    out_dir.mkdir(exist_ok=True)

    for pdf_file in sorted(pdf_dir.glob("*.pdf")):
        try:
            process_pdf(pdf_file, out_dir)
        except Exception as exc:
            print(f"Failed to process {pdf_file.name}: {exc}")


if __name__ == "__main__":
    main()
