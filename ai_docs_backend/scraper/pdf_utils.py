import pdfplumber

def extract_text_from_pdf(path: str) -> str:
    try:
        with pdfplumber.open(path) as pdf:
            text = "\n".join(page.extract_text() or "" for page in pdf.pages)
        return text.strip()
    except Exception as e:
        print(f"Errore durante l'estrazione PDF: {e}")
        return ""