# Custom Chatbot using Langchain and Flask

This project is a custom chatbot that extracts data from a specific URL, creates embeddings, stores them in a vector store, and provides a RESTful API using Flask to handle conversations.

## Features

- **Data Extraction**: Extracts course data from [Brainlox Technical Courses](https://brainlox.com/courses/category/technical) using Langchain's URL loader.
- **Embeddings**: Generates embeddings using the `sentence-transformers/all-MiniLM-L6-v2` model.
- **Vector Store**: Stores embeddings in a FAISS vector store for efficient similarity search.
- **Flask API**: Provides a RESTful API to interact with the chatbot.

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. **Libraries**
   pip install langchain flask requests beautifulsoup4 sentence-transformers faiss-cpu
