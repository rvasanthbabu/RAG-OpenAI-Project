import gradio as gr
from retrieval.rag_pipeline import RAGPipeline
import os

api_key = os.getenv('OPENAI_API_KEY', 'YOUR_API_KEY')
pipeline = RAGPipeline(api_key)

def ingest_file(file, file_type):
    pipeline.ingest_file(file.name, file_type)
    return f"File {file.name} ingested as {file_type}."

def query_rag(query):
    return pipeline.query(query)

with gr.Blocks() as demo:
    gr.Markdown("# RAG App: Upload a file and ask questions!")
    file_input = gr.File(label="Upload File")
    file_type = gr.Radio(["txt", "csv", "excel", "pdf"], label="File Type")
    ingest_btn = gr.Button("Ingest File")
    ingest_output = gr.Textbox(label="Ingestion Status")
    query_input = gr.Textbox(label="Your Question")
    query_btn = gr.Button("Ask")
    query_output = gr.Markdown(label="RAG Response")

    ingest_btn.click(ingest_file, inputs=[file_input, file_type], outputs=ingest_output)
    query_btn.click(query_rag, inputs=query_input, outputs=query_output)

demo.launch(inbrowser=True)
