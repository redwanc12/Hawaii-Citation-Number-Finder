from bs4 import BeautifulSoup
import requests

idNum = 15931
ID_MIN = 10000
ID_MAX = 99999


def id_to_link (id):
	#converts an id to a link for that id
	return("https://etraffic.ehawaii.gov/etraffic/search/1DTI-19-0" + str(id))


def blank(link):
	#checks ia link does not contain a valid ID.
	page = requests.get(link)
	soup = BeautifulSoup(page.text, 'html.parser')
	if('NO RESULTS' in soup.find('strong').text):
		return True
	return False

def find_max():
	if(blank(id_to_link(ID_MAX))):
		ID_MAX = ID_MAX/2
	else:
		print(ID_MAX)

find_max()


