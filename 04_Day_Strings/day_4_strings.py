#Day 4 Excerises
#1
given_list = ['Thirty', 'Days', "Of", "Python"]
print("#1"," ".join(given_list))

#2
given_list_2 = ["Coding", "For", "All"]
print("#2"," ".join(given_list_2))

#3
company = "Coding For All"

#4
print("#4",company)

#5
print("#5",len(company))

#6
print("#6",company.upper())

#7
print("#7",company.lower())

#8
print("#8",company.capitalize(), company.title(), company.swapcase())

#9
start = company.find("Coding")
end = start + len("Coding")
print("#9",company[end::].strip())

#10
doesContain = company.__contains__("Coding")
print("#10",doesContain)

#11
replaced_string = company.replace("Coding For All", "Python")
print("#11",replaced_string)

#12
start_string = "Python for Everyone"
new_string = start_string.replace("Everyone","All")
print("#12",new_string)

#13
print("#13",company.split(" "))

#14
fang = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print("#14", fang.split(","))

#15
print("#15",company[0])

#16
print("#16",company[-1])

#17
print("#17",company[10])

#18
def acronym_maker(string):
    acronym = ""
    word_list = string.split()
    for word in word_list:
        first_letter = word[0]
        acronym += first_letter
    
    return acronym

print("#18", acronym_maker(start_string))

#19
print("#19", acronym_maker(company))

#20
print("#20", "Coding For All".index('C'))

#21
print("#21", "Coding For All".index('F'))

#22
print("#22", "Coding For All".rfind('I'))

#23
test_sentence = 'You cannot end a sentence with because because because is a conjunction'
print("#23", test_sentence.index('because'))

#24
print("#24", test_sentence.rindex('because'))

#25
index_start = test_sentence.find("because because because")
index_end = index_start + 23 #length of phrase including two spaces
first_half = test_sentence[0:index_start - 1]
second_half = test_sentence[index_end::]
print("#25", first_half + second_half)

#26
print("#26", test_sentence.find("because"))

#27 Same as #25???

#28
print("#28", company.startswith("Coding"))

#29
print("#29", company.endswith("coding"))

#30
thirty_string = '   Coding For All      ' 
print("#30", thirty_string.strip(" "))

#31   the one with the written out thirty returns true
print("#31", "30DaysOfPython".isidentifier(), "thirty_days_of_python".isidentifier())

#32
simple_list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print("#32", "# ".join(simple_list))

#33 #its a forward slash!!!!
print('I am enjoying this challenge. \nI just wonder what is next.')

#34
print("Name\tAge\tCountry\tCity\nAsabeneh\t250\tFindland\tHelsinki")

#35
