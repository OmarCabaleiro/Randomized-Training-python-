import random

movements = ["loaded carry", "squat", "hinge", "superior pull", \
             "horizontal pull", "inferior pull", "superior push", \
             "horizontal push", "inferior push", "gait", "jump", "crawl", \
             "rotation", "trunk extension", "trunk flexion", \
             "lift from ground", "throwing"]

##while True:
##    session = input("Choose: /n 1. 2. 3. c. r.:")
##    if session == "1":
##        print(random.choice(movements))
##    if session == "2":
##        print(random.choices(movements, k=2))
##    if session == "3":
##        print(random.choices(movements, k=3))
##    if session == "c":
##        print(random.choices(movements, k=random.randint(4, 10)))
##    if session == "r":
##        print(random.choices(movements, k=random.randint(1, 10)))

# trying above, but without repeating elements during single use
while True:
    session = input("Choose: /n 1. 2. 3. c. r.:")
    if session == "1":
        print(random.choice(movements))
    if session == "2":
        print(random.sample(movements, 2))
    if session == "3":
        print(random.sample(movements, 3))
    if session == "c":
        print(random.sample(movements, k=random.randint(4, 10)))
    if session == "r":
        print(random.sample(movements, k=random.randint(1, 10)))

