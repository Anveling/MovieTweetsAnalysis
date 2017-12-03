import pandas as pd
import sys
print (sys.version)
import got3 as got

def main():

    
    def printTweet(descr, t):
        print(descr)
        print("Username: %s" % t.username)
        print("Retweets: %d" % t.retweets)
        print("Text: %s" % t.text)
        print("Mentions: %s" % t.mentions)
        print("Hashtags: %s\n" % t.hashtags)

    # Example 1 - Get tweets by username
    #tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(10000)
    #tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch("avengers").setSince("2017-07-28").setUntil("2017-12-02").setMaxTweets(1000).setLang("en")
    #tweetCriteria.setQuerySearch('atomic blonde')
    #tweetCriteria.setSince("2017-07-28")
    #tweetCriteria.setUntil("2017-08-07")
    #tweetCriteria.setMaxTweets(1000)
    #tweetCriteria.setLang("en")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    print(len(tweets))

    def change_text(text):
        return text
    for i in range(len(tweets)):
        #print("in for")
        d = {'index':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,
             'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites,  'mentions':tweets[i].mentions,
             'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
        if i == 0:
            df = pd.DataFrame.from_dict(d,orient='index').T
            df.apply(change_text,axis=1)
            df.index = df['index']
            df = df.drop('index', axis=1)
            #print("there")
        else:
            df2 = pd.DataFrame.from_dict(d,orient='index').T
            df2.apply(change_text,axis=1)
            df2.index = df2['index']
            df2 = df2.drop('index', axis=1)
            df = df.append(df2)
            #print("Here")

    #with open('fateofthefurious.csv', 'a') as f:
        #df.to_csv(f, header=True)
    df.to_csv('test1.csv')
    #df.head()

    # Example 2 - Get tweets by query search
    #tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(1)
    #tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    #printTweet("### Example 2 - Get tweets by query search [europe refugees]", tweet)

    # Example 3 - Get tweets by username and bound dates
    #tweetCriteria = got.manager.TweetCriteria().setUsername("barackobama").setSince("2015-09-10").setUntil("2015-09-12").setMaxTweets(1)
    #tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

    #printTweet("### Example 3 - Get tweets by username and bound dates [barackobama, '2015-09-10', '2015-09-12']", tweet)

if __name__ == '__main__':
    main()
