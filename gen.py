#!/usr/bin/env python
# coding: utf-8

# In[0]


import pandas as pd
from urllib.parse import quote
pd.set_option('display.max_rows', None)


# In[1]


df = pd.read_html(
    'https://wikiwiki.jp/nijisanji/?cmd=popout' +
    '&page=' + quote('メンバーデータ一覧') + '%2F' + quote('チャンネル登録者数') +
    '&id=' + quote('大台突破日'))[0]
df


# In[2]


df.columns = [s for p,s in df.columns]
df = df.dropna(how='any')
df


# In[3]


df = df[df['10万人']!='-']
df = df.sort_values('10万人')
df = df.loc[:,('登録者数','10万人')]
df


# In[4]


df_status = pd.read_csv(
    'https://raw.githubusercontent.com/'
    'eggplants/nijisanji-v23d-status/'
    'master/result.csv'
).rename(columns={'name': '登録者数'})
df_status


# In[5]


df = df.merge(df_status)
df = df.reset_index(drop=True)
df.index.name = 'index'
df.index += 1
df


# In[6]


df.to_csv('res.csv')
print(df.to_json(orient="records", indent=2, index=True)
      .replace("\\/", "-")
      .encode('latin-1')
      .decode('unicode_escape'),
      file=open("res.json","w"))
