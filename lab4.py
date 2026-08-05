print("----ELECTRICITY BILL GENERATOR-----")
name = input("Enter consumer name: ")
id = int(input("Enter consumer id: "))
pmr=int(input("Enter previous month reading: "))
cmr=int(input("Enter current month reading: "))
cost=int(input("Enter cost per unit: "))

consumed_unit = cmr - pmr
energy_cost = consumed_unit * cost
electricity_duty = energy_cost * 0.05
fixed_charge = 100
total_bill = energy_cost + electricity_duty + fixed_charge

print(f"Consumer name is {name} and consumer id is {id}")
print(f"Previous month reading is {pmr} and current month reading is {cmr}")
print(f"Consumed unit is {consumed_unit} and cost per unit is {cost}")
print(f"Energy cost is {energy_cost} and electricity duty is {electricity_duty}")
print(f"Fixed charge is {fixed_charge} and total bill is {total_bill}")


