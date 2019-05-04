from cult_network import *
import json
from process_cult_data import process


def fetch_classes():
    send_book = SendFindClass()
    resp = send_book.send_request()
    print(resp)
    return resp.json()

def book_clas(data):
    id, flag = process(data)
    if flag:
        send_book = SendBookClass(id)
        resp = send_book.send_request()
        return resp

if __name__ == '__main__':
    with open('data.json') as file:
       data = json.load(file)
    print(book_clas(data))
    #print(fetch_classes())