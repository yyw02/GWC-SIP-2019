
#----------------------------------
import json
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# def numOfLetter(tw, letter):
# 	count = 0
# 	for l in tw:
# 		if l == letter or l.lower() == letter:
# 			#print(l)
# 			count += 1
# 	return count

tweetFile = open("tweets_small.json", "r")
tweetData = json.load(tweetFile)
# print(tweetData[0].keys())
tweetFile.close()
tweetList = []

# print(type(tweetData))
# print(type(tweetData[0]))
# print(tweetData[0]["favorite_count"])

# favoriteCount, numberofFavoriteCounts = 0, 0
# for i in range(0, len(tweetData)):
# 	if "favorite_count" in tweetData[i]:
# 		favoriteCount += tweetData[i]["favorite_count"]
# 		numberofFavoriteCounts += 1
# avg = favoriteCount / numberofFavoriteCounts
# # print(avg)
# #
# # # tweetData[0]["text"]
# # # for tweet in tweetData:
# # # 	if "text" in tweet:
# # # 		text = tweet["text"]
# # # 		for index in range(26):
# # # 			print(index)
# #
tweet_texts = []
for t in range(len(tweetData)):
		tweet_texts.append(tweetData[t]["text"])


def wordCount(stringOfTweet, string1):
	count = 0
	string1 = string1.lower()
	wordList = stringOfTweet.split(" ")
	for item in wordList:
		if item == string1:
			counter += 1
	return counter
	#Let's make a list of times a word occurs in a tweet
wordCountList = []
for item in tweet_texts:
	wordoccurence = wordCount(item, "the")
	wordCountList.append(wordoccurence)

# print(tweet_texts)

# tweetID = []
# for i in range(len(tweetData)):
# 	tweetList.append(tweetData [i]["id"])
# print(type(tweetID))
'''
polarityList =[]
for item in tweet_texts:
	blob1 = TextBlob(item)
	polar1 = blob1.polarity
	polarityList.append(polar1)
#print(polarityList)

tweetpol = {}
dictlist = []
for i in range(0,len(tweetData)):
	poldict = {}
	poldict["twitterid"] = tweetData[i]["id"]
	poldict["polarity"] = polarityList[i]
	poldict["tweet"] = tweet_texts[i]
	dictlist.append(poldict)
# print(dictlist)
'''

def countLetter(string, letter):
	counter = 0
	for let in string:
		if let.lower() == letter:
			counter += 1
		else:
			counter += 0
		# print(counter)
	return counter


tweetstring = ""
for tweet in tweet_texts:
	tweet = tweet + " "
	tweetstring += tweet
print(tweetstring)

countLetter(tweetstring, "a")
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(letters)

occurrences = []
for letter in letters:
	occurrences.append(countLetter(tweetstring, letter))
	# print(f"letter:{letter} occurrences:{countLetter(tweetstring, letter)}")
print(occurrences)
print(min(occurrences), max(occurrences))
plt.hist(occurrences)
plt.axis([min(occurrences), max(occurrences), 0, 10])
plt.show()
# plt.savefig("chart.png")


# wordcloud = WordCloud(height = 1000, width = 1000).generate(tweetstring)
# plt.figure(figsize = (10,10), facecolor = None)
# plt.imshow(wordcloud, interpolation = "bilinear")
# plt.axis("off")
# plt.show()
# plt.savefig('chart.png')
# #tweet_texts[]
#
# print(polarityList)
# print(min(polarityList), max(polarityList))
# plt.hist(polarityList)
# plt.axis([min(polarityList), max(polarityList), 0, 50])
#plt.show()
# plt.savefig("chart.png")

# tweetFile.close()
# print("Tweet id: ", tweetData[0]["id"])
# print("Tweet text: ", tweetData[0]["text"])
#
# for idx in range(len(tweetData)):
# 	print("Tweet text: " + tweetData[idx]["text"])
#
# for tweet in tweetData:
# 	print("Tweet text: " + tweet["text"])
