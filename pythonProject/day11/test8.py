import requests
import json

def main():
    resp = requests.get('http://api.tianapi.com/guonei/?key=77a87a2a75a8fe3139fbaff41712def8&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])

if __name__ == '__main__':
    main()

