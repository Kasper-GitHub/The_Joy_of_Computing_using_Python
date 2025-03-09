import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')

file = "Conversation.xlsx"
xl = pd.ExcelFile(file)

dfs = xl.parse(xl.sheet_names[0])
dfs = list(dfs['Timeline'])
print(dfs)

sid = SentimentIntensityAnalyzer()
str = "UTC+05:30"
for data in dfs:
    a = data.find(str)
    if a == -1:
        ss = sid.polarity_scores(data)
        print(data)

        for k in ss:
            print(k,ss[k])