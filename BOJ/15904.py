inputs = input()
lists = ["U","C","P","C"]

for i in inputs:
    if i in lists:
        if i==lists[0]:
            del lists[0]

if len(lists)==0:
    print("I love UCPC")
else:
    print("I hate UCPC")