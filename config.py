__all__ = ['FindClass', 'BookClass']

headers = {'accept': 'application/json',
 'datatype': 'json',
 'appversion': '7.47',
 'osname': 'android',
 'accept-encoding': '',
 'codepushversion': '130',
 'deviceid': 'fb6c338b45178cff',
 'st': 'CFAPP:39958c2a-a936-4a26-8876-3357cf79662b',
 'at': 'CFAPP:2d2d9ce5-f71a-458b-8500-1a00cb07be61',
 'lat': 'null',
 'lon': 'null',
 'user-agent': 'okhttp/3.12.1'}


class FindClass:
    def __init__(self):
        self.headers = headers.copy()
        #self.url='https://www.cure.fit/api/cult/classes/v2?productType=FITNESS'
        self.url = 'http://localhost:8080'
        self.type='GET'


class BookClass(FindClass):
    def __init__(self):
        super().__init__()
        #self.url= 'https://www.cure.fit/api/cult/class/{}/book'
        self.url = 'http://localhost:8080/{}'
        self.headers['content-type'] = 'application/json'
        self.type = 'POST'
        self.payload = {
            "advertiserId": "1556000658319-96450588272129600"
        }

class CultAttr:
    def __init__(self):
        self.day = -1
        self.center = [100]
        self.time = ['07:00:00','08:00:00']
        self.classes = [56, 46, 8]
