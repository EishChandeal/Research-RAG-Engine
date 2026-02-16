# Research RAG Engine

A high-performance Retrieval-Augmented Generation (RAG) system designed to handle the structural complexity of academic research paper

## Key features

- High-Fidelity Ingestion: Uses Grobid (CRF-driven) to parse two-column academic PDFs into structured TEI XML, identifying titles, abstracts, and section headers.

- Structural Awareness: The pipeline distinguishes between "Introduction," "Methodology," and "Results" to improve retrieval context.

- Environment-Ready: Managed with Poetry for robust dependency resolution and reproducible builds.

## Getting started

**Prerequisites**

Docker & Docker Compose
Python 3.x & Poetry

**1. Start the Ingestion Server**
The engine relies on a running Grobid instance to process PDFs structurally.

```bash
docker compose up -d
```

_Verify it is running at http://localhost:8070_

**2. Setup Environment**
This project uses Poetry to manage dependencies.

```Bash
# To ensure that virtual environment is build on the folder itself
poetry config virtualenvs.in-project true

# Install dependencies
poetry install

# Activate virtual environment
Invoke-Expression(poetry env activate)
```

**3. Basic Usage (Phase 1)**
Run the experiment script to verify high-fidelity extraction from your sample PDFs:

```bash
python experiments/sandbox.py
```

## 📂 Project Structure

```
research-rag-engine/
├── docker/                 # Docker configurations
├── experiments/            # Sandbox and prototypes
├── src/                    # Production source code
│   └── ingestion/          # PDF processing logic
├── tests/                  # Unit tests
├── pyproject.toml          # Poetry dependency file
└── docker-compose.yml      # Service orchestration
```

### Note:

To keep the requirements.text file up to date cleanly (just for possible use in the future by docker)

```bash
poetry export -f requirements.txt --without-hashes > requirements.txt
```
