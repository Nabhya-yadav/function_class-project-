def calculate(bill_amount, tip_percentage):
    if bill_amount<=0:
        print("bill amount cannot be 0")

    else:
        result=(tip_percentage/bill_amount)*100

    return result

tip=calculate(100,5)

print(tip)