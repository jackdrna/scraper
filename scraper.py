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

base_url = 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords='
keywords = 'Engineer%2FIntern'
location = 'San%20FFrancisco'
start = 0

url = base_url + keywords + '&location=' + location + '&start=' + str(start)

# 'https://www.linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?
# keywords=Engineer%2FIntern&location=San%20FFrancisco&start=25'

# Send a GET request to the website
response = requests.get(url)

# Check if successful (status code 200)
if response.status_code == 200:
    print("Got success!")
else:
    print("Got failed :(")

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())

