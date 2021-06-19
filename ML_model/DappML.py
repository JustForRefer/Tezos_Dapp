#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


data = pd.read_csv("C:/Users/romas/Documents/aman_VIT/ML Dataset/Book1.csv")


# In[3]:


data.head()


# In[4]:


data.shape


# In[5]:


data.describe()


# In[6]:


data.shape


# In[7]:


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data['Country'] = le.fit_transform(data['Country'])


# In[8]:


data.columns


# In[9]:


data = data.drop(['State'],axis=1)


# In[10]:


data = data.drop(['City'],axis=1)


# In[11]:


data = data.drop(['Unnamed: 7'],axis=1)


# In[12]:


def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


# In[13]:


clean_dataset(data)


# In[14]:


data.head()


# In[15]:


X = data.drop(['classify'],axis=1)
Y = data['classify']


# In[16]:


from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)


# In[17]:


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[18]:


from sklearn.linear_model import LogisticRegression
lm = LogisticRegression()


# In[19]:


lm.fit(X_train,Y_train)


# In[20]:


predictions = lm.predict(X_test)
from sklearn import metrics
y_pred = lm.predict(X_test)
print('Mean Absolute Error:', metrics.mean_absolute_error(Y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(Y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(Y_test, y_pred)))


# In[21]:


print(y_pred)


# In[22]:


lm.score(X_test,Y_test)#final accuracy


# In[23]:


from sklearn.metrics import confusion_matrix,classification_report


# In[24]:


print(classification_report(y_pred,Y_test))


# In[25]:


print(confusion_matrix(y_pred,Y_test))


# In[29]:



import pickle


# In[32]:


pickle_final=open("lm.pkl","wb")


# In[33]:



pickle.dump(lm,pickle_final)


# In[34]:


pickle_final.close()


# In[ ]:




