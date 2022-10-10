import pyqrcode

s = "https://vk.com/audios405146197?section=all"

url = pyqrcode.create(s)

url.svg("filename", scale=8)
