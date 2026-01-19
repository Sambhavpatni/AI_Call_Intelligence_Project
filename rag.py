
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

embeddings = OpenAIEmbeddings()
llm = ChatOpenAI(temperature=0)

def build_vector_store(text: str):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.create_documents([text])
    db = FAISS.from_documents(docs, embeddings)
    return db

def get_answer(db, query: str) -> str:
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())
    return qa.run(query)
