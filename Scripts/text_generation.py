import openai
from config import Key_OpenAi

openai.api_key = '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'

def TextGenertion():
    message ="привет"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= message,
        temperature=0.9,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You"]
        )
    print(response['choices'][0]['text'])

