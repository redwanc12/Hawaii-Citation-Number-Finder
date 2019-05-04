from bs4 import BeautifulSoup
import requests

idNum = 15895
name = input("enter a name ")


while(idNum < 15905):

	page = requests.get("https://etraffic.ehawaii.gov/etraffic/search/1DTI-19-0" + str(idNum))
	soup = BeautifulSoup(page.text, 'html.parser')

	for each in soup.find_all('dd'):
		if(('FIRST' not in each.text) and ('1D' not in each.text)):
			if(each.text == name):
				print('1DTI-19-0' + str(idNum))
				break;

	idNum = idNum + 1;

