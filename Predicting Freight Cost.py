#!/usr/bin/env python
# coding: utf-8

# In[134]:


import numpy as np
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt


# In[135]:


db_path = r"C:\Users\sumit\Downloads\inventory.db"
conn = sqlite3.connect(db_path)
print("Database connected successfully!")


# In[136]:


conn = sqlite3.connect(db_path)
tables = pd.read_sql_query("""SELECT name FROM sqlite_master WHERE type = 'table'; """, conn)
tables


# In[137]:


for table in tables['name']:
    print(f'Table name: {table}')
    df = pd.read_sql_query(f"select * from {table} limit 5", conn)
    display(df)


# In[138]:


vendor_df = pd.read_sql_query("select * from vendor_invoice", conn)
vendor_df.head()


# In[139]:


vendor_df[['Quantity','Freight','Dollars']].corr()


# In[158]:


# Relationship between quantity, Dollars and Freight
plt.figure(figsize = (4,2))
sns.heatmap(vendor_df[['Quantity','Dollars','Freight']].corr(),annot = True)
plt.show();

plt.scatter(vendor_df['Quantity'],vendor_df['Freight'],color = '#f57a55')
plt.scatter(vendor_df['Dollars'],vendor_df['Freight'],color = '#7f1e5a')
plt.legend(['Quantity','Dolaars'])
plt.show()


# In[141]:


vendor_df['freight_per_unit'] = vendor_df['Freight']/vendor_df['Quantity']


# In[142]:


low_quantity = vendor_df['Quantity'].quantile(0.25)
high_quantity = vendor_df['Quantity'].quantile(0.75)


# In[143]:


high_quantity


# In[144]:


low_quantity


# In[145]:


vendor_df.loc[vendor_df['Quantity'] < low_quantity,'freight_per_unit'].mean()


# In[146]:


vendor_df.loc[vendor_df['Quantity'] < high_quantity,'freight_per_unit'].mean()


# In[147]:


X = vendor_df[['Dollars']]
y = vendor_df['Freight']


# In[148]:


vendor_df.describe().round()


# In[149]:


from sklearn.model_selection import train_test_split


# In[150]:


X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 42)


# In[151]:


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# In[152]:


model1 = LinearRegression()
model1.fit(X_train,y_train)

model2 = DecisionTreeRegressor(max_depth = 4,random_state = 42)
model2.fit(X_train,y_train)

model3 = RandomForestRegressor(max_depth = 4,random_state = 42)
model3.fit(X_train,y_train)



# In[153]:


def evaluate_model(model,X_test,y_test,model_name):
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_test, preds)* 100

    print(f"\n{model_name} Performance:")
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R2   : {r2:.2f}%")


# In[154]:


evaluate_model(model1, X_test, y_test , 'Linear Regression')
evaluate_model(model2, X_test, y_test , 'Decision Tree Regression')
evaluate_model(model3, X_test, y_test , 'Random Forest Regression')


# In[155]:


plt.scatter(X_test,y_test)
plt.plot(X_test,model1.predict(X_test),color = 'red')


# In[156]:


input_data = {"Dollars": [18500,9000]}
df = pd.DataFrame(input_data)


# In[157]:


model1.predict(df)

