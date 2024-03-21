import requests
from twilio_conn import send_whatsapp_text, client

def ques_of_the_day():
    link="http://localhost:8000/success"
    res = requests.get(url=link)
    # print(res)

    data=res.json()
    status=res.status_code
    match status:
        case 200:
            ques = data['assignments'][0]['question']
        case 400:
            ques = data['error']['message']
        case _:
            return "Sorry!"
    return ques
        
ques = ques_of_the_day()
send_whatsapp_text(client,ques)


