from prettytable import from_csv

filename = input("Please enter the original csv filename: \n")

with open(filename, "r") as fp:
	table = from_csv(fp)

print(table)

