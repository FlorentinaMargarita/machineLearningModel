import random

random.seed()
for i in range(10000):
    temperature = random.randint(15, 25)
    humidity = random.randint(20, 40)
    sound = random.randint(70, 90)

    problem =  1 if sound > 85 else 0
    print(temperature, humidity, sound, problem)