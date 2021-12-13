import pytest
from model.vader_sentiment_model import sentiment_sentence_scores

# high_ref_value
high_ref_value = 70
low_ref_value = 60

# POSITIVE SENTENCES
positive_sentence_basic = "VADER is smart, handsome, and funny."   
positive_sentence_exclamation = "VADER is smart, handsome, and funny!!!"   
positive_sentence_exclamation_uppercase = "VADER is VERY SMART, handsome, and FUNNY!!!"   

def test_positive_sentence_basic_return_positive_scores():
    positive_sentence_basic_score = sentiment_sentence_scores(positive_sentence_basic)
    
    assert positive_sentence_basic_score['positive'] > low_ref_value
    assert positive_sentence_basic_score['neutral'] > 0
    assert positive_sentence_basic_score['negative'] == 0
    assert positive_sentence_basic_score['result'] == 'Positive'
    
def test_positive_sentence_exclamation_return_positive_scores():
    positive_sentence_exclamation_score = sentiment_sentence_scores(positive_sentence_exclamation)
    
    assert positive_sentence_exclamation_score['positive'] > high_ref_value
    assert positive_sentence_exclamation_score['neutral'] > 0
    assert positive_sentence_exclamation_score['negative'] == 0    
    assert positive_sentence_exclamation_score['result'] == 'Positive'

def test_positive_sentence_with_exclamation_increase_positivity():
    positive_sentence_basic_score = sentiment_sentence_scores(positive_sentence_basic)
    positive_sentence_exclamation_score = sentiment_sentence_scores(positive_sentence_exclamation)

    assert positive_sentence_exclamation_score['positive'] > positive_sentence_basic_score['positive']