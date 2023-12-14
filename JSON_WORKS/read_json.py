from json import load
f=open("C:\\Users\\USER\\Desktop\\L-P\\JSON_WORKS\\stdt.json","r")
data=load(f)
all_names=[emp.get("name") for emp in data]
all_dept={emp.get("department") for emp in data}
print(all_names)
print(all_dept)
max_sal=max(data,key=lambda k: k.get("salary"))
print(max_sal)