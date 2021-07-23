the_count = [1, 2, 3, 4, 6]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]

#looping

for number in the_count:
    print("This is count", number)

for stock in stocks:
    print("Stock ticker:", stock)

for i in random_things:
    print("Here's a random thing:", i)

# we can also build lists, first let's start with an empty one
people = []

people.append(input("teste: "))
people.append("Sarah")
people.append("Chris")

# now we can print them out too
print(people)

# and remove some
people.remove("Sarah")
print(people)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for square in numbers:
    print("The square of", square, "is", square**2)

# Challenge: Print out the square of the numbers 1 to 10
for number in range(1,11):
    print(number, "squared is", number * number)

# here's how you access elements of a list
animals = ['bear', 'tiger', 'penguin', 'zebra']
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)
animals.append(input("What is your favorite animal? "))
favorite_animal = animals[-1]
print(favorite_animal)
print("There are this many animals:", len(animals))
