"""wap to calculate the monthly electricity bill for multiple customers.
i) input number of customers
ii) input name in units used
iii) compute bill;
    0-100 units -> 2.5/unit
    101-200 units -> 3.9/unit
    >200 units -> 5.0/unit
iv) display each bill and revenue collected"""


def computeBill(unitsConsumed):
    if unitsConsumed <= 100:
        bill = unitsConsumed * 2.5
    elif unitsConsumed <= 200:
        bill = (100 * 2.5) + (unitsConsumed - 100) * 3.9
    else:
        bill = (100 * 2.5) + (100 * 3.9) + (unitsConsumed - 200) * 5
    return bill


def printBill(customerName, unitsConsumed, totalBill):
   
    print(f"Customer Name   : {customerName}")
    print(f"Units Consumed  : {unitsConsumed}")
    print(f"Total Bill (₹)  : {totalBill}")
    
    print()


customerNumber = int(input("Number of Customers: "))

for i in range(customerNumber):
    print(f"\n Customer {i + 1}")
    customerName = input("Enter Name: ")
    unitsConsumed = float(input("Enter number of units consumed: "))

    totalBill = computeBill(unitsConsumed)
    printBill(customerName, unitsConsumed, totalBill)
