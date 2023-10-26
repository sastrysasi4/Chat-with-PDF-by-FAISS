# Chat with your PDF (Faiss DB)

In this project, we will learn how to use FAISS, Langchain, and chat with your PDF document.

## Installation

These are the required packages

* Langchain
* OpenAI
* Pypdf
* Faiss-cpu
* Tiktoken

## Documentation


Here, we are going to see how to store the user data. (PDF data) into vector stores and use RetrievalQA to ask questions about that data.


We have taken a PDF file that contains Indian ART History information. Then we passed this text data into a text splitter with a chunk size of 1000 and chunk overlap of 30. and we took embeddings and model from OpenAI.


For the vector database, we chose FAISS, where we passed chunked text and OpenAI embeddings to change into a vector and store it. then using RetrievalQA to query the questions.


## Features

* Model -- OpenAI API
* Embeddings -- OpenAI API
* Document loader -- Pypdf loader
* Text splitter -- CharacterTextSplitter
* Vector DB -- FAISS
* QA chain -- qa_retriable


## Authors

- [@sasidhar](https://github.com/sastrysasi4)

