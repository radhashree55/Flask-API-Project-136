import pandas as pd

data = pd.read_csv("starsWithGravity.csv")

starName = data["Star_name"].tolist()
distance = data["Distance"].tolist()
mass = data["Mass"].tolist()
radius = data["Radius"].tolist()
gravity = data["Gravity"].tolist()

finalStarList = []

temp_dict = {}

for i in range(0, len(starName)):
    temp_dict["name"] = starName[i]
    temp_dict['distance'] = distance[i]
    temp_dict["mass"] = mass[i]
    temp_dict["radius"] = radius[i]
    temp_dict['gravity'] = gravity[i]
    finalStarList.append(temp_dict)
    temp_dict={}

print(finalStarList)

