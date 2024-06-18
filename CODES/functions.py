import requests
from bs4 import BeautifulSoup

########################################################
#### CONTENT SCRAP
#### This function scrap the contents in the url
#### input: url
#### output: content (type: str)
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
########################################################

def scrape_content(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
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
#### GOOGLE NEWS
#### This function scrap the titles, links, and dates of the first 20 articles from google (news tab) with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
# It only gives info in the form of "1 month ago", "3 hours ago", not YYYY-MM-DD form
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
#### YAHOO NEWS 
#### This function scrap the titles, links, and dates of the first 20 articles from Yahoo (news tab) with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
#
# Note: The dates in Yahoo news is in different form.
# It only gives info in the form of "1 month ago", "3 hours ago", not YYYY-MM-DD form
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
#### BING NEWS
#### This function scrap the titles, links, and dates of the first 20 articles from Microsoft Bing news with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
#
# Note: The dates in Yahoo news is in different form.
# It only gives info in the form of "1 month ago", "3 hours ago", not YYYY-MM-DD form like Google
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
#### This function scrap the titles, links, and dates of the first 20 articles from Microsoft Bing news with the given query
#### input: query
#### output: the list of the title and link
####
#### required libraries:
# import requests
# from bs4 import BeautifulSoup
#
# Note: The dates in Yahoo news is in different form.
# It only gives info in the form of "1 month ago", "3 hours ago", not YYYY-MM-DD form like Google
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
#### Relevance Score
#### input: title and content of the article
#### output: the relevance score
########################################################







########################################################
#### Information Score
#### input: title and content of the article
#### output: the information score
########################################################