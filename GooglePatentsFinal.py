import re
import requests
import openai
import os
from bs4 import BeautifulSoup

# ChatGPT Code
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
openai.api_key  = os.getenv('OPENAI_API_KEY')

temp = None

def set_temp(inItTemp):
    global temp
    temp = inItTemp

# set_temp(1)

def get_completion(prompt, model="gpt-3.5-turbo", max_tokens=2000, temp=0.7):
    # Truncate the input prompt to max_tokens
    truncated_prompt = prompt[:max_tokens]
    messages = [{"role": "user", "content": truncated_prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temp, # this is the degree of randomness of the model's output
        max_tokens=max_tokens  # Set the maximum tokens for the response
    )
    return response.choices[0].message["content"]

# Sarb's Code
CLEANR = re.compile('<.*?>') 
def cleanhtml(raw_html):
    cleantext = re.sub(CLEANR, '', raw_html)
    cleantext = cleantext.replace('&hellip;', '')
    cleantext = cleantext.strip()
    cleantext = cleantext.capitalize()
    return cleantext

main_url = "https://patents.google.com/?q="
# Params: search term, input from user
params = input("What would you like to search?: ")

res = requests.get("https://patents.google.com/xhr/query?url=q%3D(" + params + ")&exp=&tags=")
main_data = res.json()
data = main_data['results']['cluster']

# Array to store patent dictionaries
patents = []

for i in range(len(data[0]['result'])):
    num = data[0]['result'][i]['patent']['publication_number']
    title = data[0]['result'][i]['patent']['title']
    title = cleanhtml(title)
    patent_url = "https://patents.google.com/patent/" + num
    
    patent_info = {# Patent Dictionaries to store information on patents
        'index': i + 1,
        'title': title,
        'number': num,
        'url': patent_url
    }
    
    patents.append(patent_info)

    print(patent_info['index'])
    print(patent_info['title'])
    print(patent_info['number'])
    print(patent_info['url'])
    print("\n")

chosen_file = input("Please select a patent by number: ")

# Now you can access the chosen patent's information from the `patents` array using the chosen index
chosen_index = int(chosen_file) - 1
chosen_patent = patents[chosen_index]

print("\nChosen Patent:")
print("Title:", chosen_patent['title'])
print("Number:", chosen_patent['number'])
print("URL:", chosen_patent['url'])
print()

# Amarjot's Code
URL = chosen_patent['url']
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Find the abstract section and extract its text
abstract_section = soup.find('div', class_='abstract')
if abstract_section:
    abstract = abstract_section.text.strip()
else:
    abstract = "Could not load abstract."

# Find all description paragraphs and extract their text
description_paragraphs = soup.find_all('div', class_='description-paragraph')
if description_paragraphs:
    description_text = '\n'.join([description.text.strip() for description in description_paragraphs])
else:
    description_text = "Could not load description."

# Find all claim texts and extract their text
claim_texts = soup.find_all('div', class_='claim-text')
if claim_texts:
    claim_text = '\n'.join([claim.text.strip() for claim in claim_texts])
else:
    claim_text = "Could not load claims."

print("Abstract:\n" + abstract + "\n")
# print("Description:\n" + description_text + "\n")
# print("Claims:\n" + claim_text + "\n")

prompt = f"""
You are a lawyer needing to scan a specific patent and its contents. Scan the selected patent delimited by triple backticks,
and summarize the content into two main paragraphs.

Your two sections are: a section on the making of the invention, and a second section on the usage of said invention. 
Only include key details and other information that lawyers might find helpful.

On your first section, be sure to make a list detailing generalized steps that you would need to make such a product. Make sure to combine certain aspects
so you can keep your summary short and consice. This sections should have no more that 600 characters.

On the second section, go a little more in depth and extract all relevant data that might help describe how or why this product could be used.
This sections should have no more that 400 characters.

```{description_text}```

"""

response = get_completion(prompt)
print("Summarized Description: (Please note...)\n\n" + str(response))

prompt = f"""
You are a lawyer tasked with analyzing a specific patent and its claims, provide a concise summary of the content based on the following sections:

1. Main Features in Independent Claims - Scan the selected patent's claims delimited by triple backticks, and identify the primary features outlined in the independent claims.
2. Notable Dependent Claims and Additional Features - Highlight any significant dependent claims and the additional features they introduce beyond the independent claims.
3. Definition of Scope of Protection - Explain how the claims define the scope of protection for the invention, including its boundaries and limitations.
4. Potential Variations or Embodiments Covered by the Claims - Discuss the potential variations or embodiments that are encompassed by the claims, showcasing the flexibility and breadth of the patent's coverage.

Separate each section with its title.

```{claim_text}```

"""

response = get_completion(prompt)
print("\nSummarized Claims: (Please note...)\n\n" + str(response))

# Roop's Code
download_Y_N = input("\nWould you like to download the full PDF? (Please Enter \"yes\" or \"no\"): ")
if(download_Y_N == "yes"):
    def download_pdf_from_google_patents(patent_number):
        # Construct the URL of the Google Patents page for the specified patent number
        url = f'https://patents.google.com/patent/{patent_number}/en'
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        # Find all anchor tags in the page
        anchor_tags = soup.find_all('a')
        # Search for the download link by looking for the 'href' attribute containing '.pdf'
        pdf_url = None
        for tag in anchor_tags:
            href = tag.get('href', '')
            if href.endswith('.pdf'):
                pdf_url = href
                break
        if pdf_url:
            # Send another HTTP GET request to the PDF URL to download the file
            pdf_response = requests.get(pdf_url)
            # Check if the response status is OK (200)
            if pdf_response.status_code == 200:
                # Save the PDF content to a file
                with open(f'{patent_number}.pdf', 'wb') as pdf_file:
                    pdf_file.write(pdf_response.content)
                print(f"PDF file for patent number {patent_number} downloaded successfully.")
            else:
                print(f"Failed to download PDF file for patent number {patent_number}.")
        else:
            print(f"PDF download link not found for patent number {patent_number}.")
    # Example usage: Download the PDF file for patent number US20180000123A1
    patent_number = chosen_patent['number']
    download_pdf_from_google_patents(patent_number)
