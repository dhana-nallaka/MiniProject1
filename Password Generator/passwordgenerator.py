#importing random module
import random,string

#Strong Password:
# Eight Character
# One Upper Character
# One Lower Character
# One Special Character
#Random Password
random_password=random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.punctuation)+random.choice(string.digits)+random.choice(string.ascii_uppercase)+random.choice(string.ascii_lowercase)+random.choice(string.punctuation)+random.choice(string.digits)
print(random_password)
