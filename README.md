# Hawaii-Citation-Number-Finder
Finds the Citation number of any on-going tickets in the state of Hawaii. Can be used to locate lost citation numbers, or to check if someone has any on-going tickets.

# Technologies
Uses requests and BeautifulSoup4 frameworks to scrape and parse website. 

# How to use
Run the Main.py file and enter a name you want to check. If the name is found in the database, it will print the citation number.

# How it works
The Hawaii DMV handles their ticket cases individually through the URL extension. This program works by finding the latest ticket that has been issued and the most recent ticket that is still on-going. It then checks every ticket in that range and tries to find a matching name.