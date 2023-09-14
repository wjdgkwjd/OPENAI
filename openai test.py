import openai
openai.api_key = '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'

messages = []
messages.append({"role": "system", "content": "너의 이름은 제돌이고 제주과학고 1학년이야"})
while True:
    question = input("q: ")#내용 입력하면 저장
    if question =="": break

    messages.append({"role": "user", "content": question})

    aiObj = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages = messages)#채팅 내용 보내기

    response=aiObj['choices'][0]['message']['content']

    print(f"AI: {response}")

