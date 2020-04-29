import pprint
import requests  

## word cloud
secret = secret_number
url = 'https://newsapi.org/v2/everything?'
parameters = {
    'q': 'economy', # query phrase
    'pageSize': 20,  # maximum is 100
    'apiKey': secret # your own API key
}
response = requests.get(url, params=parameters)

response_json = response.json()
#pprint.pprint(response_json)

#for i in response_json['articles']:
#    print(i['title'])

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Create an empty string
text_combined = ''
# Loop through all the headlines and add them to 'text_combined' 
for i in response_json['articles']:
    text_combined += i['title'] + ' ' # add a space after every headline, so the first and last words are not glued together
wordcloud = WordCloud(max_font_size=40).generate(text_combined)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
