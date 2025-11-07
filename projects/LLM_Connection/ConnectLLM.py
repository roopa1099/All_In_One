from langchain_ollama import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

model = "llama3:latest"

#for simple queries
llm = OllamaLLM(model=model,
    # You can optionally set model parameters here:
    temperature=0.8,
    num_ctx=4096 # Context window size)
)

prompt = "Write a short poem about the sea."

response = llm.invoke(prompt)

print("Response --------->", response)

llmOllamaChat = ChatOllama(model=model,  # You can optionally set model parameters here:
    temperature=0.8,
    num_ctx=4096 # Context window size)
)

messages = [SystemMessage(content="You are a Maths assistant."), HumanMessage(content="Write about world's toughest maths problems.")]

responseChat = llmOllamaChat.invoke(messages)

print("Chat Response --------->", responseChat)




