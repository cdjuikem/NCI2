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
    for i in range(min(len(search_results), 10)):
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
    url = f"https://ca.news.search.yahoo.com/search?p={query}"

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the search result elements
    search_results = soup.find_all('div', class_='NewsArticle')
    date_elements = soup.find_all('span', class_='fc-2nd s-time mr-8')

    # Extract the title and link of each search result
    scrap = []
    for i in range(min(len(search_results), 20)):
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
########################################################
########################################################
# Synonym (copied 240619)
# required libraries:
import nltk 
import requests
from nltk.stem import WordNetLemmatizer
from lemminflect import getInflection, getAllInflections
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.corpus import wordnet 


def get_synonyms(word):
    url = f"https://api.datamuse.com/words?rel_syn={word}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        synonyms = [entry['word'] for entry in data]
        return synonyms
    else:
        print("Error:", response.status_code)
        return []

########################################################
# related words (copied 240619)
def get_related_words(word, limit=60, topics=None):
    url = f"https://api.datamuse.com/words?ml={word}&max={limit}"
    
    if topics:
        url += f"&topics={topics}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        related_words = [entry['word'] for entry in data]
        return related_words
    else:
        print("Error:", response.status_code)
        return []
    
########################################################
# different forms of a verb

def verb_forms(word):
    # Get all inflections for the word as a verb
    inflections = getAllInflections(word, upos='VERB')
    
    # Check if the word or any of its inflections are in the list of verb inflections
    forms = list(inflections.values())
    form_set = set()
    for item in forms:
        form_set.add(item[0])
    if form_set == {}:
        return [word]
    else:
        return list(form_set)


########################################################
# A function to check if a word is in the list or not (copied 240619)    
def check_word_in_list(word, word_list):
    if word in word_list:
        return f"'{word}' is in the list."
    else:
        return f"'{word}' is not in the list."






########################################################
#### input: text, a list of word
#### output: text with only lower case and without special characters (hyphen will stay) 
# This function requires re library
########################################################
import re 

def text_preprocess(text):
    # Text to lowercase
    text = text.lower()
    # Remove special characters using regular expression (except for hyphen "-")
    cleaned_text = re.sub(r'[^-a-zA-Z0-9\s]', '', text)
    return cleaned_text


########################################################
#### Use one representative word for all synonyms / derived words
#### input: text, a list of word
#### output: cleaned text (using the first word in the list for all words in the list)
# This function requires re library
########################################################



########################################
# Forming word_group_list for verbs
def collect_verb(text):
    words = word_tokenize(text)
    pos_tags = pos_tag(words)
    verbs = [word for word, tag in pos_tags if tag.startswith('V')]
    return verbs

##########################################
# cleaning the text using the given list of verb forms
# clean_word is with a subroutine of rep_word_text, dealing with one group of words
# group: a list of different forms of a verb
def clean_word(text, group):
    if len(group) == 1:
        return text
    elif len(group) != 1:
        new_text = text
        for i in range(1,len(group)):
            pattern = r'\b{}\b'.format(re.escape(group[i]))
            new_text = re.sub(pattern, group[0], new_text)
        return new_text
    else:
        print("The word group is empty")
        return text

##########################################    
##### In text, change all verbs in representative form (mostly the basic form, but sometimes not)
misreport = ['misreport', 'misreports', 'misreporting', 'misreported']
underreport = ['underreport', 'underreports', 'underreporting', 'underreported']
unreport = ['unreport', 'unreports', 'unreporting', 'unreported']
pre_selected_word_list = [misreport, underreport, unreport]

def rep_word_text(text):
    global pre_selected_word_list
    
    new_text = text
    for word_form_list in pre_selected_word_list:
        if len(word_form_list) != 1:
            new_text = clean_word(new_text,word_form_list)
        else:
            new_text = text
            
    verb_list = collect_verb(new_text)
    if verb_list == []:
        return new_text
    else:
        lemmatizer = WordNetLemmatizer()
        for verb in verb_list:
            # Form the verb_form_list using the basic form of each word.
            verb_form_list = verb_forms(lemmatizer.lemmatize(verb.lower(), pos='v'))
            
            #if the verb form list is not trivial, clean the text with the list
            if len(verb_form_list) > 1:
                new_text = clean_word(new_text, verb_form_list)
            else:
                new_text = text
        return new_text

    


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
# people's names
def find_people(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    names = []

    for ent in doc.ents:
        if ent.label_ in ['PERSON']: # NORP is about nationality/religious/political group
            names.append(ent.text)
    return names

########################################################
# company's names
def find_company(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    names = []

    for ent in doc.ents:
        if ent.label_ in ['ORG']: # NORP is about nationality/religious/political group
            names.append(ent.text)
    return names


########################################################
# country's name / location
def find_location(text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(text)
    locations = []

    for ent in doc.ents:
        if ent.label_ in ['LOC', 'GPE', 'NORP']: # location labels
            locations.append(ent.text)
    return locations


########################################################
# fishing species


########################################################
# GRT


########################################################
# Information score
# This function requires numpy
import numpy as np

########################################################
# Information score
def weighted_info_score(text):
    #give weigths to each information:
    # IMO: 2
    # MMSI: 2
    # Involved parties or location: 1
    # The score will be out of 10
    score_list = [find_imo, find_mmsi, find_people, find_company, find_location]
    weight_vector = np.array([2, 2, 1, 1, 1])
    score = []
    for item in score_list:
        if len(item(text)) > 0:
            score.append(1)
        else:
            score.append(0)
    score = np.array(score)
    weighted_score = score * weight_vector
    #np.dot(score,weight_vector)

    return weighted_score



###################################################################
#

        
from datetime import datetime, date

def convert_day(date_string):
    # Define the format of the input date string
    date_format = "%m/%d/%Y"

    try:
        # Parse the input date string into a datetime object
        given_date = datetime.strptime(date_string, date_format).date()

        # Get today's date
        today = date.today()

        # Calculate the difference in days
        days_difference = (today - given_date).days

        return days_difference

    except ValueError:
        # Handle invalid date format or other errors
        return None





