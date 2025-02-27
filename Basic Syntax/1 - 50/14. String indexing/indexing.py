# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start: end : stop]

credit_number = "1234-5678-9012-3456"

print(credit_number[4])         #the first index is 0
print(credit_number[0:4])       #showing the numbers appearing from the indexes 1,2,3 and 4
print(credit_number[5:9])
print(credit_number[5:])        #showing from the 5th index to the end
print(credit_number[:9])        #showing from the beginning to the 9th index
print(credit_number[-1])        #negative numbers index from the back of the string
print(credit_number[::2])       #step field that make the string show everh 2nd character

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

credit_number = credit_number[::-1] #reversing the string
print(credit_number)

