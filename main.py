def count_ones(left, right):
    return sum(bin(i).count("1") for i in range(left, right + 1))


print(count_ones(4,7))