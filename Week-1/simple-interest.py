#write program to calculate simple interest

p = input("Enter the principle amount: ")
R = input("Enter the rate: ")
T = input("Enter the time: ")

simple_interest = (int(p)*int(R)*int(T))/100

print(simple_interest)