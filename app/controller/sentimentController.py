import sys
from flask import render_template, redirect, url_for, request, abort
from model.vader_sentiment_model import sentiment_sentence_scores

form_template = 'request_form.html'
result_template = 'request_response.html'
undefined_string = 'NO SENTENCE DEFINED'

def sentiment_form():
    return render_template(form_template)
    
def sentiment_sentence_check():
    sentence = request.args.get('sentence')
    
    # Empty sentence
    if sentence is None:
        sentence = undefined_string
        
    # Call Vader Sentiment Model
    scores = sentiment_sentence_scores(sentence)
    
    return render_template(result_template, result=scores["result"], positive=scores["positive"], neutral=scores["neutral"], negative=scores["negative"], sentence=sentence)