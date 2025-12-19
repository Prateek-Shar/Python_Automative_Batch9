# Adds a single element to the end of the list.
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)


# Removes the first occurrence of a specified value.
numbers = [1, 2, 3, 2, 4]
numbers.remove(2)
print(numbers)


# Removes and returns an element at a given index.
numbers = [10, 20, 30, 40]

last_element = numbers.pop()
print(last_element)
print(numbers)


# Inserts an element at a specific position.
numbers = [1, 2, 4]
numbers.insert(2, 3)
print(numbers)


# Sorts the list in ascending order by default.
numbers = [4, 1, 3, 2]
numbers.sort()
print(numbers)


# Removes all elements from the list.
numbers = [1, 2, 3]
numbers.clear()
print(numbers)