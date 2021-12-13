import pytest
import requests
from bs4 import BeautifulSoup


def get_request():
    response = requests.get('http://localhost:5000/')
    return BeautifulSoup(response.text, "html5lib")


def test_input_form():
    soup = get_request()
    form = soup.find('textarea')
    assert 'id="sentence"' in str(form)
    assert 'name="sentence"' in str(form)


def test_submit_button():
    soup = get_request()
    button = soup.find('button')
    assert 'type="submit"' in str(button)
