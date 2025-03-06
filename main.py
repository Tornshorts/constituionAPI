import os
import gradio as gr
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def ask_constitution(question):
    if not question.strip():
        return "Please enter a question."

    try:
        # Send the question to Groq API
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an assistant that answers questions based on the Constitution of Kenya."},
                {"role": "user", "content": f"Question: {question}"}
            ],
            model="llama-3.3-70b-versatile",
        )
        
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Create a Gradio interface
interface = gr.Interface(
    fn=ask_constitution,
    inputs=gr.Textbox(placeholder="Ask a question about the Constitution of Kenya..."),
    outputs="text",
    title="Kenya Constitution Q&A",
    description="Ask questions related to the Constitution of Kenya, and get AI-generated answers.",
)

# Launch the Gradio app
if __name__ == "__main__":
    interface.launch()
