### When importing all functions from this file, we can use the following line
# from functions import *

import requests
from bs4 import BeautifulSoup

########################################################
#### scrape_content: scraping the contents in the url
#### input: url
#### output: content (type: str)
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
########################################################

def scrape_content(url):
    # Send a GET request to the URL
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers = headers)
    
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the webpage
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the desired information
        # Example: Extracting all paragraphs from the webpage
        paragraphs = soup.find_all('p')

        content = ""
        # Print or process the extracted information
        for paragraph in paragraphs:
            content += " " + paragraph.text

###### The below is to only return a shorter content. For the full content, use the commented commands above
#        for i in range(min(len(paragraphs), 10)):
### For the whole content:
#        for i in range(len(paragraphs)):
#            content += " " + paragraphs[i].text
        return content
    else:
        print("Failed to retrieve content. Status code:", response.status_code)
        return None
    

    
    
    
########################################################
#### scrape_google_news: scraping the titles, links, and dates of the first 20 articles from google (news tab) with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
#
# Note: The dates are in the form of "1 month ago", "3 hours ago"
########################################################

def scrape_google_news(query):
    # Construct the Google News URL with the query
    url = f"https://www.google.com/search?q={query}&tbm=nws"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the search result elements
    search_results = soup.find_all('div', class_='Gx5Zad fP1Qef xpd EtOod pkphOe')
    date_elements = soup.find_all('span', class_='r0bn4c rQMQod')


    # Extract the title and link of each search result
    scrap = []
    for i in range(min(len(search_results), 5)):
        title = search_results[i].find('a').text
        link = search_results[i].find('a')['href']
        #link = 'https://news.google.com' + link[1:]
        date = date_elements[i].text   
        scrap.append({'title': title, 'link': link, 'date': date})   
    return scrap



import requests
from bs4 import BeautifulSoup


########################################################
#### scrape_yahoo_news: scraping the titles, links, and dates of the first 20 articles from Yahoo (news tab) with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
#
# Note: The dates are in the form of "1 month ago", "3 hours ago"
########################################################

def scrape_yahoo_news(query):
    # Construct the Yahoo News URL with the query
    url = f"https://news.search.yahoo.com/search?p={query}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the search result elements
    search_results = soup.find_all('div', class_='NewsArticle')
    date_elements = soup.find_all('span', class_='fc-2nd s-time mr-8')

    # Extract the title and link of each search result
    scrap = []
    for i in range(min(len(search_results), 5)):
        title = search_results[i].find('h4').text
        link = search_results[i].find('a')['href']
        date = date_elements[i].text[2:]
        scrap.append({'title': title, 'link': link, 'date': date})   
    return scrap


########################################################
#### scrape_bing_news: scraping the titles, links, and dates of the first 20 articles from Microsoft Bing news with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
#
# Note: The dates are in the form of "1 month ago", "3 hours ago"
########################################################

def scrape_bing_news(query):
    # Construct the Yahoo News URL with the query
    url = f"https://www.bing.com/news/search?q={query}"
    print(url)
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the search result elements
    search_results = soup.find_all('div', class_='news-card')
    date_elements = soup.find_all('span', tabindex="0")
    
    # Extract the title and link of each search result
    scrap = []
    for i in range(min(len(search_results), 20)):
        title = search_results[i].find('a', class_ = 'title').text
        link = search_results[i].find('a', class_ = 'title')['href']
        date = date_elements[i]['aria-label']
        scrap.append({'title': title, 'link': link, 'date': date})   
    return scrap



########################################################
#### scrape_maritime_executive: scraping the titles, links, and dates of the first 20 articles from maritime executive with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
########################################################

def scrape_maritime_executive(query):
    # Construct the Yahoo News URL with the query
    url = f"https://www.maritime-executive.com/search?key={query}"
    print(url)
    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
    # Find all the search result elements
    search_results = soup.find_all('div', class_='desc body no-padding-xs')
    
    # Extract the title and link of each search result
    scrap = []
    for i in range(min(len(search_results), 20)):
        title = search_results[i].find('a', class_ = "font-firasans").text
        title = title.strip()
        link = search_results[i].find('a', class_ = "font-firasans")['href']
        date = 0
        scrap.append({'title': title, 'link': link, 'date': date})   
    return scrap



########################################################
#### Synonym and derived forms
#### input: word
#### output: the list of synonym and derived forms
########################################################







########################################################
#### Use one representative word for all synonyms / derived words
#### input: text, a list of word
#### output: cleaned text (using the first word in the list for all words in the list)
# This function requires re library
########################################################
import re 

def clean_word(text, group):
    if len(group) == 1:
        return text
    elif len(group) != 1:
        updated_text = text
        for i in range(1,len(group)):
            pattern = r'\b{}\b'.format(re.escape(group[i]))
            updated_text = re.sub(pattern, group[0], updated_text)
        return updated_text
    else:
        print("The word group is empty")
        return None
        






########################################################
#### Relevance Score
#### input: title and content of the article
#### output: the relevance score
########################################################







########################################################
#### Information Score functions
# These functions below require re library
########################################################

########################################################
#### find_imo: Find IMO (7-digit numbers)

def find_imo(content):    
    # regular expression for a 7-digit number (exactly 7-digit)
    imo_pattern = r'\b\d{7}\b'
    
    # find all 7-digit numbers in the content 
    imo_list = re.findall(imo_pattern, content)
    
    return imo_list

########################################################
#### find_mmsi: Find MMSI (9-digit numbers)

def find_mmsi(content):    
    # regular expression for a 9-digit number (exactly 9-digit)
    mmsi_pattern = r'\b\d{9}\b'
    
    # find all 9-digit numbers in the content 
    mmsi_list = re.findall(mmsi_pattern, content)
    
    return mmsi_list

########################################################
#### find names (company, people, etc)
# These functions require spaCy
########################################################

import spacy

########################################################
# people or company's names and nationality
def find_involved_parties_spacy(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    names = []

    for ent in doc.ents:
        if ent.label_ in ['PERSON', 'ORG', 'NORP']: # NORP is about nationality/religious/political group
            names.append(ent.text)
    return names

########################################################
# country's name / location
def find_location(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    locations = []

    for ent in doc.ents:
        if ent.label_ in ['LOC', 'GPE']: # location labels
            locations.append(ent.text)
    return locations


########################################################
# fishing species


