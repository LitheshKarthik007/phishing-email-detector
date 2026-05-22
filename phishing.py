import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer   #count vectorizer is the method which converts the text into data
from sklearn.naive_bayes import MultinomialNB
import streamlit as st


data = pd.read_csv("dataset.csv")

#print (data.shape)

data.drop_duplicates(inplace=True)  #used when using the same datasets


#print (data.shape)
#print (data.isnull().sum()) 
#gives the count of the null datasets

#spliting i/p ds vs o/p ds

mess = data['text']
cat =data['label']

(mess_train , mess_test , cat_train , cat_test) = train_test_split(mess,cat,test_size=0.2)


#converting the text data into the decimal/numerical  data for training

cv=CountVectorizer(stop_words='english')  #FILTERS THE STOP WORDS in english

f=cv.fit_transform(mess_train) #applying it to the dataset

#creating model

model=MultinomialNB()
model.fit(f,cat_train)  # f is the i/p ds converted into decimal form

#testing model

ft=cv.transform(mess_test)
#print(model.score(ft,cat_test))

#predict data

def predict(message):
    ip_message = cv.transform([message]).toarray()
    result=model.predict(ip_message)
    return result

#making it as a web app

st.header('Email phishing detection')
ip_mess=st.text_input('Enter Message Here')
if st.button('Validate'):
    res=predict(ip_mess)

    # dislaying the result

    if res[0] == "phishing":
        st.error("Phishing Email Detected")
    else:
        st.success("Safe Email")

