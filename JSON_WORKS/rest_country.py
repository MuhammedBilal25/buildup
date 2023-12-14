from json import load
f=open("C:\\Users\\USER\\Desktop\\L-P\\JSON_WORKS\\countrydata.json", encoding="UTF-8")
data=load(f)
print(len(data))

# for all country names
all_country_name=[c.get("name")for c in data]
# print(all_country_name)

# for all country comes under asian continant
asian_country=[c.get("name")for c in data if c.get("region")=="Asia"]
# print(asian_country)

# independent_country_names
independent_country=[c.get("name")for c in data if c.get("independent")==True]
# print(independent_country,len(independent_country))

# all_regions
all_regions={c.get("region") for c in data }
# print(all_regions,"no.of regions:",len(all_regions))

# find capital of ukraine
cap_of_ukraine=[c.get("capital") for c in data if c.get("name")=="Ukraine"]
# print("capital of Ukraine is :",cap_of_ukraine)

# countryname  capital 
country_and_capital=[(c.get("name"),c.get("capital"))for c in data]
# print(country_and_capital)

# find most populated country 
polutaed_country=max(data,key=lambda d:d.get("population") )
# print(polutaed_country.get("name"))

# print all country name and currency name 
for c in data:
    if "currencies" in c :
        currency_dat=c.get("currencies")[0]
        # print(c.get("name"),":",currency_dat.get("name"))
   
# print all countries sharing border with India 
Indian_border=[c.get("borders")for c in data if c.get("name")=="India"] [0]
# print(Indian_border)

# for getting the full name of countries charing the border with India 
indian_border_name=[c.get("name")for c in data if c.get("alpha3Code") in Indian_border]
# print("List of countries sharing border with INDIA:",indian_border_name)

# print country name share more than 4 country 
four_border_country=[c.get("name")for c in data if "borders" in c and len(c.get("borders"))>4 ]
print(four_border_country)
