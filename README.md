# 📚 PDF Toolkit 🛠️

A powerful and simple-to-use Python CLI tool for manipulating PDF files!  
Easily **merge**, **extract**, and **filter** pages with just a few commands. 🔥

---

## 🚀 Features

- 🔗 **Merge** multiple PDFs into a single file
- ✂️ **Extract** specific page ranges from a PDF
- 🧹 **Discriminate** (keep or remove) even/odd pages

---

## 🧰 Requirements

- 🐍 Python `3.6+`
- 📦 [`PyPDF2`](https://pypi.org/project/PyPDF2/)

---

## ⚙️ Installation

```bash
pip install PyPDF2
```

---

## 📝 Usage

Run the tool from the terminal like so:

```bash
python pdf_toolkit.py <operation> [options]
```

### 🔧 Operations

#### 🔗 Merge PDFs
Merge multiple PDF files into one.

```bash
python pdf_toolkit.py merge <output_path> <pdf_paths...>
```

Example:
```bash
python pdf_toolkit.py merge merged.pdf sample1.pdf sample2.pdf sample3.pdf
```

---

#### ✂️ Extract Pages
Extract a specific range of pages from a PDF.

```bash
python pdf_toolkit.py extract <pdf_path> <start_page> <end_page> <output_path>
```

Example:
```bash
python pdf_toolkit.py extract sample1.pdf 1 5 extracted.pdf
```

---

#### 🧹 Discriminate (Even/Odd Pages)
Keep or remove pages based on even/odd condition.

```bash
python pdf_toolkit.py discriminate <pdf_path> <condition> <output_path>
```

- `<condition>` should be either `even` or `odd`.

Example:
```bash
python pdf_toolkit.py discriminate sample1.pdf odd discriminated.pdf
```

---

## ✅ Example Commands

```bash
# Merge three PDFs
python pdf_toolkit.py merge merged.pdf sample1.pdf sample2.pdf sample3.pdf

# Extract pages 1–5 from a PDF
python pdf_toolkit.py extract sample1.pdf 1 5 extracted.pdf

# Remove all odd-numbered pages from a PDF
python pdf_toolkit.py discriminate sample1.pdf odd discriminated.pdf
```

---

## 📄 License

This project is licensed under the MIT License.  
Feel free to use, modify, and share! 🙌

---

## 🌟 Star This Repo

If you find this tool helpful, please ⭐ it on [GitHub](https://github.com/MONTYOC/PDF-Tool-Kit-)!
