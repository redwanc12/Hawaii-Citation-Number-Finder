from bs4 import BeautifulSoup
import requests

#Lowest min value of ID.
ID_START = 15900


def id_to_link (id):
	#converts an id to a link for that id
	return("https://etraffic.ehawaii.gov/etraffic/search/1DTI-19-0" + str(id))


def blank(link):
	#checks ia link does not contain a valid ID.
	page = requests.get(link)
	soup = BeautifulSoup(page.text, 'html.parser')
	strongTag = soup.find('strong')
	if(strongTag is not None):
		if('NO RESULTS' in strongTag):
			return True
	return False

def find_max(min_id, incr):
	#finds the most recent ID number issued
	while(not blank(id_to_link(min_id))):
		min_id = min_id + incr
	min_id = min_id - incr
	if(blank(id_to_link(min_id+1))):
		return min_id
	else:
		return find_max(min_id, int(incr/2))

