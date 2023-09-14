import openai
import json
openai.api_key = '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'

'너의 이름은 재돌이야. 제주과학고 1학년, 나이는 16세'
#text로 학습
with open('aitext.txt', 'r',encoding='utf-8') as f:
    aitext = f.read()                #utf-8 한글
aitext = aitext.replace("\n", "").replace("\r", "")
print(aitext)

#json으로 학습
with open('aitraining.json', 'r',encoding='utf-8') as f:
    messages = json.load(f)
messages.append({"role": "user", "content": aitext})
print(messages)
while True:
    question = input("me: ")
    if  question =="": break

    messages.append({"role": "user", "content": question})

    aiObj = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages
    )

    response=aiObj['choices'][0]['message']['content']

    print(f"AI: {response}")