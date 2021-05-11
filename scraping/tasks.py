import requets
import lxml
import json
from datetime import datetime
from bs4 import BeautifullSoup
from celery import shared_task
from .models import News


@shared_task
def web_scrap():
	article_list = []
	try:
		print('starting web scrap ...')
		r = requets.get('https://news.ycombinator.com/rss')
		soup = BeautifullSoup(r.connect, features ='xml')
		articles = soup.findall('item')

		for a in articles:
			title = a.find('link').text
			pulished_wrong = a.find('pubDate').text
			published = datetime.strptime(published_wrong, '%a, %d %b %Y %H:%M:%S %z')

		article = {
		'title':title,
		'link':link,
		'published':published,
		'source':'hackernewa rss'
		}

		article_list.append(article)
		print('finished scraping the article')


		return save_fuunction(article_list)

	except Exception as e:
		print('The scraping job failed. See exception:')
		print(e)


@shared_task(serializer='json')
def save_function(article_list):
	print('starting')
	new_count = 0

	for article in article_list:
		try:
			News.objects.create(
				title = article['title'],
				link = article['link'],
				published = article['published'],
				source = article['source']
			)
			new_count += 1
		
		except Exception as e:
		print('failed at latest_article is none')
		print(e)
		break
	return print('finished') 