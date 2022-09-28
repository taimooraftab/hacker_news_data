import requests
from bs4 import BeautifulSoup
import pprint

for i in range(1,3):
	res = requests.get(f'https://news.ycombinator.com/news?p={i}')
#print(res.text)

soup = BeautifulSoup(res.text,'html.parser')
#print(soup)
#print(soup.body)
#print(soup.body.contents)
# print(soup.find_all('div'))
# print(soup.find_all('a'))
# print(soup.title)

#only first item
# print(soup.a)
# print(soup.find('a'))
# print(soup.find(id= "score_32969957"))

# print(soup.select('a'))
# print(soup.select('.score'))
# print(soup.select('#score_32969957'))
# print(soup.select('.titlelink'))

# print(soup.select('.titlelink')[0])
# print(soup.select('.score')[0])

links = soup.select('.titlelink')
subtext = soup.select('.subtext')

# print(votes[0].get('score_32969957'))
# print(votes[0].get('id'))

def sort_stories_by_votes(hnlist):
	return sorted(hnlist, key = lambda k:k['votes'],reverse=True)

def create_custom_hn(links,subtext):
	hn = []
	for idx,item in enumerate(links):
		title = item.getText()
		href = item.get('href',None)
		vote = subtext[idx].select('.score')
		if len(vote):
			points = int(vote[0].getText().replace(' points',''))
			if points > 99:
				# hn.append(href)
				# hn.append(title)
				# print(points)
				hn.append({'title':title,'link':href,'votes':points})
		
	return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(links,subtext))
# print(create_custom_hn(links,subtext))
#create_custom_hn(links,subtext)