appearance= {}
myList = [2,2,2,2,2,2,2,1,3]
for i in range (len(myList)):
    if f"{myList[i]}" in appearance.keys():
        appearance[f"{myList[i]}"] += 1
    else:
        appearance[f"{myList[i]}"] = 1
for key, value in appearance.items():
    if value > len(myList)/3:
        print("The element appears mor ethan n/3 times: ", key)
print(appearance)