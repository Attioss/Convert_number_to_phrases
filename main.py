
#fundamental building blocks
pairs = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
             6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety', 0: 'zero'}

n = int(input())
# this lines spare the input number into number triplets
num_millions = n//1000000
num_thousands = (n-num_millions*1000000)//1000
num_under1000 = n-num_millions*1000000-num_thousands*1000
list = []
# this lines append triplets to the list if they are greater than 0
if num_millions > 0:
    list.append(num_millions)
if num_thousands > 0:
    list.append(num_thousands)
list.append(num_under1000)
print(list)
# this is the list which can provide final results
res_list = []
# this for cycle iterating the list to transform triplets into words and append it to the res_list
for num in list:
    hundreds = num//100
    if hundreds > 0:
        under100 = num-(num//100)*100
        if under100 > 0:
# the following lines deciede the number is between 10-20 or greater than 20
            if under100 % 10 != 0:
                res = (pairs[hundreds] + " " + "hundred and " + pairs[under100 - under100 % 10] + "-" + pairs[under100 % 10])
                res_list.append(res)
            else:
                res = (pairs[hundreds] + " " + "hundred and " + pairs[under100])
                res_list.append(res)
        else:
            res = (pairs[hundreds] + " " + "hundred")
            res_list.append(res)
# the following lines contain debugging to avoid errors if numbers are less than 100
    else:
        under100 = num
        if under100 < 20:
            res = (pairs[under100])
            res_list.append(res)
        else:
            if under100 % 10 != 0:
                res = (pairs[under100 - under100 % 10] + "-" + pairs[under100 % 10])
                res_list.append(res)
            else:
                print(under100)
                res = (pairs[under100])
                res_list.append(res)
print(res_list)

# debugging: program did not accept value under 1 million

if n > 999999:
    # this is debugging to avoid the result something + zero
    if int(list[1]) > 0 and 100 > int(list[2]) > 0:
        print(res_list[0], "million", res_list[1], "thousand", "and", res_list[2])
    elif int(list[1]) > 0 and int(list[2]) > 99:
        print(res_list[0], "million", res_list[1], "thousand", res_list[2])
    elif int(list[1]) > 0 and int(list[2]) == 0:
        print(res_list[0], "million", res_list[1], "thousand")
    elif int(list[1]) == 0 and 100 > int(list[2]) > 0:
        print(res_list[0], "million", res_list[2])
    elif int(list[1]) == 0 and int(list[2]) > 99:
        print(res_list[0], "million", "and", res_list[2])
    else:
        print(res_list[0], "million")
elif 999 < n < 1000000:
    if 100 > int(list[1]) > 0:
        print(res_list[0], "thousand", "and", res_list[1])
    elif int(list[1]) > 99:
        print(res_list[0], "thousand", res_list[1])
    else:
        print(res_list[0], "thousand")
else:
    print(res_list[0])

