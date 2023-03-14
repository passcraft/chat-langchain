"""Load html from files, clean up, split, ingest into Weaviate."""
import pickle

from langchain.document_loaders import DirectoryLoader, PagedPDFSplitter, ReadTheDocsLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.faiss import FAISS


def ingest_docs():
    """Get documents from web pages."""
    loader = ReadTheDocsLoader("langchain.readthedocs.io/en/latest/", encoding='utf-8')
    raw_documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(raw_documents)
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    # Save vectorstore
    with open("vectorstore.pkl", "wb") as f:
        pickle.dump(vectorstore, f)


def ingest_pdfs():
    # ingest pdf files
    pdf_dir_loader = DirectoryLoader('./', glob="example_data/*.pdf", loader_cls=PagedPDFSplitter)
    raw_documents = pdf_dir_loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(raw_documents)
    # add OPENAI_API_KEY key to System ENV variable
    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    # Save vectorstore
    with open("vectorstore_all_pdf.pkl", "wb") as f:
        pickle.dump(vectorstore, f)
    print('trained on the pdf files located in <projectroot>/example_data/')


if __name__ == "__main__":
    ingest_pdfs()