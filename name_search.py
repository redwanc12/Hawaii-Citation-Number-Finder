from bs4 import BeautifulSoup
import requests

idNum = 15931

def check_blank(link):
	page = requests.get(link)
	soup = BeautifulSoup(page.text, 'html.parser')
	if('NO RESULTS' in soup.find('strong').text):
		return True
	return False

print(check_blank("https://etraffic.ehawaii.gov/etraffic/search/1DTI-19-0" + str(idNum)))