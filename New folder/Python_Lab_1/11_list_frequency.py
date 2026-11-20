# Sample input: apple,banana,apple. Sample output: apple: 2, banana: 1.

items = input("Enter items separated by commas: ").split(",")
frequencies = {}

for item in items:
    item = item.strip()
    if item:
        frequencies[item] = frequencies.get(item, 0) + 1

if frequencies:
    for item, count in frequencies.items():
        print(item + ":", count)
else:
    print("No items were entered.")
