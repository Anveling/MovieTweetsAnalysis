import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn import svm
from sklearn import preprocessing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score



movie_list = []

df = pd.read_csv(os.path.join(os.getcwd(),"polairity_table.csv"),index_col=None)
df  = df.dropna()
df.columns = ["movie","sentiment","budget","collection"]
# df.columns = ["movie_name","budget","collection"]
# df["sentiment"] = preprocessing.MinMaxScaler().fit_transform(df["sentiment"].reshape(-1,1))
# df["sentiment"] = df["sentiment"]
df["ratio"] = df["budget"]/df["collection"]
df.to_csv(os.path.join(os.getcwd(),"res.csv"))
length  = len(df)
X_train,X_test,Y_train,Y_test = train_test_split(df["sentiment"].reshape(length,1),df["ratio"].reshape(length,1),test_size=0.2)

reg = linear_model.LinearRegression()
reg = svm.SVR(kernel="rbf", C = 1)
reg = RandomForestRegressor()

def flatten(val):
    return val[0]


reg.fit(X_train.reshape(len(X_train),1),Y_train.reshape(len(Y_train),1))
print(sorted(list(map(flatten,Y_train.tolist()))))
print(sorted(reg.predict(X_train).tolist()))
# print(reg.score(df["ratio"].reshape(length,1),df["sentiment"].reshape(length,1)))
# print(reg)
pred_train = reg.predict(X_train)
pred_test = reg.predict(X_test)

print(r2_score(Y_train,pred_train))

# print(pred_train)
# print(reg.coef_)

# print(pred_test,Y_test)

def track(a,b):
    if (a==b):
        return True
    else:
        return False




def return_df(ndarray):
    lis = ndarray.tolist()
    lis = list(map(flatten,lis))
    return pd.DataFrame(lis)

# Y_train = return_df(Y_train)

# print(Y_train)
# res = pd.DataFrame(pred_train)

# print(pd.DataFrame({"res":sorted(pred_train.tolist()),
              # "y_train":sorted(Y_train.tolist())}))
# print(res.head())
# df_res = pred_train+Y_test
# df_res = pd.DataFrame(df_res)
# df_res.to_csv(os.path.join(os.getcwd(),"res.csv"))
# print(df_res)

plt.scatter(df["ratio"].reshape(length,1),df["sentiment"].reshape(length,1))
#plt.xlabel()
#plt.ylabel()
plt.show()


#
# lr = LinearRegression()
#
# # print(train[])
#
# X_train,y_train = train["Polarity"], train["ratio"]
# lr.fit(X_train, y_train)
# print(lr.coef_)
#
# lr.predict(test["Polarity"])


# reg.fit(train[train.columns[1]],train["ratio"])



# df["ratio"] = df[:,2].apply(int)/df[:,3].apply(int)
# with open(os.path.join(os.getcwd(),"polairity_table.csv"),"r+") as polarity_table:
#
#     pd.DataFrame.from_csv()
#     for row in polarity_table.readlines():
#         # print(row)
#         row_list = [word.strip("\n") for word in row.split(",")]
#
#         try:
#         # print(list(row).extend([int(row[2]/int(row[1]))]))
#             row[2] = int(row[2])
#             row[3] = int(row[3])
#             row_list.extend([row[2]/row[3]])
#             movie_list.append(row_list)
#
#         except Exception as e:
#             print(e)
#         # print(movie_list)
#     polarity_table.close()
#
# print(movie_list)
