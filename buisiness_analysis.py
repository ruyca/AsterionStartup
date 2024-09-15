from dotenv import load_dotenv
from openai import OpenAI
import os
import json
import requests
import re

# Function to preprocess the string
def preprocess_string(input_str):
    # Remove Python code blocks, if they exist
    cleaned_str = re.sub(r'```python|```', '', input_str)
    
    # Remove any leading/trailing whitespace
    cleaned_str = cleaned_str.strip()
    
    # Return the cleaned string
    return cleaned_str


load_dotenv()
OPENAI_KEY = os.getenv("OPENAI_KEY")

def make_json(message: str) -> json: 
    message = message.replace("json", "").replace("\'\'\'", "")
    print(f"\n\n\n{message}", end="\n\n\n")
    json_data = json.dumps(message, indent=4)
    return json_data



def query_chatgpt(**kwargs):
    client = OpenAI(api_key=OPENAI_KEY)

    user_prompt = f"my company name is {kwargs['q1']} and what it does is \
        {kwargs['q2']}. My business solves the issue of {kwargs['q3']} \
        My main way of making money is by {kwargs['q4']} and my target audience \
        is {kwargs['q5']}."   

    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", 
         "content": "You are an advanced business stategist that gives concises answers. \
            Users will prompt you their business ideas and you must create a SWOT analysis \
            and finally make a strong conclussion on the business. The output must be in JSON with \
            the following structure: title: title, 'strenghts': [keys and values of strenghts] \
            'weakness': [keys and values of strenghts], 'opportunities': [keys and values of opportunities] \
            'threats': [keys and values of threats], 'conclussion': 'conclussion'. It is important \
            that the keys stay always the same (title, SWOT, conclussion). Ensure that the \
            response is identical to a python dictionary so it can later be converted to a JSON."},
        {"role": "user", "content": f"{user_prompt}"}
    ]
    )

    message = completion.choices[0].message.content

    print(f"\n\n{message}\n\n")

    return message

