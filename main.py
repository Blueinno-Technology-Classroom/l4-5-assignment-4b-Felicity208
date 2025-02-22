# ✅ Complete this function, replace `pass` with your solution:
def count(numbers) -> dict:
    typesofnum = []
    result = {}
    for num in numbers:
        if num not in typesofnum:
            typesofnum.append(num)
            result[num] = 1
        else:
            result[num] += 1

    return result






    

# ❌ Do NOT change these lines:
list1 = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
list2 = [-1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 99]

count1 = count(list1)
count2 = count(list2)

print(count1)  # --> {1: 3, 2: 2, 3: 1, 4: 4, 5: 5}
print(count2)  # --> {-1: 8, 0: 3, 99: 1}
