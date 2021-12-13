import pytest
from flask import url_for
from app import app
from controller.sentimentController import form_template, result_template, undefined_string

client = app.test_client()

def test_sentiment_form_bp_return_form_template():
    # Simulate a request context to use blueprint
    with app.test_request_context():
        url = url_for('sentiment_bp.sentiment_form')
    
    rv = client.get(url)
    assert rv.status == '200 OK'
    assert '<title>Sentiment Form</title>' in rv.data.decode('utf-8')
    
def test_sentiment_sentence_check_bp_return_result_template():
    # Simulate a request context to use blueprint
    with app.test_request_context():
        url = url_for('sentiment_bp.sentiment_sentence_check')
    
    rv = client.get(url)
    assert rv.status == '200 OK'
    assert '<title>Sentiment Result</title>' in rv.data.decode('utf-8')