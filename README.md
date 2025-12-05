# PDF Summarizer App

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)
![HuggingFace](https://img.shields.io/badge/Hugging_Face-API-purple)

A simple web application to extract text from PDF files and generate concise summaries using **Hugging Face’s BART model** via API requests. Built as a learning exercise to practice integrating frontend, backend, and AI models.

---

## Project Purpose
This project was created to learn:

- FastAPI backend development
- Frontend integration using HTML, CSS, and JavaScript
- PDF text extraction using `pdfplumber`
- Calling **Hugging Face APIs** for AI-based summarization

It demonstrates a complete flow from uploading a PDF to displaying a summarized version, with plenty of room for future improvements.

---

## Key Features
- Upload PDF files and extract text
- Generate summaries using Hugging Face **inference API** (`facebook/bart-large-cnn`)
- Supports multi-page PDFs
- Responsive and simple frontend interface
- Instant display of summarized text

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/anushka746/pdf_text_summariser.git
cd pdf_text_summariser
```
###2. Install Python dependencies
```bash
pip install fastapi uvicorn pdfplumber requests python-multipart
```

###3. Set your Hugging Face API key
```bash
# Windows
set HF_TOKEN=your_huggingface_token

# Mac/Linux
export HF_TOKEN=your_huggingface_token
```

###4. Run the FastAPI server
```bash
uvicorn main:app --reload
```

###5. Open your browser

Open index.html in your browser and upload a PDF file to see the extracted text and summary.

###Technologies Used

Python 3.8+

FastAPI

Uvicorn (ASGI server)

Hugging Face API (BART)

pdfplumber (PDF text extraction)

HTML, CSS, JavaScript (frontend)

## Future Improvements

- Handle large PDFs efficiently  
- Extract text from scanned PDFs or images (OCR)  
- Support tables, charts, and complex formatting  
- Improve summary quality with better AI models  
- Enhance frontend design and usability

Project Structure
```bash
pdf_text_summariser/
├── main.py           # FastAPI backend
├── index.html        # Frontend HTML
├── script.js         # Frontend JavaScript
├── style.css         # Frontend CSS
└── README.md         # Project documentation
```
