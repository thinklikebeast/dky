with open('my.txt') as f:
    data = f.read().splitlines()

if qrcode in data:
    print("ግባ")
else:
    print("አትግቡ")
