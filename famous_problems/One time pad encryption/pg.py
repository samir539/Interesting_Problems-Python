from secrets import token_bytes

tb:bytes  = token_bytes(3)
print(tb)
print(int.from_bytes(tb, "big"))
h = "helloworld"
l = h.encode()
print(type(l))