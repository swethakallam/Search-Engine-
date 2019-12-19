# Watch Search Engine

This is our try at building a search engine from scratch. 
The goal is create a search engine for users who are looking for genuine original watches as we collect data from genuine websites and show search results which ensures that the products displayed are 100% genuine.

# Scarping 
We scraped the data of all the watches from Macy’s and Kohl’s using Beautiful Soup and Selenium. We stored this data .csv format. 

# Data Cleaning 
Converted all the information to lower case, did Tokenization, and removed all special characters.

# Information Retrival 
We created an inverted index. Ranked the links retrieved using matching score(TF-IDF). 

# UI/UX
Our Search engine has 2 pages.
The first page is where the user searches about the watch he or she is looking for with keywords related to a brand and watch style.
The second page is where the search results are displayed. We created the UI using Flask and HTML.
