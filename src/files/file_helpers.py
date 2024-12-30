import json 
from typing import Any 
import pickle 

def load_json_file(fn: str) -> dict: 
    with open(fn, 'r') as f: 
        res = json.load(f)
    return res

def save_json_file(data: dict, fn: str) -> None: 
    """Saves a dictionary as a json file"""
    with open(fn, 'w') as f: 
        json.dump(data, f)
    return fn


def load_pickle_file(fn: str) -> Any: 
    with open(fn, 'rb') as handle:
        data = pickle.load(handle)
    return data

def save_pickle_file(data, fn: str) -> None: 
    with open(fn, 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)