import os
import pickle
import json

from tools.encrypt_decrypt import decrypt


def get_key(val, in_env_var=False):
    if in_env_var:
        p = os.environ[val]
    else:
        p = val
    with open("key.bin", "rb") as fh:
        data = pickle.loads(fh.read())
    key = decrypt(data, p)
    return key
