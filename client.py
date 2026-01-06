# from openai import OpenAI
 
# # pip install openai 
# # if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key="OPENAI_API_KEY",
# )

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a virtual assistant named nova skilled in general tasks like Alexa and Google Cloud"},
#     {"role": "user", "content": "what is coding"}
#   ]
# )

# print(completion.choices[0].message.content)


from openai import OpenAI

client = OpenAI(api_key="OPENAI_API_KEY")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
        {"role": "system", "content": "You are a virtual assistant named Nova"},
        {"role": "user", "content": "what is coding"}
    ]
)

print(response.output_text)
