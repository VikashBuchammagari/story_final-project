import os
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text()
    return text

def extract_and_store_text(pdf_folder, output_file):
    all_text_data = ""  
    if os.path.exists(pdf_folder):
        pdf_files = [file_name for file_name in os.listdir(pdf_folder) if file_name.endswith('.pdf')]
        total_files = len(pdf_files)
        print(f"Extracting text from {total_files} PDF files...")
        for i, file_name in enumerate(pdf_files, 1):
            pdf_path = os.path.join(pdf_folder, file_name)
            text = extract_text_from_pdf(pdf_path)
            all_text_data += text
            print(f"Processed file {i}/{total_files}: {file_name}")
        print("Text extraction completed.")
    else:
        print("Folder", pdf_folder, "not found.")

    with open(output_file, 'w') as f:
        f.write(all_text_data)

pdf_folder = "X-files"
output_file = "all_text_data.txt"

extract_and_store_text(pdf_folder, output_file)
