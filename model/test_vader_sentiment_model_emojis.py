import pytest
from model.vader_sentiment_model import sentiment_sentence_scores

# high_ref_value
high_ref_value = 70
# low_ref_value
low_ref_value = 60

# EMOJI SENTENCES
basic_sentence_without_emoji = "Hello"
emoji_sentence_smile = "Hello :)"
emoji_sentence_frowning = "Hello :("

def test_smile_emoji_return_positive_score():
    emoji_sentence_smile_score = sentiment_sentence_scores(emoji_sentence_smile)
    
    assert emoji_sentence_smile_score['positive'] > high_ref_value
    assert emoji_sentence_smile_score['neutral'] > 0
    assert emoji_sentence_smile_score['negative'] == 0
    assert emoji_sentence_smile_score['result'] == 'Positive'
    
def test_negative_sentence_with_exclamation_increase_negativity():
    emoji_sentence_frowning_score = sentiment_sentence_scores(emoji_sentence_frowning)
   
    assert emoji_sentence_frowning_score['positive'] == 0
    assert emoji_sentence_frowning_score['neutral'] > 0
    assert emoji_sentence_frowning_score['negative'] > high_ref_value
    assert emoji_sentence_frowning_score['result'] == 'Negative'
    
def test_smile_emoji_increase_positivity():
    basic_sentence_without_emoji_score = sentiment_sentence_scores(basic_sentence_without_emoji)
    emoji_sentence_smile_score = sentiment_sentence_scores(emoji_sentence_smile)
   
    assert emoji_sentence_smile_score['positive'] > basic_sentence_without_emoji_score['positive']
    
def test_frowning_emoji_increase_negativity():
    basic_sentence_without_emoji_score = sentiment_sentence_scores(basic_sentence_without_emoji)
    emoji_sentence_frowning_score = sentiment_sentence_scores(emoji_sentence_frowning)
   
    assert emoji_sentence_frowning_score['negative'] > basic_sentence_without_emoji_score['negative']    
