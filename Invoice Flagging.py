#!/usr/bin/env python
# coding: utf-8

#  **Flagging Vendor Invoices for Manual Review**
#  
#  ***Objective: Predict whether a vendor invoice should be flagged for manual approval based on abnormal cost, freight, or delivery patterns, in order to                reduce financial risk, improve operational efficiency, and prioritize human review it adds the most value.***
#            . Manual Invoice review is time-consuming and does not scale with transaction volume.
#             . Abnormal freight charges, pricing deviations, or delivery delays often indicate errors, disputes, or compliance risks.
#             . An automated flagging system enables finance teams to focus attention on high-risk invoices while allowing low-risk invoices to be          processed automatically.

# In[1]:


import sqlite3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


conn = sqlite3.connect("C:/Users/sumit/Downloads/inventory.db")


# In[3]:


tables = pd.read_sql_query("""SELECT name FROM sqlite_master WHERE type = 'table'; """, conn)
for table in tables['name']:
    print(f'Table name: {table}')
    df = pd.read_sql_query(f"select * from {table} limit 5", conn)
    display(df)


# In[4]:


purchase_agg_df = pd.read_sql_query("""
select
p.PONumber, 
count(distinct p.Brand) as total_brands,
sum(p.Quantity) as total_item_quantity,
sum(p.Dollars) as total_item_dollars,
avg(julianday(p.ReceivingDate) - julianday(p.PODate)) as avg_receiving_delay
from purchases p
group by p.PONumber
""",conn)


# In[5]:


purchase_agg_df.shape


# In[6]:


pd.read_sql_query("""
select
vi.Quantity as invoice_quantity,
vi.Dollars as invoice_dollars,
vi.Freight,
(julianday(vi.InvoiceDate) - julianday(vi.PODate)) AS day_po_to_invoice,
(julianday(vi.PayDate) - julianday(vi.InvoiceDate)) AS day_to_pay

from vendor_invoice vi 
""",conn)


# In[7]:


df_whole = pd.read_sql_query("""
WITH purchase_agg AS (
    SELECT
        p.PONumber, 
        count(distinct p.Brand) as total_brands,
        sum(p.Quantity) as total_item_quantity,
        sum(p.Dollars) as total_item_dollars,
        avg(julianday(p.ReceivingDate) - julianday(p.PODate)) as avg_receiving_delay
    from purchases p
    group by p.PONumber
)

SELECT
    vi.PONumber,
    vi.Quantity as invoice_quantity,
    vi.Dollars as invoice_dollars,
    vi.Freight,
    (julianday(vi.InvoiceDate) - julianday(vi.PODate)) AS day_po_to_invoice,
    (julianday(vi.PayDate) - julianday(vi.InvoiceDate)) AS day_to_pay,
    pa.total_brands,
    pa.total_item_quantity,
    pa.total_item_dollars,
    pa.avg_receiving_delay

FROM vendor_invoice vi
LEFT JOIN purchase_agg pa
    ON vi.PONumber = pa.PONumber
""",conn)


# In[8]:


df.isnull().sum()


# In[9]:


df_whole.dtypes


# In[10]:


def create_invoice_risk_label(row):
    # Invoice total mismatch with item_level total
    if(abs(row["invoice_dollars"] - row["total_item_dollars"]) > 5 ):
        return 1

    # Abnormally high receiving delay
    if row["avg_receiving_delay"] > 10:
        return 1
    return 0

df_whole["flag_invoice"] = df_whole.apply(create_invoice_risk_label, axis = 1)
df_whole["flag_invoice"].value_counts()


# In[11]:


df_whole['flag_invoice'].value_counts().plot(kind = 'bar')


# In[12]:


plt.figure(figsize =(20,10))
sns.heatmap(df_whole.iloc[:,1:-1].corr(),annot = True)
plt.show()


# In[13]:


flagged = df_whole[df_whole['flag_invoice'] == 1]
normal = df_whole[df_whole['flag_invoice'] == 0]


# In[14]:


significant_features = []
non_significant_features = []
results = []


# In[15]:


metrics = ['invoice_quantity','invoice_dollars','Freight',
           'day_po_to_invoice','day_to_pay','total_brands',            
           'total_item_quantity','total_item_dollars','avg_receiving_delay']


# In[16]:


from scipy.stats import ttest_ind
for metric in metrics:
    flagged_mean = flagged[metric].mean()
    normal_mean = normal[metric].mean()

    t_stat,p_value = ttest_ind(
        flagged[metric].dropna(),
        normal[metric].dropna(),
        equal_var = False
    )
    if p_value < 0.05:
        significant_features.append(metric)
        results.append({
        "metric": metric,
        "flagged_mean": flagged_mean.round(2),
        "normal_mean": normal_mean.round(2),
        "p_value": p_value.round(3)
    })
    else:
        non_significant_features.append(metric)
        print(metric)
        print({
        "metric": metric,
        "flagged_mean": flagged_mean.round(2),
        "normal_mean": normal_mean.round(2),
        "p_value": p_value.round(3) })



# In[17]:


non_significant_features


# In[18]:


significant_features


# In[19]:


results


# In[20]:


X = df_whole[['invoice_quantity','invoice_dollars',
              'total_brands','total_item_quantity',
              'day_po_to_invoice','total_item_dollars']]
y = df_whole['flag_invoice']


# In[21]:


X.describe().round()


# In[22]:


from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# In[23]:


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier


# In[24]:


model1 = LogisticRegression(random_state = 42)
model1.fit(X_train_scaled,y_train)

model2 = DecisionTreeClassifier(random_state = 42)
model2.fit(X_train_scaled,y_train)

model3 = RandomForestClassifier(random_state = 42)
model3.fit(X_train_scaled,y_train)


# In[25]:


from sklearn.metrics import accuracy_score, classification_report

def evaluate_model(model, X_test, y_test, model_name):
    # Predictions
    preds = model.predict(X_test)

    # Accuracy
    accuracy = accuracy_score(y_test, preds)

    print(f"\n{model_name} Performance:")
    print(f"Accuracy  : {accuracy:.2f}")
    print("Classification Report:")
    print(classification_report(y_test, preds))


# In[26]:


evaluate_model(model1, X_test_scaled, y_test, 'Logistic Regression')
evaluate_model(model2, X_test_scaled, y_test, 'Decision Tree Regression')
evaluate_model(model3, X_test_scaled, y_test, 'Random Forest Regression')


# In[27]:


model3.feature_importances_


# In[28]:


feature_importance = pd.DataFrame({
    "feature": X_train.columns,
    "importance": model3.feature_importances_
}).sort_values(by="importance", ascending = False)

feature_importance


# In[29]:


X = df_whole[['invoice_quantity','invoice_dollars',
              'total_item_quantity',
              'total_item_dollars']]
y = df_whole['flag_invoice']


# In[30]:


from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model3 = RandomForestClassifier(random_state = 42)
model3.fit(X_train_scaled,y_train)

evaluate_model(model3, X_test_scaled, y_test, 'Random Forest Regression')


# In[31]:


param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 4, 5, 6],
    "min_samples_split": [2, 3, 5],
    "min_samples_leaf": [1, 2, 5],
    "criterion": ['gini', 'entropy']
}


# In[32]:


from sklearn.metrics import make_scorer, f1_score
from sklearn.model_selection import GridSearchCV

rf = RandomForestClassifier(
    random_state=42,
    n_jobs=-1
)

param_grid = {
    "n_estimators": [100, 200, 300],
    "max_depth": [None, 4, 5, 6],
    "min_samples_split": [2, 3, 5],
    "min_samples_leaf": [1, 2, 5],
    "criterion": ["gini", "entropy"]
}

scorer = make_scorer(f1_score)

grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    scoring=scorer,
    cv=5,
    verbose=2,
    n_jobs=-1
)

grid_search.fit(X_train_scaled, y_train)

evaluate_model(grid_search, X_test_scaled, y_test, "Random Forest Classifier")


# In[33]:


from sklearn.metrics import confusion_matrix


# In[34]:


confusion_matrix(grid_search.predict(X_test_scaled),y_test)


# In[35]:


confusion_matrix(model3.predict(X_test_scaled),y_test)


# In[ ]:




