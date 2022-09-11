import json

#Program 1
def ends_of_string(str):
    if len(str) < 2:
        return 'The string is too short.'
    return str[0:2] + str[-2:]

#Program 2
def multiples():
    num1 = int(input("Please enter first number: "))
    num2 = int(input("Please enter second number: "))
    for i in range(num1, num2+1):
        if i % 7 == 0:
            if i % 5 != 0:
                print(i,end="")
                if num2 - i >= 7:
                    print(end=",")
    print()

#Program 3
def add_dict():
    str = input("Input first dictionary: ")
    dict1 = string_to_dict(str)
    str = input("Input second dictionary: ")
    dict2 = string_to_dict(str)
    dictR = {}
    for key in dict1:
        if key in dict2:
            dictR[key] = dict1[key] + dict2[key]
        else:
            dictR[key] = dict1[key]
    for key in dict2:
        if key not in dict1:
            dictR[key] = dict2[key]
    return dictR

def string_to_dict(str):
    dict = {}
    ind1 = str.find("'")
    while ind1 != -1:
        ind2 = str.find("'",ind1+1)
        item = str[ind1+1:ind2]
        ind1 = str.find(":",ind2+1)
        ind2 = str.find(",",ind1+1)
        if ind2 == -1:
            ind2 = len(str) - 1
        key = int(str[ind1+1:ind2])
        dict[item] = key
        ind1 = str.find("'",ind2+1)
    return dict

#Program 4
def price_order():
    numItem = int(input("Number of items: "))
    itemList = []
    for i in range(numItem):
        itemList.append(input("Input item and price: "))
    swapped = True
    while(swapped):
        swapped = False
        firstItem = itemList[0]
        highNum = int(firstItem[first_int(firstItem)])
        for i in range(1,len(itemList)):
            item = itemList[i]
            itemPrice = int(item[first_int(item)])
            if(highNum > itemPrice):
                swapped = True
                tempItem = itemList[i-1]
                itemList[i-1] = item
                itemList[i] = tempItem
            else:
                highNum = itemPrice
    for i in itemList:
        print(i)


def first_int(str):
    for i in str:
        if i.isdigit():
            return str.find(i)
    return -1

#Program 1 Tests
string = input("Enter your string:")
stringresult = ends_of_string(string)
print(stringresult)

#Program 2 Tests
multiples()

#Program 3 Tests
dict = add_dict()
print(dict)

#Program 4 Tests
price_order()