import openai
from urllib.request import urlopen
from datetime import date

today = date.today().strftime("%Y/%m/%d")
html = urlopen(f"https://hehu-s.jje.hs.kr/jeju-s/food/{today}/lunch")
soup = BeautifulSoup(html,"html.parser")
lunch = soup.select(".ulType_food > li:nth-child(2) > di > dd")[0].text

openai.api_key = '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'

messages = []
messages.append({"role": "system", "content": "너는 제주과학고등학교 학생이다."})
messages.append({"role": "system", "content": "너의 이름은 제돌이다."})
messages.append({"role": "system", "content": "오늘의 식단은 "})
while True:
    question = input("me: ")
    if  question =="": break

    messages.append({"role": "user", "content": question})

    aiObj = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages
    )
    response=aiObj['choices'][0]['message']['content']#AI 답변 내용
    print(aiObj)

    print(f"AI: {response}")