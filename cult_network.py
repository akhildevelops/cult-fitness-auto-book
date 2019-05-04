from requests import Request, Session
import config
import json

__all__=['SendBookClass', 'SendFindClass']

config_FindClass = config.FindClass()
config_BookClass = config.BookClass()

http_proxy  = "http://localhost:8888"
https_proxy = "https://localhost:8888"
ftp_proxy   = "ftp://10.10.1.10:3128"
#cafile = 'FiddlerRoot.cer'
proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }

#print(config_FindClass.headers)

class CultSend:
    def __init__(self,url=None, headers=None, type=None, payload = None):
        self.url = url
        self.headers = headers
        self.type = type
        self.payload = payload


    def __prepare_session(self):
        s = Session()
        #params_arr = [self.type, self.url, self.headers, self.payload]
        req = self.__utility_params()
        print(req.url)
        prepped = req.prepare()
        #prepped = self.__utility_headers(prepped)
        return s, prepped

    def send_request(self):
        s, prepped = self.__prepare_session()
        print(prepped.headers)
        return s.send(prepped,proxies=proxyDict,verify=False)

    def __utility_headers(self, prepped):
        #print(prepped.headers)
        if self.type == 'GET':
            del prepped.headers['Accept-Encoding']
        return prepped

    def __utility_params(self):
        if self.type == 'GET':
            return Request(self.type, self.url,headers=self.headers)
        else:
            print(self.payload)
            return Request(self.type,self.url,data=json.dumps(self.payload), headers=self.headers)

class SendFindClass(CultSend):
    def __init__(self):
        url = config_FindClass.url
        headers = config_FindClass.headers
        type = config_FindClass.type
        super().__init__(url, headers, type)


class SendBookClass(CultSend):
    def __init__(self, book_id):
        url =config_BookClass.url.format(book_id)
        headers = config_BookClass.headers
        type = config_BookClass.type
        payload = config_BookClass.payload
        super().__init__(url, headers, type, payload)
