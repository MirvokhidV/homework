import requests


req = requests.get(
    f"https://api.telegram.org/bot5724766211:AAFzpwZlPhmtr2px_weZ-Kr5dsXemfkJGL4/getUpdates"
).json()

for result in req['result']:
    try:
        if result['message']['text'].lower() == 'salom':
            requ = requests.get(
                f"https://api.telegram.org/bot5724766211:AAFzpwZlPhmtr2px_weZ-Kr5dsXemfkJGL4/sendMessage?chat_id={str(result['message']['chat']['id'])}&text=Salom"
            ).json()
            # print(result['message']['chat']['id'])
            # print('ho')
        if result['message']['text'].lower() != 'salom':
            r = requests.get(
                f"https://api.telegram.org/bot5724766211:AAFzpwZlPhmtr2px_weZ-Kr5dsXemfkJGL4/sendMessage?chat_id={str(result['message']['chat']['id'])}&text=<strong>sizning xabarlaringiz:</strong>\n\n{result['message']['text']}&parse_mode=HTML"
            ).json()
    except:
        pass
    # if result['message']['text'].lower() == 'salom':
    #     print('Cho tam mujik!')
