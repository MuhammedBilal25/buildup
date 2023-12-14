from json import load
f=open("C:\\Users\\USER\\Desktop\\L-P\\JSON_WORKS\\data.json",encoding="UTF-8")
data=load(f)
source_currency_code=input("enter source currency code : ")
target_currency_code=input("enter the target currency code : ")
amount=int(input("ENTER THE AMOUNT : "))
conversion_rates=data.get("conversion_rates")
source_currency_code_rate=conversion_rates.get(source_currency_code)
target_currency_code_rate=conversion_rates.get(target_currency_code)
print(source_currency_code_rate)
print(target_currency_code_rate)
res=(amount/source_currency_code_rate)*target_currency_code_rate
print(res)