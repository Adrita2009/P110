import random

response = int(input("Do you want to roll the dice? Press 1 for yes and 2 for no: "))

while response==1:
    no = random.randint(1,6)

if no == 1:
    print("[-----]")
    print("[     ]")
    print("[  0  ]")
    print("[     ]")
    print("[-----]")
elif no == 2:
    print("[-----]")
    print("[     ]")
    print("[ 0 0 ]")
    print("[     ]")
    print("[-----]")
elif no == 3:
    print("[-----]")
    print("[    0]")
    print("[  0  ]")
    print("[0    ]")
    print("[-----]")
elif no == 4:
    print("[-----]")
    print("[0   0]")
    print("[     ]")
    print("[0   0]")
    print("[-----]")
elif no == 5:
    print("[-----]")
    print("[0   0]")
    print("[  0  ]")
    print("[0   0]")
    print("[-----]")
elif no == 6:
    print("[-----]")
    print("[0   0]")
    print("[0   0]")
    print("[0   0]")
    print("[-----]")

