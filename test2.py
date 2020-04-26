import GetOldTweets3 as got
#tweetCriteria = got.manager.TweetCriteria().setQuerySearch('i have the coronavirus').setMaxTweets(10)
import csv

usrs = [x.replace("@", "") for x in handles.split("\n")]
data = []
labels = []

tweetCriteria = got.manager.TweetCriteria().setQuerySearch("coronavirus").setSince("2020-03-20").setMaxTweets(10)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)

handles2 = set()

count = 0

for tweet in tweets:
    handles2.add(tweet.username)

for x in handles2:
    print(count/len(handles2))
    if len(x):
        tweetCriteria = got.manager.TweetCriteria().setUsername(x).setSince("2020-03-20").setMaxTweets(50)
        tweets = got.manager.TweetManager.getTweets(tweetCriteria)
        d = ""
        for tweet in tweets:
            d = d + " " + tweet.text
        if len(d):
            data.append(d)
            labels.append("not positive")
        count += 1;
                
wtr = csv.writer(open ('out.csv', 'w', encoding="utf-8"), delimiter=',', lineterminator='\n')
for i in range(len(data)):
    wtr.writerow([data[i], labels[i]])
