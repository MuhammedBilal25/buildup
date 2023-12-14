from json import load
f=open("C:\\Users\\USER\\Desktop\\L-P\\products\\items.json","r",encoding="UTF-8")
data=load(f)
# print(len(data))
category={d.get("category")for d in data}
# print(category,len(data))
electronoic_product=[d for d in data if d.get("category")=="electronics"]
print(electronoic_product)
# print(len(electronoic_product))
jewellery_product=[d for d in data if d.get("category")=="jewelery"]
# print(len(jewellery_product))
costly_product=max()