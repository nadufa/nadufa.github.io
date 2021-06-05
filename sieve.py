'''
d = {"Alex": 25, "Peter": 37}
print(d)

print(len(d))

d["Kate"] = 18
print(d)
print(len(d))
print(d["Alex"])
print(d["Kate"])
d["Kate"] = 24
print(d["Kate"])

d[10] = 20
print(d)

for k, v in d.items():
    print("key: " + str(k) + ", " + "value: " + str(v))



a = ["first", 1, 2, 3, "second", 10, 20, "third", 15, 56, 70, "fourth", -50]

my_d = {}

pr = None

for e in a:
    if type(e) == str:
        my_d[e] = []
        pr = e
    else:
        my_d[pr].append(e)

print(my_d)




text = "Hello my name is Nadufa I miss my krash"

a = text.split(" ")
b = len(a)
print(b)
'''





a = [1, 2, 3, 'fewfw']
print(a)







