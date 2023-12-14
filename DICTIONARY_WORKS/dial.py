dials={
    "1":["a","b","c"],
    "2":["d","e","f"],
    "3":["g","h","i"]
}
user_input="13"
result=[]
for ch in user_input:
    result.append(dials.get(ch))
print(result)
last_result=[(i,k) for i in result[0] for k in result[1]]
    
print(last_result)
