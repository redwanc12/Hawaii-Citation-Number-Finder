from bs4 import BeautifulSoup
import requests
from name_search import find_max, id_to_link

name = input("enter a name ")

ID_START = 15900
ID_MAX = find_max(ID_START, 100)
idNum = ID_MAX - 70


while(idNum <= ID_MAX):

	page = requests.get(id_to_link(idNum))
	soup = BeautifulSoup(page.text, 'html.parser')

	for each in soup.find_all('dd'):
		if(('FIRST' not in each.text) and ('1D' not in each.text)):
			if(name in each.text):
				print('1DTI-19-0' + str(idNum))
				break

	idNum = idNum + 1

