from ecdsa import SigningKey, NIST256p
import re

def remove_whitespace(text):
    """Removes all whitespace from passed in string"""
    return re.sub(r"\s+", "", text, flags=re.UNICODE)

key = int(remove_whitespace("babedead babedead babedead babedead babedead babedead"), 16)
"""
This call will create hacked version of signing key (private key) which uses fixed value of 
random nonce and signing key. These argument are then passed manually having the same value
as the code running on MKL is using.
"""
sk = SigningKey.generate(secexp = key)

# random number spat out by LTC
rn = int(remove_whitespace("27298cb6 c92f7506 d1036836 3fbe9d65 f009758b 0da6a79f"), 16)
hash = int(remove_whitespace("d0826070 6affe7c8 673a1d6d af983fce 5b975a26 c5ad7633 584ecd48 956cb7e7"), 16)
signature = sk.sign_number(hash, k=rn)
print(signature)
