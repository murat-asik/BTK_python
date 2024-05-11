"""
1- Create a variable for the following information of a customer.

Customer name
Customer last name
Customer name + surname
Customer gender
Customer TR ID
Customer birth year
Customer address information
Customer age

"""


customerName = "Sabiha"
customerLastName = "Gökçen"
customerNameLastName = customerName+ " " +customerLastName 
customerGender = True #Women
customerId = "84679513475"
CustomerBirthDay = 1904
customerAddress= "Bahçeşehir"
customerAge = 2020 - CustomerBirthDay



"""
2- Calculate the total information of the following orders.

Order 1 => 110 TL
Order 2 => 1100.5 TL
Order 3 => 356.95 TL

"""

order1 = 110 
order2 = 1100.5
order3 = 356.95
total = order1 + order2 + order3
print("Total:", total)