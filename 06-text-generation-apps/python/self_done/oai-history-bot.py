from openai import OpenAI
import os
import dotenv

# import dotenv
dotenv.load_dotenv()

# configure Azure OpenAI service client 
client =  OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
  organization= os.environ['OPENAI_ORG'],
  project= os.environ['OPENAI_PROJECT'],
)
deployment="gpt-3.5-turbo"

# add your completion code
persona = input("Tell me the historical character I want to be: ")
question = input("Ask your question about the historical character: ")
prompt = f"""
You are going to play as a historical character {persona}. 

Whenever certain questions are asked, you need to remember facts about the timelines and incidents and respond the accurate answer only. Don't create content yourself. If you don't know something, tell that you don't remember.

Provide answer for the question: {question}
"""
messages = [{"role": "user", "content": prompt}]  
# make completion
completion = client.chat.completions.create(model=deployment, messages=messages, temperature=0.6)

# print response
print(completion.choices[0].message.content)

#  very unhappy _____.

# Once upon a time there was a very unhappy mermaid.