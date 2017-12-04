import pandas as pd
import sys
import got3 as got
import os
import datetime


def get_tweets(movie_name,start_date,end_date,max_tweets=10):
    print(movie_name,start_date,end_date)
    def printTweet(descr, t):
        print(descr)
        print("Username: %s" % t.username)
        print("Retweets: %d" % t.retweets)
        print("Text: %s" % t.text)
        print("Mentions: %s" % t.mentions)
        print("Hashtags: %s\n" % t.hashtags)

    #
    #     # Example 1 - Get tweets by username
    #     #tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees').setSince("2015-05-01").setUntil("2015-09-30").setMaxTweets(10000)
    #     #tweetCriteria = got.manager.TweetCriteria().setUsername('barackobama').setMaxTweets(1)
    # tweetCriteria = got.manager.TweetCriteria().setQuerySearch("avengers").setSince("2012-05-04").setUntil("2012-05-11").setMaxTweets(10).setLang("en")
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(movie_name).setSince(start_date).setUntil(end_date).setMaxTweets(max_tweets).setLang("en")
    # #tweetCriteria.setQuerySearch('atomic blonde')
    # #tweetCriteria.setSince("2017-07-28")
    # #tweetCriteria.setUntil("2017-08-07")
    # #tweetCriteria.setMaxTweets(1000)
    # #tweetCriteria.setLang("en")
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    if not tweets:
        print("No tweets found.You are BLOCKED!!!!")
        return
    #
    def change_text(text):
        return text
    for i in range(len(tweets)):
        d = {'index':tweets[i].date, 'text':tweets[i].text, 'id':tweets[i].id, 'username':tweets[i].username,
             'retweets':tweets[i].retweets, 'favorites':tweets[i].favorites,  'mentions':tweets[i].mentions,
             'hashtags':tweets[i].hashtags, 'geo':tweets[i].geo, 'permalink':tweets[i].permalink}
        if i == 0:
            df = pd.DataFrame.from_dict(d,orient='index').T
            df.apply(change_text,axis=1)
            df.index = df['index']
            df = df.drop('index', axis=1)
        else:
            df2 = pd.DataFrame.from_dict(d,orient='index').T
            df2.apply(change_text,axis=1)
            df2.index = df2['index']
            df2 = df2.drop('index', axis=1)
            df = df.append(df2)


    movie_name= "_".join([val.lower() for val in movie_name.split()])
    csv_location = os.path.join(os.getcwd(),"{0}.csv".format(movie_name))
    print(csv_location)
    df.to_csv(csv_location)
    return csv_location


def read_file(file_name):
    print(1)
    if not file_name:
        return
    with open(file_name,"r+") as movie_list:
        for line in movie_list.readlines()[2:]:
            print(line)
            line_list = line.split("\t")
            print(line_list)
            movie_name= line_list[1]
            try:
                start_date = datetime.datetime.strptime(line_list[2],"%m/%d/%Y")
                end_date = start_date + datetime.timedelta(weeks=2)
                start_date =  start_date.strftime("%Y-%m-%d")
                end_date = end_date.strftime("%Y-%m-%d")
                print("Processing tweets for the movie {0}".format(movie_name))
                get_tweets(movie_name=movie_name,start_date=start_date,end_date=end_date)

            except Exception as e:
                print(e)
                pass
            print("Processed the movie {0}".format(movie_name))

read_file("movies_lists.csv")
