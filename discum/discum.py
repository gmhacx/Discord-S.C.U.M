import requests

from messages.messages import Messages

class Client():
    # Define token, headers and create the request session.
    def __init__(self,token):
        self.token = token
        self.headers = {
        "Host": "discord.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36",
        "Accept": "*/*",
        "Accept-Language": "en-US",
        "Accept-Encoding": "gzip, deflate, br",
        "Authorization": self.token,
        "Connection": "keep-alive",
        "keep-alive" : "timeout=10, max=1000",
        "TE": "Trailers",
        "Pragma": "no-cache",
        "Cache-Control": "no-cache",
        "Referer": "https://discord.com/channels/@me",
        "Content-Type": "application/json"
        }
        self.s = requests.Session()
        self.s.headers.update(self.headers)
        
    #test token
    def connectionTest(self): #,proxy):
        url='https://discord.com/api/v6/users/@me/affinities/users'
        connection = self.s.get(url)
        if(connection.status_code == 200):
            print("Connected")
        else:
            print("Incorrect Token")

    #send text messages
    def sendMessage(self,channelID,message,tts=False):
        return Messages(self.headers).sendMessage(channelID, message, tts)

    #send files (local or link)
    def sendFile(self,channelID,filelocation,isurl=False,message=""):
        return Messages(self.headers).sendFile(channelID,filelocation,isurl,message)
