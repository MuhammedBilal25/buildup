insta_users={"mohanlal","prithvi","dq","vijay","fahad","sureshgopi","lalu"}
mohanlal_following={"prithvi","vijay","lalu"}
dq_following={"prithvi","fahad","sureshgopi","lalu"}
insta_users.remove("mohanlal")
suggesion=insta_users.difference(mohanlal_following)
print(f"SUGGESTIONS ARE : {suggesion}")
mutual_friends=mohanlal_following.intersection(dq_following)
print(f"MUTUAL FRIENS ARE : {mutual_friends}")