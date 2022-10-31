my_bytes = 'a123n'.encode('ascii')

print(my_bytes) # 👉️ <class 'bytes'>

print(len(b'\x86G5\xcb')) 
print(bytes("snsns",encoding="utf-8"))
print(str(bytes("snsns",encoding="utf-8"),encoding="utf-8"))
print()