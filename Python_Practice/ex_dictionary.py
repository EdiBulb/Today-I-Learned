MSE = {
    "location" : "Auckland",
    "Tuition fee" : 3000,
    "class" : 2
}

print(MSE["location"])
print(MSE["Tuition fee"])
print(MSE["class"])

MSE["new"] = "new"
print(MSE)

del MSE["new"]
print(MSE)

print(MSE.keys())
print(MSE.values())

print(MSE.get("location"))

print("================================================")

'''finding average of product people want to buy'''
if __name__ == '__main__':
    n = int(input("number of people?: "))
    
    people_products = {} # dictionary
    
    # get name and price of products
    for _ in range(n):
        name, *line = input("name and prices:").split() # packing rest of data except name
        prices = list(map(float, line)) # map : change data type to float
        people_products[name] = prices
    
    query_name = input("who do you want to find?: ")
    
    if query_name in people_products:
        values = people_products[query_name] # put prices in list "values"
        average = sum(values) / len(values)
        print(f"{average:.2f}")
    else:
        print("the person not found!")