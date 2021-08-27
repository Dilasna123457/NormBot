from ef_norm import telethn as tbot

from telethon import TelegramClient, events
import json
import requests


def staat(qq):
  url = "https://api.telegram.org/bot"+BOTT+"/sendphoto"
  data = {
    "chat_id": str(qq),
    "photo": "https://telegra.ph/file/a23d1886930bd8d9cb0a9.jpg",
    "caption": "ශ්‍රී ලංකාවේ කොරෝනා තතු දැන ගන්න මාව භාවිතා කරන්න පුළුවන්. \n\nභාවිතා කළ හැකි විධාන 📌 \n \n • /covid - නවතම කොරෝනා තොරතුරු සදහා. \n • /about - මම ගැන දැන ගැනීම සදහා.",
    "parse_mode": "HTML",
    "reply_markup": {
        "inline_keyboard": [
            [
                {
                    "text": " Join Our Group",
                    "url": "https://t.me/slplatform"
                }
            ]
        ]
    }
}
  headers = {'Content-type': 'application/json'}
  r = requests.post(url, data=json.dumps(data), headers=headers)

def staa():
    r = requests.get('https://hpb.health.gov.lk/api/get-current-statistical')
    jsondata = json.loads(r.text)
    update_date_time    = str(jsondata['data']['update_date_time'])
    local_new_cases     = str(jsondata['data']['local_new_cases'])
    local_active_cases  = str(jsondata['data']['local_active_cases'])
    local_total_cases   = str(jsondata['data']['local_total_cases'])
    local_deaths        = str(jsondata['data']['local_deaths'])
    local_recovered     = str(jsondata['data']['local_recovered'])
    local_total_number_of_individuals_in_hospitals = str(jsondata['data']['local_total_number_of_individuals_in_hospitals'])
    global_new_cases    = str(jsondata['data']['global_new_cases'])
    global_total_cases  = str(jsondata['data']['global_total_cases'])
    global_deaths       = str(jsondata['data']['global_deaths'])
    global_new_deaths   = str(jsondata['data']['global_deaths'])
    global_recovered    = str(jsondata['data']['global_recovered'])

    textt = str(
                    '<b>වත්මත් තත්තවය</b>' + '\n' + '\n' + '<b>' +
                    update_date_time + ' ට යාවත්කාලීන කරන ලදී. </b>' + '\n' + '\n' +
                    '<b>🇱🇰 ශ්‍රී ලංකාවේ කොරෝනා තත්වය</b>' + '\n' + '\n'  +
                    '🤒 තහවුරු කරන ලද මුළු රෝගීන් ගණන = ' + '<code>' +
                    local_total_cases + '</code>' + '\n' +
                    '🤕 තවමත් ප්‍රතිකාර ලබන රෝගීන් ගණන = ' + '<code>' + local_active_cases + '</code>' +
                    '\n' + '😷 නව රෝගීන් ගණන = ' + '<code>' + local_new_cases + '</code>' +
                    '\n'
                    '🙂 මේ වන විට සුව වූ කොරෝන රෝගීන් ගණන = ' + '<code>' + local_recovered + '</code>' + 
                    '\n' + '⚰ මුළු මරණ සංඛ්‍යාව = ' + '<code>'  + local_deaths + '</code>' + '\n' +
                    '\n' + '<b>🌎 සමස්ත ලෝකයේ තත්වය</b>' + '\n' +
                    '\n' + '🤒 තහවුරු කරන ලද මුළු රෝගීන් ගණන = ' '<code>'  +
                    global_total_cases + '</code>' + '\n' + '😷 නව රෝගීන් ගණන = ' '<code>'  +
                    global_new_cases + '</code>' + '\n' + '⚰ මුළු මරණ සංඛ්‍යාව = ' '<code>'  +
                    global_deaths + '</code>' + '\n' + '🙂 මේ වන විට සුව වූ කොරෝනා රෝගීන් ගණන = ' '<code>'  +
                    global_recovered + '</code>' + '\n' + '\n' + '\n' +
                    '✅ සියලු තොරතුරු සෞඛ්‍ය ප්‍රවර්ධන කාර්‍යංශයෙන් ලබා ගත් තොරතුරු ය.' + '\n' +
                    '@efbots')
    return textt


@tbot.on(events.NewMessage(pattern='/covid19'))
async def corona(event):
    await event.respond(staa(),parse_mode='html')
    raise events.StopPropagation

def main():
    """Start the bot."""
    bot.run_until_disconnected()

if __name__ == '__main__':
    main()
    
_mod_name__ = " Covid19"

__help__ = """
 ~ /covid19 - corona
"""
