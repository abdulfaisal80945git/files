n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    closing = int(input("Enter actual closing stock: "))
    minimum = int(input("Enter minimum stock required: "))

    if min(opening, incoming, dispatched, closing, minimum) < 0:
        print("Invalid stock details")
        continue

    expected = opening + incoming - dispatched

    print("\nProduct:", name)
    print("Expected Closing Stock:", expected)

    if closing != expected:
        print("Discrepancy:", closing - expected)
    else:
        print("No discrepancy")

    if closing < minimum:
        replenish = minimum - closing
        print("Replenishment Required:", replenish)
    else:
        print("No replenishment required")

print("\nInventory checking completed.")
