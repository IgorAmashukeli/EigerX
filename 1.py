def priceCheck(products, productPrices, productSold, soldPrice):
    prices, count = {}, 0
    n, m = len(products), len(productSold)
    for i in range(n):
        prices[products[i]] = productPrices[i]
    for i in range(m):
        if soldPrice[i] != prices[productSold[i]]:
            count += 1
    return count


print(priceCheck(
    products = ['eggs', 'milk', 'cheese'],
    productPrices = [2.89, 3.29, 5.79],
    productSold = ['eggs', 'eggs', 'cheese', 'milk'],
    soldPrice = [2.89, 2.99, 5.97, 3.29]
))