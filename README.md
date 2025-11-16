# Crimenet-RAG

![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white)

## 📝 Description

Dive deep into the world of crime data analysis with Crimenet-RAG, an innovative AI-powered Retrieval-Augmented Generation (RAG) system. Designed to empower investigators and analysts, Crimenet-RAG facilitates seamless querying and extraction of critical insights from complex crime datasets. Leveraging state-of-the-art NLP techniques, vector embeddings, and a robust Python-based backend, this system delivers intelligent, real-time support for crime investigation, helping you connect the dots and uncover hidden patterns within the data. Unlock the power of your crime data with Crimenet-RAG and transform the way you approach crime analysis.

## ✨ Features

- 🗄️ Database


## 🛠️ Tech Stack

- 🐍 Python


## 📦 Key Dependencies

```
fastapi: latest
uvicorn[standard]: latest
chromadb: latest
sentence-transformers: latest
transformers: latest
torch: latest
pydantic: latest
```

## 📁 Project Structure

```
.
├── data
│   ├── processed
│   │   ├── TC-119-2024.json
│   │   ├── cybercrime_case3.json
│   │   ├── fir1.json
│   │   └── fir2.json
│   └── raw
│       ├── cybercrime_case3.txt
│       ├── fir1.txt
│       ├── fir2.txt
│       └── theft_case.json
├── db
│   └── chroma
│       ├── chroma.sqlite3
│       └── f92d7351-f64a-4430-9bbe-ae0b0e5672ae
│           ├── data_level0.bin
│           ├── header.bin
│           ├── length.bin
│           └── link_lists.bin
├── requirements.txt
└── src
    ├── app.py
    ├── chroma_client.py
    ├── embed.py
    ├── ingest.py
    ├── rag_query.py
    └── utils.py
```

## 🛠️ Development Setup

### Python Setup
1. Install Python (v3.8+ recommended)
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`


## 👥 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/VennelaSara/Crimenet-RAG.git`
3. **Create** a new branch: `git checkout -b feature/your-feature`
4. **Commit** your changes: `git commit -am 'Add some feature'`
5. **Push** to your branch: `git push origin feature/your-feature`
6. **Open** a pull request

Please ensure your code follows the project's style guidelines and includes tests where applicable.


