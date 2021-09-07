#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from urllib.parse import quote
pd.set_option('display.max_rows', None)


# In[2]:


df = pd.read_html('https://wikiwiki.jp/nijisanji/'
                  + quote('メンバーデータ一覧'))[-5]
df.columns = [_[1] for _ in df.columns.to_flat_index()]


# In[3]:


df = df[df['10万人']!='-']
df = df.sort_values('10万人')
df = df.loc[:,('チャンネル','10万人')]


# In[4]:


df_status = pd.read_csv(
    'https://raw.githubusercontent.com/'
    'eggplants/nijisanji-v23d-status/'
    'master/result.csv'
).rename(columns={'name': 'チャンネル'})


# In[5]:


df = df.merge(df_status)
df = df.reset_index(drop=True)
df.index.name = 'index'
df.index += 1
df


# In[6]:


df.to_csv('res.csv')
print(df.to_json(orient="records", indent=2, index=True)
      .replace("\\/", "-")
      .encode('latin-1')
      .decode('unicode_escape'),
      file=open("res.json","w"))
