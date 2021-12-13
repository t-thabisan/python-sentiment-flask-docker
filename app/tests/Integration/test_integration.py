import pytest
import requests
from bs4 import BeautifulSoup


def get_request(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, "html5lib")


def get_response(sentence):
    soup = get_request('http://localhost:5000/')
    form = soup.find('form')
    action = form.get('action')
    sentence = sentence.strip()
    sentence_url = sentence.replace(' ', '+')
    return get_request('http://localhost:5000' + action + '?sentence=' + sentence_url)


def test_input_form():
    soup = get_request('http://localhost:5000/')
    form = soup.find('textarea')
    assert form.get('id') == 'sentence'
    assert form.get('name') == 'sentence'


def test_submit_button():
    soup = get_request('http://localhost:5000/')
    button = soup.find('button')
    assert button.get('type') == 'submit'


def test_get_sentiment():
    soup = get_response('I like good cookies')
    print(soup)
    sentiment = soup.find("p", {"id": "result"}).text
    assert sentiment == 'Positive'


def test_get_statistics():
    soup = get_response('I like good cookies')
    positive = soup.find(id="positive").p.text
    neutral = soup.find(id="neutral").p.text
    negative = soup.find(id="negative").p.text
    assert positive == '73.0%'
    assert neutral == '27.0%'
    assert negative == '0.0%'
