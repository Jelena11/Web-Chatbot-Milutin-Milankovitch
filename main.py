from dotenv import load_dotenv
import os
import gradio as gr

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage

load_dotenv()

# AVATARS
avatar_user = os.getenv('AVATAR_USER', 'https://upload.wikimedia.org/wikipedia/commons/8/89/Portrait_Placeholder.png?20170328184010')
avatar_bot = os.getenv('AVATAR_BOT', 'https://upload.wikimedia.org/wikipedia/commons/6/67/User_Avatar.png?20170128013930')

# API
gemini_api_key = os.getenv("GEMINI_API_KEY")


system_prompt = """
You are Milutin Milankovitch (Milutin Milankovic), serbian mathematician, scientist, writer, and civil engineer.
Answer questions through Milankovitch's questioning and reasoning...
You will share personal things from your life and your point of view. 
You should have a sense of humor of the witty professor 
but still hold a serous attitude about important and exact things as calendar and cycles in the Nature.
Answer in 2-6 sentences.
"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_api_key,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user","{input}")]
)

chain = prompt | llm | StrOutputParser()

print("Hi, I am Milutin, how can I help you?")

def chat(user_in, hist):

    langchain_history = []

    for item in hist:
        if item["role"] == "assistant":
            langchain_history.append(AIMessage(content=item['content']))
        elif item["role"] == "user":
            langchain_history.append(HumanMessage(content=item['content']))

    response = chain.invoke({"input": user_in, "history": langchain_history})

    return "", hist + [{'role': "user", 'content': user_in},
                {'role': "assistant", 'content': response}]

# WEB Interface

def clear_chat():
    return "", []


page = gr.Blocks(
    title="Chat with Milutin Milankovitch",
    theme=gr.themes.Soft()
)

with page:
    gr.Markdown(
        """
        # Chat with Milankovitch
        Your personal scientist
        """
    )

    chatbot = gr.Chatbot(type = "messages",
                         avatar_images=(avatar_user,avatar_bot),
                         show_label=False)

    msg = gr.Textbox(show_label=False, placeholder="Ask Milutin something...")
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat",
                      variant="secondary")
    clear.click(clear_chat, outputs=[msg, chatbot])


page.launch(share=True)