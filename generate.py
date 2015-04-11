import qrcode

def generate(string):
    return qrcode.make(string)
