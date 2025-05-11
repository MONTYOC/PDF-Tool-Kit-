# PDF Toolkit

This is a Python tool for manipulating PDF files. It can merge multiple PDF files into a single PDF file, extract specific pages from a PDF file, and discriminate pages based on a condition (even or odd).

## Requirements

*   Python 3.6 or higher
*   PyPDF2 library

## Installation

```
pip install PyPDF2
```

## Usage

The script can be run from the command line with the following syntax:

```
python pdf_toolkit.py <operation> [options]
```

### Operations

*   **merge**: Merges multiple PDF files into a single PDF file.
    *   Usage: `python pdf_toolkit.py merge <output_path> <pdf_paths...>`
    *   Example: `python pdf_toolkit.py merge merged.pdf sample1.pdf sample2.pdf sample3.pdf`
*   **extract**: Extracts a range of pages from a PDF file into a new PDF file.
    *   Usage: `python pdf_toolkit.py extract <pdf_path> <start_page> <end_page> <output_path>`
    *   Example: `python pdf_toolkit.py extract sample1.pdf 1 5 extracted.pdf`
*   **discriminate**: Removes or selects pages based on a condition (even or odd).
    *   Usage: `python pdf_toolkit.py discriminate <pdf_path> <condition> <output_path>`
    *   Example: `python pdf_toolkit.py discriminate sample1.pdf even discriminated.pdf`

### Example

To merge three PDF files named `sample1.pdf`, `sample2.pdf`, and `sample3.pdf` into a single PDF file named `merged.pdf`, run the following command:

```
python pdf_toolkit.py merge merged.pdf sample1.pdf sample2.pdf sample3.pdf
```

To extract pages 1 to 5 from a PDF file named `sample1.pdf` into a new PDF file named `extracted.pdf`, run the following command:

```
python pdf_toolkit.py extract sample1.pdf 1 5 extracted.pdf
```

To remove all odd-numbered pages from a PDF file named `sample1.pdf` and save the result to a new PDF file named `discriminated.pdf`, run the following command:

```
python pdf_toolkit.py discriminate sample1.pdf odd discriminated.pdf
