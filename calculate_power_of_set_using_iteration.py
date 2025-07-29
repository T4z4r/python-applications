def power_set_iterative(s):
    power_set = [[]]
    for elem in s:
        power_set += [curr + [elem] for curr in power_set]
    return power_set

input_set = input("Enter a set of elements separated by spaces: ").split()
print("Power set:", power_set_iterative(input_set))