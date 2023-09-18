list = ["1.1", "2.2", "3.3"]

def sum (arr):
    total = 0

    for num in arr:
        total += float(num)

    return total

print(sum(list))
