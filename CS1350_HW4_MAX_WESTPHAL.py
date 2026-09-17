#3.1
# Beginner

inventory = {"apples": 50, "bananas": 30, "oranges": 25}

print("Products:")
for product in inventory:
    print(product)

total_items = sum(inventory.values())
print("\nTotal items:", total_items)
print("\nInventory:")
for product, quantity in inventory.items():
    print(f"{product}: {quantity}")


# Intermediate
prices = {"laptop": 999, "phone": 699, "tablet": 449, "watch": 299}
print("\nProducts sorted alphabetically:")
for product in sorted(prices):
    print(product)

print("\nProducts sorted by price:")
for product, price in sorted(prices.items(), key=lambda item: item[1]):
    print(f"{product}: ${price}")

most_expensive = max(prices.items(), key=lambda item: item[1])
print("\nMost expensive item:")
print(f"{most_expensive[0]}: ${most_expensive[1]}")
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}


# Advanced
temps = {"Mon": 72, "Tue": 68, "Wed": 75, "Thu": 80, "Fri": 65}

average_temp = sum(temps.values()) / len(temps)
print("Average temperature:", average_temp)

hottest_day = coldest_day = None
highest_temp = float("-inf")
lowest_temp = float("inf")

for day, temp in temps.items():
    if temp > highest_temp:
        highest_temp = temp
        hottest_day = day
    if temp < lowest_temp:
        lowest_temp = temp
        coldest_day = day

print(f"Hottest day: {hottest_day} ({highest_temp}°F)")
print(f"Coldest day: {coldest_day} ({lowest_temp}°F)")

above_average_count = 0

for temp in temps.values():
    if temp > average_temp:
        above_average_count += 1
print("Days above average:", above_average_count)



#3.2
# Beginner

products = {
    "laptop": {"price": 999, "stock": 15},
    "phone": {"price": 699, "stock": 50}
}
print("Laptop price:", products["laptop"]["price"])

print("\nProduct stock levels:")
for product, info in products.items():
    print(f"{product}: {info['stock']} in stock")


# Intermediate

countries = ["USA", "Canada", "Mexico"]
capitals = ["Washington", "Ottawa", "Mexico City"]

country_capitals = dict(zip(countries, capitals))
print("\nCountry Capitals:")
print(country_capitals)

products["tablet"] = {"price": 449, "stock": 30}

print("\nProducts after adding tablet:")
for product, info in products.items():
    print(f"{product}: Price=${info['price']}, Stock={info['stock']}")

for product in list(products.keys()):
    if products[product]["stock"] < 20:
        del products[product]

print("\nProducts after removing stock < 20:")
for product, info in products.items():
    print(f"{product}: Price=${info['price']}, Stock={info['stock']}")
    
# Advanced
company = {
    "Engineering": {"Alice": 95000, "Bob": 85000},
    "Marketing": {"Carol": 75000, "Dave": 70000}
}

print("Employees and Salaries:")
for department, employees in company.items():
    print(f"\n{department}:")
    for employee, salary in employees.items():
        print(f"{employee}: ${salary}")

print("\nAverage Salary Per Department:")
for department, employees in company.items():
    average_salary = sum(employees.values()) / len(employees)
    print(f"{department}: ${average_salary:.2f}")

highest_employee = ""
highest_salary = 0
highest_department = ""

for department, employees in company.items():
    for employee, salary in employees.items():
        if salary > highest_salary:
            highest_salary = salary
            highest_employee = employee
            highest_department = department

print("\nHighest-Paid Employee:")
print(f"{highest_employee} ({highest_department}) - ${highest_salary}")

#3.3
# Beginner

cubes = {num: num**3 for num in range(1, 6)}
print("Cubes:", cubes)

temps = {"Mon": 72, "Tue": 68, "Wed": 75}

celsius_temps = {
    day: (temp - 32) * 5 / 9
    for day, temp in temps.items()
}
print("Celsius Temperatures:", celsius_temps)

#Intermideate 
scores = {"Alice": 88, "Bob": 65, "Carol": 92, "Dave": 71, "Eve": 58}

passing_dict = {
    student: score
    for student, score in scores.items()
    if score >= 70
}

print("Passing Scores:", passing_dict)
letter_grades = {
    student:
        "A" if score >= 90 else
        "B" if score >= 80 else
        "C" if score >= 70 else
        "D" if score >= 60 else
        "F"
    for student, score in scores.items()
}
print("Letter Grades:", letter_grades)

student_ids = {"Alice": 101, "Bob": 102}
inverted_ids = {
    student_id: student
    for student, student_id in student_ids.items()
}

print("Inverted IDs:", inverted_ids)

# Advanced
sales = [
    ("North", "Alice", 5000),
    ("South", "Bob", 4500),
    ("North", "Carol", 6000),
    ("South", "Alice", 3500)
]
sales_by_region = {}

for region, person, amount in sales:
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

print("Sales by Region:")
print(sales_by_region)
sales_by_person = {}

for region, person, amount in sales:
    sales_by_person[person] = sales_by_person.get(person, 0) + amount

print("\nSales by Salesperson:")
print(sales_by_person)
nested_sales = {}

for region, person, amount in sales:
    if region not in nested_sales:
        nested_sales[region] = {}

    nested_sales[region][person] = (
        nested_sales[region].get(person, 0) + amount
    )
print("\nNested Sales Dictionary:")
print(nested_sales)


#Unite 1
#Beginner
vowels = {"a", "e", "i", "o", "u"}
print(vowels)

numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(numbers)

print(unique_numbers)
print("Number of elements:", len(unique_numbers))

# empty = {} creates a empty dictionary not a empty set

#Intermediate
text = "mississippi"

unique_letters = set(text)

print(unique_letters)
print("Number of unique letters:", len(unique_letters))

emails = ["a@b.com", "c@d.com", "a@b.com", "e@f.com", "c@d.com"]

unique_emails = list(set(emails))

print(unique_emails)

#s = {[1, 2], [3, 4]} fails because lists are mutable and therefore unhashable, so they cannot be stored in a set

#Advanced
import time

numbers_list = list(range(1_000_000))
numbers_set = set(numbers_list)

start = time.time()
999999 in numbers_list
list_time = time.time() - start

start = time.time()
999999 in numbers_set
set_time = time.time() - start

print("List lookup time:", list_time)
print("Set lookup time:", set_time)
key = frozenset(["red", "green", "blue"])

color_groups = {
    key: "Primary Colors"
}
print(color_groups[key])
edges = [(1, 2), (2, 3), (1, 3), (3, 4)]

nodes = set()

for a, b in edges:
    nodes.add(a)
    nodes.add(b)

print(nodes)

#Unit 2
#Beginner
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("Union:", a | b)

print("Intersection:", a & b)

print("Difference (a - b):", a - b)

# Intermediate
morning_shift = {"Alice", "Bob", "Carol"}
evening_shift = {"Carol", "Dave", "Eve"}
weekend_shift = {"Alice", "Eve", "Frank"}

all_shifts = morning_shift & evening_shift & weekend_shift
print("Work all shifts:", all_shifts)

any_shift = morning_shift | evening_shift | weekend_shift
print("Work at least one shift:", any_shift)

only_morning = morning_shift - evening_shift - weekend_shift
print("Only morning:", only_morning)

exactly_one = set()

for employee in any_shift:
    count = (
        (employee in morning_shift) +
        (employee in evening_shift) +
        (employee in weekend_shift)
    )
    if count == 1:
        exactly_one.add(employee)

print("Exactly one shift:", exactly_one)

# Advanced
prereqs_met = {"Alice", "Bob", "Carol", "Dave"}
has_space = {"Bob", "Carol", "Eve", "Frank"}
paid_tuition = {"Alice", "Carol", "Eve"}

eligible = prereqs_met & has_space & paid_tuition
print("Eligible to enroll:", eligible)

not_paid = prereqs_met - paid_tuition
print("Met prereqs but haven't paid:", not_paid)

need_prereqs_or_pay = (has_space | paid_tuition) - (prereqs_met & paid_tuition)
print("Need prereqs or tuition:", need_prereqs_or_pay)

#Unit 3
#Beginner
numbers = {1, 2, 3}

numbers.add(4)
numbers.remove(1)

print(numbers)

evens = {num for num in range(21) if num % 2 == 0}

print(evens)
numbers = {1, 2, 3}

numbers.discard(5)

print(numbers)
#intermediate
nums = [4, 5, 2, 4, 8, 5, 2, 1, 9, 4]

seen = set()
result = []

for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)
sentence = "To be or not to be that is the question"
unique_words = {word.lower() for word in sentence.split()}

print(unique_words)
expected = set(range(1, 11))
actual = {1, 2, 4, 5, 7, 8, 10}

missing = expected - actual

print(missing)

# Advanced
def find_duplicates(lst):
    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return duplicates

print(find_duplicates([1, 2, 2, 3, 3, 3, 4]))

alice = {"Python", "SQL", "Excel", "Tableau"}
bob = {"Python", "Java", "SQL", "AWS"}
carol = {"Python", "R", "SQL", "Tableau"}

print("All three have:", alice & bob & carol)
print("Only Alice has:", alice - bob - carol)
print("All unique skills:", alice | bob | carol)

def common_chars(str1, str2):
    return set(str1) & set(str2)

print(common_chars("hello", "world"))
