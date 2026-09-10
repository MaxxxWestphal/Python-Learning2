# CS1350 Mini Project 1

# Phase 1 - Quick Contacts

print("=== Phase 1: Quick Contacts ===")
quick_contacts = {}
quick_contacts["Mom"] = "555-1234"
quick_contacts["Dad"] = "555-5678"
quick_contacts["Best Friend"] = "555-8888"
quick_contacts["Pizza Place"] = "555-9999"
quick_contacts["Work"] = "555-0000"
print(quick_contacts)
print("\n--- Access and Modify ---")
print("Mom's number:", quick_contacts["Mom"])

quick_contacts["Dad"] = "555-1234"
quick_contacts["Dentist"] = "555-2222"

grandma = quick_contacts.get("Grandma", "Contact not found")
print("Looking up Grandma:", grandma)

print("Updated contacts:", quick_contacts)

print("\n--- Delete and Analyze ---")

del quick_contacts["Pizza Place"]

old_work = quick_contacts.pop("Work")
print("Removed work number:", old_work)

print("Contacts remaining:", len(quick_contacts))
print("Contact names:", list(quick_contacts.keys()))
print("Phone numbers:", list(quick_contacts.values()))

print()

# Data
contact_book = {
    "Mom": {"phone": "555-1234", "category": "Family", "city": "Fort Wayne"},
    "Dad": {"phone": "555-4321", "category": "Family", "city": "Fort Wayne"},
    "Sister": {"phone": "555-7777", "category": "Family", "city": "Chicago"},
    "Best Friend": {"phone": "555-8888", "category": "Friend", "city": "Indianapolis"},
    "Roommate": {"phone": "555-3141", "category": "Friend", "city": "Fort Wayne"},
    "Boss": {"phone": "555-0000", "category": "Work", "city": "Chicago"},
    "Professor": {"phone": "555-2718", "category": "Work", "city": "Fort Wayne"},
    "Dentist": {"phone": "555-2222", "category": "Business", "city": "Indianapolis"},
}

call_log = {
    "Mom": {"Jan": 120, "Feb": 95, "Mar": 140},
    "Dad": {"Jan": 45, "Feb": 60, "Mar": 30},
    "Sister": {"Jan": 80, "Mar": 70},
    "Best Friend": {"Jan": 200, "Feb": 180, "Mar": 220},
    "Roommate": {"Feb": 15, "Mar": 25},
    "Boss": {"Jan": 60, "Feb": 90, "Mar": 75},
    "Professor": {"Feb": 20, "Mar": 35},
    "Dentist": {"Jan": 10},
}

# Phase 2 - Contact Activity

print("=== Phase 2: Contact Activity ===")

total_minutes = {}
for contact, months in call_log.items():
    months_called = len(months)
    total = sum(months.values())
    average = total / months_called
    busiest_month = ""
    busiest_minutes = 0
    for month, minutes in months.items():
        if minutes > busiest_minutes:
            busiest_minutes = minutes
            busiest_month = month
    total_minutes[contact] = total

    print(
        f"{contact}: {months_called} month(s), "
        f"{total} min total, avg: {average:.2f}, "
        f"busiest: {busiest_month} ({busiest_minutes})"
    )

print()

# Phase 3A - Month Statistics

print("=== Phase 3: Aggregations ===")
month_stats = {}
for contact, months in call_log.items():
    for month, minutes in months.items():
        if month not in month_stats:
            month_stats[month] = {
                "minutes": []
            }
        month_stats[month]["minutes"].append(minutes)
for month in month_stats:
    minutes_list = month_stats[month]["minutes"]
    month_stats[month]["total"] = sum(minutes_list)
    month_stats[month]["avg"] = sum(minutes_list) / len(minutes_list)
    month_stats[month]["contacts"] = len(minutes_list)
print("Monthly summary (sorted by average, highest first):")
sorted_months = sorted(
    month_stats.items(),
    key=lambda item: item[1]["avg"],
    reverse=True
)

for month, stats in sorted_months:
    print(
        f"{month}: {stats['total']} min total, "
        f"{stats['avg']:.2f} avg "
        f"({stats['contacts']} contacts)"
    )
# Phase 3B - Aggregation with get()

minutes_by_category = {}
minutes_by_city = {}
contacts_per_city = {}
for name, details in contact_book.items():

    category = details["category"]
    city = details["city"]
    minutes = total_minutes[name]
    minutes_by_category[category] = (
        minutes_by_category.get(category, 0) + minutes
    )
    minutes_by_city[city] = (
        minutes_by_city.get(city, 0) + minutes
    )
    contacts_per_city[city] = (
        contacts_per_city.get(city, 0) + 1
    )

print("\nMinutes by category:", minutes_by_category)
print("Minutes by city:", minutes_by_city)
print("Contacts per city:", contacts_per_city)
print()
# Phase 4 - Dictionary Comprehensions

print("=== Phase 4: Comprehensions ===")
phone_book = {
    name: details["phone"]
    for name, details in contact_book.items()
}
local_contacts = {
    name: details["phone"]
    for name, details in contact_book.items()
    if details["city"] == "Fort Wayne"
}
activity_level = {
    name: ("Frequent" if minutes >= 200 else "Occasional")
    for name, minutes in total_minutes.items()
}
print("Phone book:", phone_book)
print("Local contacts (Fort Wayne):", local_contacts)
print("Activity level:", activity_level)
print()

# Phase 5 - Tier Report


print("=== Phase 5: Tier Report ===")
def get_tier(minutes):
    if minutes >= 400:
        return "Platinum"
    elif minutes >= 200:
        return "Gold"
    elif minutes >= 100:
        return "Silver"
    elif minutes >= 50:
        return "Bronze"
    else:
        return "Inactive"
for name, minutes in total_minutes.items():
    print(f"{name}: {minutes} min ({get_tier(minutes)})")

print("\n--- Tier Distribution ---")

platinum = 0
gold = 0
silver = 0
bronze = 0
inactive = 0

for minutes in total_minutes.values():
    if minutes >= 400:
        platinum += 1
    elif minutes >= 200:
        gold += 1
    elif minutes >= 100:
        silver += 1
    elif minutes >= 50:
        bronze += 1
    else:
        inactive += 1

print("Platinum:", platinum)
print("Gold:", gold)
print("Silver:", silver)
print("Bronze:", bronze)
print("Inactive:", inactive)
print("\n--- Top and Bottom ---")
top_name = ""
top_minutes = 0

bottom_name = ""
bottom_minutes = 999999

for name, minutes in total_minutes.items():
    if minutes > top_minutes:
        top_minutes = minutes
        top_name = name
    if minutes < bottom_minutes:
        bottom_minutes = minutes
        bottom_name = name
print(f"Most contacted: {top_name} ({top_minutes} min)")
print(f"Least contacted: {bottom_name} ({bottom_minutes} min)")

grand_total = sum(total_minutes.values())
average_contact = grand_total / len(total_minutes)
print(f"Total minutes: {grand_total}")
print(f"Average per contact: {average_contact:.2f}")
print("\n--- Above Average Contacts ---")

for name, minutes in total_minutes.items():
    if minutes > average_contact:
        print(f"{name}: {minutes}")
print()

#Phase 6 - Contact Hub Report

print("=== Phase 6: Contact Hub Report ===")
print(
    f"{'Name':<12} {'Category':<10} {'City':<15} {'Minutes':>8} {'Tier':>10}"
)
print("-" * 60)
sorted_contacts = sorted(
    total_minutes.items(),
    key=lambda item: item[1],
    reverse=True
)
for name, minutes in sorted_contacts:

    category = contact_book[name]["category"]
    city = contact_book[name]["city"]
    tier = get_tier(minutes)
    print(
        f"{name:<12} "
        f"{category:<10} "
        f"{city:<15} "
        f"{minutes:>8} "
        f"{tier:>10}"
    )
print("-" * 60)
print(
    f"{len(contact_book)} contacts | "
    f"{grand_total} total minutes | "
    f"{average_contact:.2f} average"
)
#ThatwassolongLOL
