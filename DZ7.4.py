def common_elements():
    numbers = range(100)

    elist_3 = []
    for x in numbers:
        if x % 3 == 0:
            elist_3.append(x)

    elist_5 = []
    for x in numbers:
        if x % 5 == 0:
            elist_5.append(x)
    set_3 = set(elist_3)
    set_5 = set(elist_5)

    common = set_3 & set_5
    return common


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}  # якраз всі кратні 15
print("Yes")
# assert common_elements() == {0, 74, 45, 15, 91, 65, 33} # - AssertionError
