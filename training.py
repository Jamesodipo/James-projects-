# accessing element in the list
names = ["James","Rodgers","Mike","Ezra","Brian","Collins"]


#print(names[0].lower())
# individual items in the list

#print(f"Hello {names[0]} welcome")
#for name in names:
#	print(f"Hello {name} you are great patner in this project\n")
#	print(f"But remember {name} greatness comes if we work together\t\n")
#adding changing removing items from list
    # modifying elements in the list
names[0]="Mercy"
print(names)
del names[0]
print(names)

popped_name=names.pop()
print(names)
print(popped_name)