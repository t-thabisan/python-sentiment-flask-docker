# import SentimentIntensityAnalyzer class
# from vaderSentiment.vaderSentiment module.
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_sentence_scores(sentence):
 
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SentimentIntensityAnalyzer()
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(sentence)
    sentiment = ''
    
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        sentiment = 'Positive'
    elif sentiment_dict['compound'] <= - 0.05 :
        sentiment = 'Negative'
    else :
        sentiment = 'Neutral'

    scores = {
      "negative": round(sentiment_dict['neg']*100, 1),
      "neutral": round(sentiment_dict['neu']*100, 1),
      "positive": round(sentiment_dict['pos']*100, 1),
      "result": sentiment
    }
    
    return scores