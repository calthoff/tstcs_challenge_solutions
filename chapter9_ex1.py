an_array = [2,44,3,43,6,7,5,89, 14, 56]
evens = []
odds = []
for i in an_array:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
new_array = evens + odds
print(new_array)