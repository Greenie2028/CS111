points_per_category = {
    "Homework": 50,
    "Labs": [1,2,3],
    17: 95, #Please don't
    "Projects":{
        "points": 20,
        "percentage": 10
    }
}
print(points_per_category["Projects"])
for key in points_per_category:
    print(key, points_per_category[key])

scores = {
    "Labs": [20, 10, 15],
    "Projects": [1,1,1]
}
print(scores)
scores["Projects"][1]=100
scores["Projects"].append(1000)
try:
    scores["Dancing"]
except KeyError:
    print("Oops there is no dancing")
scores["Dancing"] = []
scores["Dancing"].append(9)
scores[(1,2,3)] = 0
print(scores)

a = scores
b = scores
c = 10

print(id(scores))
print(id(a))
print(id(b))
print(id(c))

