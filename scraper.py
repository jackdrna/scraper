import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# ALGORITHM:
# 1. Get HTML information from API jobs site with chosen keywords
# 2. Create an array with all of the job links found
# 3. In a loop, scrape each job posting for the job details
# 4. Now within the Job details, save all bullet points (<li>)

url = 'https://www.linkedin.com/jobs/search/?currentJobId=4199504245&geoId=90000084&keywords=engineer%20intern&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true'

# Send a GET request to the website
response = requests.get(url)

# Check if successful (status code 200)
if response.status_code == 200:
    print("Got success!")
else:
    print("Got failed :(")

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

