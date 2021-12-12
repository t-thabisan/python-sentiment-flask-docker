import pytest
from model.vader_sentiment_model import sentiment_sentence_scores

# high_ref_value
high_ref_value = 70
# low_ref_value
low_ref_value = 60

# NEGATIVE SENTENCES
negative_sentence_basic = "VADER is not smart, handsome, nor funny."
negative_sentence_exclamation = "VADER is not smart, handsome, nor funny!!!"
negative_sentence_bad_word = "It sucks."

def test_negative_sentence_basic_return_negative_score():
    negative_sentence_basic_score = sentiment_sentence_scores(negative_sentence_basic)
    
    assert negative_sentence_basic_score['positive'] == 0
    assert negative_sentence_basic_score['neutral'] > 0
    assert negative_sentence_basic_score['negative'] > low_ref_value
    assert negative_sentence_basic_score['result'] == 'Negative'
    
def test_negative_sentence_with_exclamation_increase_negativity():
    negative_sentence_basic_score = sentiment_sentence_scores(negative_sentence_basic)
    negative_sentence_exclamation_score = sentiment_sentence_scores(negative_sentence_exclamation)
   
    assert negative_sentence_exclamation_score['negative'] > negative_sentence_basic_score['negative']
    
def test_negative_sentence_with_bad_word_return_high_negative_score():
    negative_sentence_bad_word_score = sentiment_sentence_scores(negative_sentence_bad_word)
    
    assert negative_sentence_bad_word_score['positive'] == 0
    assert negative_sentence_bad_word_score['neutral'] > 0
    assert negative_sentence_bad_word_score['negative'] > high_ref_value
    assert negative_sentence_bad_word_score['result'] == 'Negative'