def linear_search_product(products, target_product):
    indices = []
    for i in range(len(products)):
        if products[i] == target_product:
            indices.append(i)
    return indices


products = ["apple", "banana", "orange", "banana", "grape", "banana"]
target_product = "banana"

indices = linear_search_product(products, target_product)
if indices:
    print("Target product found at indices:", indices)
else:
    print("Target product not found.")