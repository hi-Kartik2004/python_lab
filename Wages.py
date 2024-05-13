def calculatePayment(hours, pay):
    double = 0
    extra = 0
    regular = 0
    if(hours > 60):
        double = hours - 60
        extra = 20
        regular = 40
    elif hours > 40:
        extra = hours - 40
        regular = 40
    else:
        regular = hours

    return double*2*pay + extra*1.5*pay + regular * pay


hours = int(input("Enter the number of hours: "))
pay = float(input("Enter the hourly pay: "))

print(calculatePayment(hours, pay))
