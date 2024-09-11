import os
import tkinter as tk
from tkinter import filedialog
from docx2pdf import convert


def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    return folder_path


def convert_docx_to_pdf(folder_path):
    docx_files = [f for f in os.listdir(folder_path) if f.endswith(".docx")]
    pdf_names = {}

    for docx_file in docx_files:
        base_name = docx_file  # docx_file[:5]
        if base_name in pdf_names:
            pdf_names[base_name] += 1
            pdf_name = f"{base_name}{pdf_names[base_name]:02d}.pdf"
        else:
            pdf_names[base_name] = 1
            pdf_name = f"{base_name}.pdf"

        docx_path = os.path.join(folder_path, docx_file)
        pdf_path = os.path.join(folder_path, pdf_name)
        convert(docx_path, pdf_path)
        print(f"Converted {docx_file} to {pdf_name}")


if __name__ == "__main__":
    folder = select_folder()
    if folder:
        convert_docx_to_pdf(folder)
    else:
        print("No folder selected.")
