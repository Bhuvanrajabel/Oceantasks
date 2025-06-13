import random
print(random.randint(3,9))
print(random.uniform(10,70))
list=["apple","orange","banana"]
print(random.choice(list))
print(random.choices(list,weights=[10,1,1],k=5))
print(random.sample(list,k=2))
random.shuffle(list)
print(list)