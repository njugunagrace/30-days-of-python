# Declare an empty list
a=[]
# Declare a list with more than 5 items
b=["Grace","Victor","Elizabeth","Shadrack","Joel","Wambui"]
print(len(b))                                     #Find the length of your list
c=b[0]+" "+b[-1]                                  #Get the first item, the middle item and the last item of the list
print(c)
# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=["Grace",18,5.9,"Not married","572Thika"]
print(mixed_data_types)
# Declare a list variable named it_companies and assign initial values Facebook, Google, Apple, IBM, Oracle and Amazon.
it_companies=["Facebook","Google","Apple","IBM","Oracle","Amazon"]
print(it_companies)                                     #Print the list using print()
# Print the number of companies in the list
print(len(it_companies))
print(it_companies[0]+" " +it_companies[-1])             #Print the first, middle and last company
# Print the list after modifying one of the companies
it_companies[0]="Microsoft"
print(it_companies)
# Add an IT company to it_companies
print(it_companies.append("Koko Networks"))

# Insert an IT company in the middle of the companies list
middle=(len(it_companies)-1)//2
it_companies.insert(middle,"Twiga foods")
# Change one of the it_companies names to uppercase (IBM excluded!)
capital=it_companies[0].upper()
print(capital)

# Join the it_companies with a string '#;  '
companies= '#'.join(it_companies)
print(companies)
# Check if a certain company exists in the it_companies list.
exist="Koko Networks"in it_companies
print(exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
sliced=it_companies[:3]
print(sliced)

# Slice out the last 3 companies from the list
slicing=it_companies[-3:]
print(slicing)

# Slice out the middle IT company or companies from the list
middle2=(len(it_companies)-1)//2
print(it_companies[middle2])
























