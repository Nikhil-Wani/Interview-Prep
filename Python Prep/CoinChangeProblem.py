# sum = 1100

# num1= sum // 5
# num1Mod = sum % 5

# num1Mod != 0
# num2 = num1Mod // 3
# num2Mod = num1Mod % 3

# num2Mod !=0
# num3 = num2Mod // 1
# num3Mod = num2Mod % 1

# result = num1 + num2+ num3
# print(result)

sum = 104
coins_available = [2,5,10,3,1]  # coins available for change
coins_available.sort(reverse=True)

result = 0
for coin in coins_available:
    number_of_coins = sum // coin  # Integer division
    sum = sum % coin
    result += number_of_coins

print(result)




