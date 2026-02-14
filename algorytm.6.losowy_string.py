import random
import string

def losowy_napis(min_dl=10, max_dl=100):
    dl = random.randint(min_dl, max_dl)
    znaki = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(znaki) for _ in range(dl))

print(losowy_napis())