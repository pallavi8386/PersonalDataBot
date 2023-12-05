    #!/usr/bin/env python
# coding: utf-8

import openai
import os
import streamlit as st
from secret_key import api_key

openai.api_key = api_key

# Personal data bot
with open('data.txt', 'r') as file:
    content = file.read()

def mydatachatbot(user_input):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that only answers questions strictly based on the given text."},
            {"role": "user", "content": f"Do not provide answers from general context. If the context does not have answer say I don't know.The text for you to strictly base your answers on is as follows: {content}"},
            {"role": "user", "content": user_input},
        ],
        temperature=0,  # Make output more focused and deterministic
    )

    # Check if the answer is valid
    if "I don't know" in response.choices[0].message['content']:
        return "This data is not available on this site. Please ask a relevant question."
    else:
        return response.choices[0].message['content']
    
#         messages=[
#             {'role': "system", 'content': "You're a helpful assistant"},
#             {'role': "user", 'content': "Please answer my queries according to the given context \nContext:{}".format(str(content))},
#             {'role': "assistant", 'content': "Okay, sure!"},
#             {'role': "user", 'content': user_input}
#         ]
#     )
#     return response['choices'][0]['message']['content']

def main():
    counter = 0
    st.title("My Personal Data ChatBot")
    st.write("Ask your question related to Paris: ")

    while True:
        user_input = st.text_input("You: ", key=f'user_input_{counter}')

        if user_input:
            generated_output = mydatachatbot(user_input)
            st.write(f"{generated_output}")

            counter += 1
        else:
            break
            
if __name__ == "__main__":
    main()