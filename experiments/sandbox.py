import requests
import xml.etree.ElementTree as ET

def extract_paper_info(pdf_path):
    # Grobid endpoint for full text (headers + body + citations)
    url = "http://localhost:8070/api/processFulltextDocument"
    
    with open(pdf_path, 'rb') as f:
        files = {'input': f}
        # This sends the PDF to your 500MB Docker container
        response = requests.post(url, files=files)
    
    if response.status_code != 200:
        print("Error: Grobid is not running or the file is invalid.")
        return

    # Grobid returns TEI XML. We need to parse the tags.
    # The '{http://www.tei-c.org/ns/1.0}' is the standard TEI namespace
    ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
    root = ET.fromstring(response.text)

    # 1. Extract Title
    title_element = root.find(".//tei:titleStmt/tei:title", ns)
    # If it exists, get the text; otherwise, use a fallback string
    title = title_element.text if title_element is not None else "Unknown Title"
    
    # 2. Extract Section Headers (Introduction, Methods, etc.)
    # High-fidelity means we know exactly where sections start!
    sections = []
    for head in root.findall(".//tei:body//tei:head", ns):
        if head.text:
            sections.append(head.text)

    print(f"--- High-Fidelity Extraction ---")
    print(f"TITLE: {title}")
    print(f"SECTIONS FOUND: {', '.join(sections)}")

# Usage: Point this to one of your sample PDFs
extract_paper_info("samples/Attention_is_all_you_need.pdf")