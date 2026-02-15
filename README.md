# SemanticTextAnalyzer

Semantic text analysis tool built with FastAPI, transformer embeddings, and vector search to compare documents and generate explainable similarity insights. The system indexes reference text and performs sentence-level similarity analysis through a simple web interface.

---

## Features
- Sentence-level semantic similarity
- Hybrid TF-IDF + embedding scoring
- FastAPI backend API
- Streamlit user interface
- Vector database integration (ChromaDB)

---

## Tech Stack
Python  
FastAPI  
SentenceTransformers  
ChromaDB  
Streamlit  
scikit-learn

---

## Project Structure
api/ – FastAPI routes  
core/ – NLP processing and similarity logic  
db/ – vector storage  
ui.py – Streamlit interface

---

## Installation

Clone repository:

git clone https://github.com/fathimaali02/SemanticTextAnalyzer.git

Move into project:

cd SemanticTextAnalyzer

Create virtual environment:

python -m venv venv

Activate environment (Windows):

venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

---

## How To Run

Start backend server:

uvicorn api.main:app --reload

Open second terminal and run UI:

streamlit run ui.py

Open browser:

http://localhost:8501

---

## Usage

1. Index Documents tab – add reference text to the database.  
2. Check Text tab – analyze new text and view similarity results.

---

## Notes
This project demonstrates semantic similarity and NLP pipeline design.  
It provides similarity insights, not definitive plagiarism or AI-authorship verification.
