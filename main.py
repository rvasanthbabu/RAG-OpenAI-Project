import os
from ui.gradio_app import demo

def main():
    # Optionally set the OpenAI API key from environment or config
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print('Warning: OPENAI_API_KEY not set. Using default key from gradio_app.')
    print('Starting Gradio RAG application...')
    demo.launch()

if __name__ == "__main__":
    main()


#install dependencies : pip install -r requirements.txt

# To run the Gradio UI, use: python main.py