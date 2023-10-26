import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.llms.openai import OpenAI
from langchain.vectorstores.faiss import FAISS
from langchain.chains import RetrievalQA

from dotenv import load_dotenv
load_dotenv()

if __name__ == '__main__':
    print("hi faiss")

    pdf_path = 'Indian_history.pdf'
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size = 1000,chunk_overlap = 30,separator='\n')
    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    llm = OpenAI()

    # creating and storing a vector DB
    # vectorstore = FAISS.from_documents(docs, embeddings)
    # vectorstore.save_local('faiss_db')

    # loading vector DB
    vectorstore = FAISS.load_local("faiss_db", embeddings)

    qa = RetrievalQA.from_chain_type(llm, 
                                     chain_type='stuff', 
                                     retriever = vectorstore.as_retriever())
    
    res = qa.run('describe Mauryan Art in a 50 words')
    print(res)