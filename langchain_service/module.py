from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from rich import print
load_dotenv()
model = "qwen/qwen3-32b"


def call_llm(LLMModel):
    llm = LLMModel(
        model=model,
        temperature=0.7,
        max_tokens=2000,
        timeout=None,
    )

    messages = [
        (
            "system",
            "You are a helpful assistant that translates English to French. Translate the user sentence.",
        ),
        ("human", "I love programming.")
    ]

    ai_msg = llm.invoke(messages)

    print(ai_msg)
    print("===========")
    print(ai_msg.usage_metadata)


# call_llm(ChatGroq)

embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
vector = embeddings.embed_query("hello, world!")
print(len(vector))