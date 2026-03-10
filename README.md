# Semantic Search Engine with Vector Database

This project implements a simple **Semantic Search Engine** to demonstrate the difference between **traditional keyword search** and **semantic (meaning-based) search**. The system stores document embeddings in a vector database and retrieves documents based on semantic similarity.

The goal of the project is to show how **semantic search can find relevant documents even when the exact keywords are not present**, unlike traditional keyword search which depends on exact word matches.

The system uses a **Django backend**, **PostgreSQL with pgvector for vector storage**, **Redis for caching**, and a **Streamlit UI** for comparing search results side-by-side. Embeddings are generated locally using an embedding model served through Ollama.

The project structure is organized as follows:

backend – Django backend API
ui – Streamlit user interface
data – sample documents dataset
requirements.txt – project dependencies
README.md – project documentation

---

## How the System Works

The system follows a simple pipeline:

1. Sample documents are stored in a CSV file.
2. A Django ingestion script reads each document.
3. The document text is converted into an embedding vector using an embedding model.
4. The embedding and document text are stored in PostgreSQL using the pgvector extension.
5. When a user enters a search query in the Streamlit UI:

   * Keyword search performs a text match in the database.
   * Semantic search converts the query into an embedding and finds the most similar document vectors.
6. Results from both searches are displayed side-by-side so users can easily compare which method works better.

---

## Technologies Used

Backend Framework: Django
Database: PostgreSQL
Vector Extension: pgvector
Caching: Redis
User Interface: Streamlit
Embedding Model: nomic-embed-text (via Ollama)

---

## Installation and Setup

Clone the repository and move into the project directory.

Install the required dependencies using:

pip install -r requirements.txt

Make sure PostgreSQL is installed and running. Create a database for the project.

After creating the database, enable the pgvector extension by running:

CREATE EXTENSION vector;

This allows PostgreSQL to store and query vector embeddings.

Install and run Redis for caching search results. Start Redis using:

redis-server

Install Ollama and pull the embedding model used in this project:

ollama pull nomic-embed-text

Then start the Ollama server:

ollama serve

---

## Loading Sample Documents

The project includes a sample dataset located in the **data folder**.
Documents are stored in a CSV file containing a title and content field.

To ingest the documents and generate embeddings, run the Django management command:

python manage.py ingest_docs

This command will:

• Read documents from the dataset
• Generate embeddings for each document
• Store the title, content, and embedding in PostgreSQL

Each embedding represents the semantic meaning of the document text.

---

## Running the Application

Start the Django backend server:

python manage.py runserver

This starts the API service that handles keyword and semantic search requests.

Next, run the Streamlit UI:

streamlit run app.py

The Streamlit interface will open in the browser and provide a search box where users can enter queries.

To simplify startup, a batch file named App_exe.bat is included in the repository.
This file starts the required services automatically.

Run the batch file by double-clicking it or executing:

App_exe.bat

---

## Search APIs

The backend exposes two main search endpoints.

Keyword Search Endpoint

/api/search/keyword?q=<query>

This endpoint performs a traditional keyword search using SQL text matching on the document title and content.

Semantic Search Endpoint

/api/search/semantic?q=<query>

This endpoint generates an embedding for the query and finds the most similar documents using vector similarity search in PostgreSQL.

The system returns the top 5 most relevant documents along with similarity scores.

---

