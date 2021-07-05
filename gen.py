import pandas as pd

URL = 'https://wikiwiki.jp/nijisanji/' + \
    '%E3%83%A1%E3%83%B3%E3%83%90%E3%83%BC%E3%83%87%E3%83%BC%E3%82%BF' + \
    '%E4%B8%80%E8%A6%A7'

df = pd.read_html(URL)[-5]
df.columns = [_[1] for _ in df.columns.to_flat_index()]
df = df[df['10万人'] !=
        '-'].sort_values('10万人').loc[:, ('チャンネル', '10万人')]
df = df.reset_index(drop=True)
df.index.name = 'index'
df.index += 1
df.to_csv('res.csv')
