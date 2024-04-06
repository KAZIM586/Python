import json
d='{"cname":"python","fees":1200,"duration":"2 Months"}'
x=json.loads(d)
print(x)
print(type(x))
for a in x:
    print(a)
    print(a,x[a])
