import pandas as pd
from nltk.corpus import stopwords

stop = stopwords.words('english')
pd.read_csv("20th_century_women.csv", encoding="latin1")


df = pd.read_csv("20th_century_women.csv", encoding="latin1")

#df.columns = ['index','text','id','retweets','favorites','mentions','hashtags','geo','permalink']
#df['index'] = df['index'].str.lower().str.split()
#df.columns = ['text']
#print (stop)
# print(df["text"])
#print(df["text"].head(10))
# df['tweet_without_stopwords'] = df['text'].apply(lambda x: "".join([item for item in x.split() if item not in stop]))

# print(df['tweet_without_stopwords'] )
def remove_stop(item):
    if isinstance(item,str):
        word_list =[word.lower() for word in item.split(" ")]
        # print ("******"+" ".join([word for word in word_list if word not in stop]))
        return " ".join([word for word in word_list if word not in stop])
    else:
        return ""
    # return item if item not in stop else ""

df["text_new"] = df["text"].apply(remove_stop)
#print("*"*500)
#print(df["text_new"].head(100))


df.to_csv("test10out.csv")
