import openai
from openai import AuthenticationError

# Replace "YOUR_API_KEY" with your actual OpenAI API key
api_key = "YOUR_API_KEY"

# RAG application entry point
# To run the Gradio UI, use: python ui/gradio_app.py
# The main_bk.py file can be used for testing OpenAI API connectivity or utility functions.

try:
    # Create a client instance by passing the API key directly
    client = openai.OpenAI(api_key=api_key)

    # Make a request for a chat completion
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Explain the concept of quantum entanglement simply."}
        ]
    )

    # Print the model's response
    print(response.choices[0].message.content)

except AuthenticationError:
    print("Authentication failed. Please check your API key.")
except Exception as e:
    print(f"An error occurred: {e}")
