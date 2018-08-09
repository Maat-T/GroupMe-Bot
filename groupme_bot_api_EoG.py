import requests
import time
import calendar
import datetime

request_params = {'token': 'user token'}

while True:
    today = datetime.date.today()
    if today.day == calendar.monthrange(today.year, today.month):
        to_send = 'pay up chumps, price is 5 dollas.'
        post_params = { 'bot_id' : 'bot id', 'text': to_send }
        requests.post('https://api.groupme.com/v3/bots/post', params = post_params)
    time.sleep(14400) #4 hours


    """
#website for creating bot.  http://sweb.uky.edu/~jtba252/index.php/2017/09/13/how-to-write-a-groupme-bot-using-python/

#this is to react to messeges in the group.
    response = requests.get('https://api.groupme.com/v3/groups/group_id/messages', params = request_params)
#this helps program not crash
    if (response.status_code == 200):
        response_messages = requests.get('https://api.groupme.com/v3/groups/42582276/messages', params = request_params).json()['response']['messages']
        
        for message in response_messages:
            request_params['since_id'] = message['id']
            break 

    
    time.sleep(5)
"""