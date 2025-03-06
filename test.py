import os
from dotenv import load_dotenv
from groq import Groq


# Load environment variables
load_dotenv()



# Initialize the Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

while True:
    user_question = input("\nAsk a question about the constitution of Kenya  (or type 'exit' to quit): ")
    
    if user_question.lower() == 'exit':
        break

    

    # Send the question with the most relevant section
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are an assistant that answers questions based on he constiuion of kenya."},
            {"role": "user", "content": f"Based on question provided \nQuestion: {user_question}"}
        ],
        model="llama-3.3-70b-versatile",
    )

    # Print the answer
    print("\nAnswer:", chat_completion.choices[0].message.content)
