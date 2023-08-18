import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')

temp = None

def set_temp(inItTemp):
    global temp
    temp = inItTemp

set_temp(1)

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temp, # this is the degree of randomness of the model's output
    )
    print("\nTemprature: " + str(temp) + "\n")
    return response.choices[0].message["content"]

# def get_location():

text = f"""


"""

prompt = f"""
You are a lawyer needing to scan a specific patent and its contents. Scan the selected patent delimited by tripple backticks,
and summarize the content into two main sections.

If the selected text says "Could not load description." Your response should simply be "No description to summarize."

Your two sections are: a section on the making of the invention, and a second section on the usage of said invention. 
Only include key details and other information that lawyers might find helpful.

On your first section, be sure to make a list detailing generalized steps that you would need to make such a product. Make sure to combine certain aspects
so you can keep your summary short and consice. This sections should have no more that 600 characters.

On the second section, go a little more in depth and extract all relevant data that might help describe how or why this product could be used.
This sections should have no more that 400 characters.

Remeber, You are only getting your information from this specific patent, do not include any information gathered outside of the selected text. 
And don't make any assumptions about the product if it is not otherwised declared in the text. 
```{text}```
"""

response = get_completion(prompt)

print(response)