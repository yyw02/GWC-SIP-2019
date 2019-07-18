from wordcloud import WordCloud

wordcloud = WordCloud().generate(tweet_texts)

plt.imshow(wordcloud, interpolation = "bilinear")
plt.axis("off")
plt.show()
plt.savefig('chart.png')
#tweet_texts[]
tweetstring = ""
for tweet in tweet_texts:
	tweet = tweet + " "
	tweet_texts == tweet_texts
print(tweetstring)

#----------------------------------
import json
from textblob import TextBlob
import matplotlib.pyplot as plt

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
#print(tweetData[0].keys())
tweetFile.close()

# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.polarity)

polarityList =[]
# for item in listOfTweets:
# 	blob = TextBlob(item)
# 	polar1 = blob1.polarity
# 	polarityList.append(polar1)
#------------------------------------
# texts = [tweet_texts]
# polarity_list = [0.0, 0.9...]
# list = []
# #tweetsData[i]["id"]
# for i in range (len(tweetsData)):
# 	dictionary = {}
# 	dictionary["t_id"] = tweetsData[i]["id"]
# 	dictionary["polarity"] = polarity_list[i]
# 	dictionary["tweet"] = texts[i]
# 	list.append(dictionary)
	#------------------------


# '''
# In this program, we print out all the text data from our twitter JSON file.
# Please explain the comments to students as you code.
# '''

# We start by importing the JSON library to use for this project.
# Twitter data is stored in this format - this is the same format
# students learned for their Survey Project!
# import json
#
# # Next we want to open the JSON file. We tag this file as
# # "r" read only because we are only going to look at the data.
tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)

# print(type(tweetData))
# print(type(tweetData[0]))
# print(tweetData[0]["favorite_count"])

favoriteCount, numberofFavoriteCounts = 0, 0
for i in range(0, len(tweetData)):
	if "favorite_count" in tweetData[i]:
		favoriteCount += tweetData[i]["favorite_count"]
		numberofFavoriteCounts += 1
avg = favoriteCount / numberofFavoriteCounts
# print(avg)
#
# # tweetData[0]["text"]
# # for tweet in tweetData:
# # 	if "text" in tweet:
# # 		text = tweet["text"]
# # 		for index in range(26):
# # 			print(index)
#
tweet_texts = []
for t in range(0, len(tweetData)):
	if "text" in tweetData[t]:
		tweet_texts.append(tweetData[t]["text"])
# print(tweet_texts)
#
for i in range(0,len(tweet_texts)):
	blob1 = TextBlob(tweet_texts[i])
	polar1 = blob1.polarity
	polarityList.append(polar1)
# print(polarityList)
#
#
# We can close the file now that we have locally stored the data.
tweetFile.close()

# We then print the data of ONE tweet:
# the [0] denotes the *first* tweet object.
# # We access parts of the tweet using ["NameOfPart"].
# print("Tweet id: ", tweetData[0]["id"])
#
# # First ask students how they might print the text object:
# # Then show them the following code
# print("Tweet text: ", tweetData[0]["text"])


# First ask students how might they use loops
# to print the ["text"] of all the tweets:

# Show them the following two options:

# Explain how here, we're using index and
# counting the number of tweets in the tweetData
# using the python len() function.
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# # Explain here how Python lets you get objects
# # directly without having to use an index.
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])

# Encourage students to think about how there are
# often multiple solutions for each problem, and
# how each solution might have strenghts and drawbacks.
