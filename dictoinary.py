# user={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}
# print(user)

#clear dictionary
# user={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}
# user.clear()
# print(user)

#copying dictionary
# user={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}

# user_backup=user.copy()

# print(user_backup)

#keys
# user={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}

# print(user.keys())

#values
# user={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}
# print(user.values())

#update
# user={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}

# user.update({"Age":"34","height":"12"})
# print(user)

#MATCHING MULIPLE DICTIONARIES
# user1={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}

# user2={"Age":"34","height":"12"}
# user1.update(user2)
# print(user1)

#REMOVE AN ITEM
# user1={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}
# user1.pop("id")
# print(user1)

#LOOP THROUGH DICTIONARY
# user1={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}

# for i in user1:
#     print(i)

#LOOP values with keys.
user1={"name":"Timo","id":"2314","salary":"34200","home":"kenya"}

for key,value in user1.items():
    print(key,value)