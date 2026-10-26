
budget = float(input("Enter your budget: "))
n = int(input("Enter number of products: "))

products = []
total = 0

for i in range(n):
    print("\nProduct", i + 1)
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity!")
        continue

    cost = price * quantity
    products.append([name, price, quantity, cost])
    total += cost

# Apply discount
if total >= 5000:
    discount = total * 0.10
elif total >= 2000:
    discount = total * 0.05
else:
    discount = 0

final_total = total - discount

print("\n----- SHOPPING BILL -----")
print("Total amount: Rs.", round(total, 2))
print("Discount: Rs.", round(discount, 2))
print("Final amount: Rs.", round(final_total, 2))
print("Budget: Rs.", round(budget, 2))

if final_total <= budget:
    print("Shopping is within budget.")
else:
    excess = final_total - budget
    print("Amount exceeding budget: Rs.", round(excess, 2))
    print("\nReduce or remove these purchases:")

    # Check expensive products first
    products.sort(key=lambda x: x[3], reverse=True)

    for item in products:
        if excess <= 0:
            break

        name, price, quantity, cost = item
        print(name, "- Current quantity:", quantity)

        reduction = min(quantity, int(excess // price) + 1)
        excess -= min(reduction * price, cost)

        print("Suggested quantity reduction:", reduction)

    if excess > 0:
        print("Further reductions may be required.")
