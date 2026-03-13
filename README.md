# 🔎 Web-Based Search Engine using Inverted Index

A cutting-edge **web-based search engine** built with **C programming**,
utilizing **Swish-e** and **Nutch** concepts to implement an **inverted
index** for efficient information retrieval.

This project demonstrates how large amounts of textual data can be
indexed and searched quickly using a low-level, high-performance backend
combined with a simple web interface.

------------------------------------------------------------------------

## 🚀 Features

-   ⚡ **Fast Search Engine**
    -   Implements an **inverted index** for rapid lookup.
-   📚 **Efficient Document Indexing**
    -   Organizes text data for quick retrieval.
-   🔎 **Relevant Search Results**
    -   Ranking-based search results.
-   🌐 **Web Interface**
    -   Simple UI for submitting queries and viewing results.
-   ⚙️ **High Performance Backend**
    -   Core search engine implemented in **C**.

------------------------------------------------------------------------

## 🧠 How It Works

The system works through several main stages:

1.  **Document Processing**
    -   Documents are processed and tokenized.
    -   Stopwords are removed.
2.  **Inverted Index Generation**
    -   Words are mapped to the documents containing them.
3.  **Index Storage**
    -   The generated index is stored in the `index-db`.
4.  **Search Query Processing**
    -   User enters a search query via the web interface.
5.  **Ranking & Retrieval**
    -   The system finds matching documents and ranks them.

------------------------------------------------------------------------

## 🏗️ Project Structure

    SearchEngine/
    │
    ├── data/                # Dataset used for indexing
    ├── index-db/            # Generated inverted index database
    ├── templates/           # HTML templates for UI
    │
    ├── app.py               # Python web server (Flask)
    ├── search.php           # Web search handler
    ├── search.js            # Frontend search logic
    │
    ├── index-db.c           # Index generation module
    ├── index-tools.c        # Index utility functions
    ├── query-tools.c        # Query processing utilities
    ├── query-with-doclen.c  # Query processing with document length
    │
    ├── util.c               # Helper functions
    ├── util.h               # Utility headers
    │
    ├── define.h             # Project constants
    ├── Makefile             # Build automation
    │
    ├── indexdb.exe          # Index builder executable
    └── querydb.exe          # Query processor executable

------------------------------------------------------------------------

## ⚙️ Requirements

-   GCC Compiler
-   Python 3
-   Flask
-   Make
-   Web Browser

------------------------------------------------------------------------

## 🔧 Installation

Clone the repository:

``` bash
git clone https://github.com/yourusername/SearchEngine.git
cd SearchEngine
```

Compile the C modules:

``` bash
make
```

Install Python dependencies:

``` bash
pip install flask
```

------------------------------------------------------------------------

## ▶️ Running the Search Engine

### 1️⃣ Generate the Inverted Index

``` bash
./indexdb.exe
```

This will process the dataset and generate the index in `index-db/`.

### 2️⃣ Start the Web Server

``` bash
python app.py
```

### 3️⃣ Open in Browser

    http://127.0.0.1:5000

You will see the search interface where users can enter queries and
retrieve ranked results.

------------------------------------------------------------------------

## 🖥️ Interface

The web interface allows users to:

-   Enter search queries
-   Select ranking options
-   View search results instantly

------------------------------------------------------------------------

## 📊 Technologies Used

-   **C Programming Language**
-   **Python (Flask)**
-   **Swish-e Concepts**
-   **Apache Nutch Concepts**
-   **HTML / JavaScript / PHP**
-   **Inverted Index Data Structure**

------------------------------------------------------------------------

## 📚 Learning Objectives

This project demonstrates:

-   Search engine fundamentals
-   Inverted indexing
-   Information retrieval techniques
-   Ranking algorithms
-   Integrating C backend with web interfaces

------------------------------------------------------------------------

## 📌 Future Improvements

-   Implement TF-IDF ranking
-   Add multi-threaded indexing
-   Improve UI/UX
-   Support larger datasets
-   Add query suggestions

------------------------------------------------------------------------

