import requests
from bs4 import BeautifulSoup
from scraper.pdf_utils import extract_text_from_pdf
import os

def fetch_and_extract_documents():
    pdf_url = "https://esempio.gov.it/modulo-contributo.pdf"
    pdf_path = "data/docs/modulo-contributo.pdf"

    response = requests.get(pdf_url)
    with open(pdf_path, "wb") as f:
        f.write(response.content)

    text = extract_text_from_pdf(pdf_path)
    return text[:3000]