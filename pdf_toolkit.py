import os
import sys
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

def merge_pdfs(pdf_paths, output_path):
    """Merges multiple PDF files into a single PDF file."""
    merger = PdfMerger()
    for path in pdf_paths:
        try:
            merger.append(path)
        except FileNotFoundError:
            print(f"Error: File not found: {path}")
            return False
        except Exception as e:
            print(f"Error: Could not read file: {path} - {e}")
            return False
    try:
        merger.write(output_path)
        merger.close()
        print(f"Successfully merged PDFs into {output_path}")
        return True
    except Exception as e:
        print(f"Error: Could not write to file: {output_path} - {e}")
        return False

def extract_pages(pdf_path, start_page, end_page, output_path):
    """Extracts a range of pages from a PDF file into a new PDF file."""
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        if 1 <= start_page <= end_page <= len(reader.pages):
            for page_number in range(start_page, end_page + 1):
                page = reader.pages[page_number - 1]
                writer.add_page(page)
        else:
            print(f"Error: Invalid page number range: {start_page}-{end_page}")
            return False
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        print(f"Successfully extracted pages into {output_path}")
        return True
    except FileNotFoundError:
        print(f"Error: File not found: {pdf_path}")
        return False
    except Exception as e:
        print(f"Error: Could not extract pages: {e}")
        return False

def discriminate_pages(pdf_path, condition, output_path):
    """Removes or selects pages based on a condition (even or odd)."""
    try:
        reader = PdfReader(pdf_path)
        writer = PdfWriter()
        for i, page in enumerate(reader.pages):
            page_number = i + 1
            if condition == "even" and page_number % 2 != 0:
                writer.add_page(page)
            elif condition == "odd" and page_number % 2 == 0:
                writer.add_page(page)
        with open(output_path, "wb") as output_file:
            writer.write(output_file)
        print(f"Successfully discriminated pages into {output_path}")
        return True
    except FileNotFoundError:
        print(f"Error: File not found: {pdf_path}")
        return False
    except Exception as e:
        print(f"Error: Could not discriminate pages: {e}")
        return False

def main():
    """Main function to run the PDF toolkit."""
    if len(sys.argv) < 2:
        print("Usage: python pdf_toolkit.py <operation> [options]")
        print("Operations: merge, extract, discriminate")
        return

    operation = sys.argv[1]

    if operation == "merge":
        if len(sys.argv) < 4:
            print("Usage: python pdf_toolkit.py merge <output_path> <pdf_paths...>")
            return
        output_path = sys.argv[2]
        pdf_paths = sys.argv[3:]
        print(f"Output path: {output_path}")
        print(f"PDF paths: {pdf_paths}")
        if not merge_pdfs(pdf_paths, output_path):
            print("PDF merging failed.")

    elif operation == "extract":
        if len(sys.argv) < 5:
            print("Usage: python pdf_toolkit.py extract <pdf_path> <page_numbers> <output_path>")
            return
        pdf_path = sys.argv[2]
        page_numbers_str = sys.argv[3]
        try:
            page_numbers = [int(x.strip()) for x in page_numbers_str.split(",")]
        except ValueError:
            print("Error: Invalid page numbers.")
            return
        output_path = sys.argv[4]
        if not extract_pages(pdf_path, page_numbers, output_path):
            print("Page extraction failed.")

    elif operation == "discriminate":
        if len(sys.argv) < 5:
            print("Usage: python pdf_toolkit.py discriminate <pdf_path> <condition> <output_path>")
            return
        pdf_path = sys.argv[2]
        condition = sys.argv[3]
        output_path = sys.argv[4]
        if not discriminate_pages(pdf_path, condition, output_path):
            print("Page discrimination failed.")

    else:
        print("Invalid operation. Choose from merge, extract, or discriminate.")

if __name__ == "__main__":
    main()
