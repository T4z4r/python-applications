n = 5

# Upper part of the diamond (including the middle line)
for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

# Lower part of the diamond
for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))
