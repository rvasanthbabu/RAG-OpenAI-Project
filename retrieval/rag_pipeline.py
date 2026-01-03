from ingestion.txt_ingestor import ingest_txt
from ingestion.csv_ingestor import ingest_csv
from ingestion.excel_ingestor import ingest_excel
from ingestion.pdf_ingestor import ingest_pdf
from chunking.chunker import chunk_text
from embedding.embedder import get_openai_embedding
from vector_store.faiss_store import FAISSVectorStore
import openai
import os

class RAGPipeline:
    def __init__(self, api_key, embedding_dim=1536):
        self.api_key = api_key
        self.vector_store = FAISSVectorStore(embedding_dim)
    def ingest_file(self, file_path, file_type):
        if file_type == 'txt':
            text = ingest_txt(file_path)
        elif file_type == 'csv':
            text = ingest_csv(file_path)
        elif file_type == 'excel':
            text = ingest_excel(file_path)
        elif file_type == 'pdf':
            text = ingest_pdf(file_path)
        else:
            raise ValueError('Unsupported file type')
        chunks = chunk_text(text)
        embeddings = [get_openai_embedding(chunk, self.api_key) for chunk in chunks]
        self.vector_store.add(embeddings, chunks)
    def query(self, query_text):
        query_embedding = get_openai_embedding(query_text, self.api_key)
        retrieved_chunks = self.vector_store.search(query_embedding)
        context = '\n'.join(retrieved_chunks)
        client = openai.OpenAI(api_key=self.api_key)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer the user's question. Format your answer in clear paragraphs and use markdown for lists or code if needed. Always return your answer in markdown format."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {query_text}"}
            ]
        )
        # Return markdown-formatted answer as a single string
        return str(response.choices[0].message.content).strip()
