import pytest
from flask import url_for
from app import app
from controller.sentimentController import form_template, result_template, undefined_string

client = app.test_client()
    
def test_sentiment_request_return_form_template():
    rv = client.get('/sentiment/')
    assert rv.status == '200 OK'
    assert '<title>Sentiment Form</title>' in rv.data.decode('utf-8')
    
def test_sentiment_form_request_return_form_template():
    rv = client.get('/sentiment/form')
    assert rv.status == '200 OK'
    assert '<title>Sentiment Form</title>' in rv.data.decode('utf-8')
    
def test_sentiment_result_request_return_result_template_2():
    rv = client.get('/sentiment/result?sentence=TEST')
    assert rv.status == '200 OK'
    assert '<title>Sentiment Result</title>' in rv.data.decode('utf-8')