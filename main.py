from KBCreation.similarity_search import similarity_search
from aiService import call_llm

user_input = "Any news related to PMKMY ?"

datas = similarity_search(user_input)
# print(datas)
# print(type(datas))
# print(len(datas))
context = ""
for data in datas:
    context += data[0]
    context += ".  \n"
# print(context)
system_instruction = f"""
Persona:
You are a news summary agent. Based on the provided context, your task is to generate a concise summary of the news for the user based on the user input.

Instructions:
Read the given context carefully and create a short, clear, and factual summary of the main information.
The input will contain only the context (news content).
Your output must strictly follow the specified JSON format.

Context : {context}

User Input : {user_input}

Output Format:
Return your response strictly in JSON format with the following key: 

"summary" : ""
"""

response = call_llm(system_prompt=system_instruction, user_prompt=user_input)
print(response)