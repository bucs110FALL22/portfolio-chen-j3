import random
#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)

classes_per_week = 3
print(classes_per_week, type(classes_per_week))
cost_per_class = cost_per_week / classes_per_week
print(cost_per_class, type(cost_per_class))
print("Your cost per class is $", cost_per_class)

#Part B
#import random MUST INCLUDE TOP OF FILE BEFORE ANY CODE
#random.randrange(1,10)
dataObjects = [1, 1/5, "stem", 888, 23/2]
randomObj = random.choice(dataObjects)
print("Your random object is", randomObj)