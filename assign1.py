import requests
from bs4 import BeautifulSoup as bs
import sys

def get_body_title_link(response):
    sowp = bs(response.text,"html.parser")
    body = sowp.body.get_text() if sowp.body else ""
    cleanbody=""
    for char in body:
        if char.isalnum():
            cleanbody+=char
        else:
            cleanbody += " "
    title = ""
    if(sowp.title):
        title = sowp.title.string
    links = []
    for tag in sowp.find_all('a'):
        href = tag.get('href')
        if href:
            links.append(href)
    return cleanbody,title,links



