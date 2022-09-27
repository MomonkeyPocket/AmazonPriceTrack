from bs4 import BeautifulSoup
import requests, time

TARGET_URL = "https://www.amazon.co.jp/dp/B07JK7FZH2/"
LINE_TOKEN = "あなたのLineNotifyトークン"
LINE_NOTIFY_API = "https://notify-api.line.me/api/notify"


def amazon_tracking_price():
    amazon_page = requests.get(TARGET_URL)
    soup = BeautifulSoup(amazon_page.content, "html.parser")
    # print(soup)

    title = soup.find(id="productTitle").get_text()
    price = soup.find("span", class_="a-size-base").get_text()
    converted_price = price[1:6].replace(",", "")
    int_price = int(converted_price)
    # print(title)
    # print(price)
    # print(converted_price)

    if(int_price < 1500):
        send_line_notify()

def send_line_notify():
    print("lineに通知がいきました")
    headers = {"Authorization": f"Bearer {LINE_TOKEN}"}
    data = {"message": "今がお買い時です！{}".format(TARGET_URL)}
    requests.post(LINE_NOTIFY_API, headers=headers, data=data)

while(True):
    print("トラッキングしました")
    time.sleep(60 * 60)
    amazon_tracking_price()