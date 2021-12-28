from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    tb:bytes = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original:str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy: int = random_key(len(original_bytes))
    original_key: int = int.from_bytes(original_bytes, "big")
    encrypted: int = original_key ^ dummy
    return dummy, encrypted


def decrypt(encrypted_data:int, dummy:int) -> str:
    decrypted_int = encrypted_data ^ dummy
    decrypted_bytes: bytes = decrypted_int.to_bytes((decrypted_int.bit_length()+ 7 // 8), "big")
    return decrypted_bytes.decode()

if __name__ == "__main__":
    key1, key2 = encrypt("Hello World")
    result: str = decrypt(key1,key2)
    print(key1, key2)
    print(result)

