import random
import string
import json
from jsondiff import diff

def random_id(length):
    number = '0123456789'
    alpha = 'abcdef'
    id = ''
    for i in range(0,length,2):
        id += random.choice(number)
        id += random.choice(alpha)
    return id

# "7e8ede84-2f05-4bf7-919c-02b403517035"
def get_random_correlationId():
    return random_id(8) + "-" + random_id(4) + "-" + random_id(4) + "-" + random_id(4) + "-" + random_id(12)

# "f1f4fcf5-fc9e-458a-b72f-b09c6e0e3ee0"
def get_random_userId():
    return random_id(8) + "-" + random_id(4) + "-" + random_id(4) + "-" + random_id(4) + "-" + random_id(12)