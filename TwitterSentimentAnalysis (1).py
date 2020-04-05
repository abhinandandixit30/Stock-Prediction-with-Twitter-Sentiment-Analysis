
# coding: utf-8

# In[65]:


import tweepy
from textblob import TextBlob


# In[66]:


def percentage(part,whole):
    return 100*float(part)/float(whole)


# In[67]:


consumer_key='Enter you key here'
consumer_secret='Enter you key here'
access_token='Enter you key here'
access_token_secret='Enter you key here'


# In[68]:


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
search_term=input("Enter the keyword you want to search: ")
times=int(input("Enter the number of tweets to be analyzed: "))
tweets=tweepy.Cursor(api.search, q=search_term, lang="English").items(times)
positive=0
negative=0
neutral=0
polarity=0
for tweet in tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    polarity+=analysis.sentiment.polarity
    if(analysis.sentiment.polarity==0):
        neutral+=1
    if(analysis.sentiment.polarity<0.00):
        negative+=1
    if(analysis.sentiment.polarity>0.00):
        positive+=1
positive=percentage(positive,times)
negative=percentage(negative,times)
neutral=percentage(neutral,times)
polarity=percentage(polarity,times)
positive=format(positive,'.2f')
negative=format(negative,'.2f')
neutral=format(neutral,'.2f')
print("Sentiments are "+search_term+" by analyzing "+str(times)+" tweets.")
if(polarity==0):
    print("Neutral")
elif(polarity>0):
    print("Positive")
else:
    print("Negative")
import matplotlib.pyplot as plt
labels=['positive['+str(positive)+'%]','negative['+str(negative)+'%]','neutral['+str(neutral)+'%]']
sizes=[positive,negative,neutral]
colors=['blue','red','gold']
patches,texts=plt.pie(sizes,colors=colors,startangle=90)
plt.legend(patches,labels,loc='best')
plt.title("Sentiments are "+search_term+" by analyzing "+str(times)+" tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()

