# python lists
def lists():
    students = ["Ken", "John", "Allan", "Kelly", "Andy"]
    print(students[0:3])  # prints the list 0 inclusive, 3 exclusive
    print(students[-1])  # prints the last element in the list


def methods():
    users = ["Ken", "John", "Allan", "Kelly"]
    ages = [40, 20, 10, 14, 25]
    max_age = max(ages)
    print(max_age)
    min_age = min(ages)
    print(min_age)
    print(sorted(ages, reverse=True))
    ages.append(22)
    print(ages)
    print(ages.pop(-2))
    print(ages)
    print(ages.remove(22))
    print(ages)
    print(' '.join(users))


if __name__ == '__main__':
    methods()
