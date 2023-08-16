import os


def toFourDigit(number):
    number = str(number)
    digits = len(number)

    if digits == 1:
        number = "000" + number
    elif digits == 2:
        number = "00" + number
    elif digits == 3:
        number = "0" + number

    return number

def sortNumber(number):
    smallNumber = None
    bigNumber = None
    listNumber = None

    listNumber = list(number)
    listNumber = sorted(listNumber, key= int)

    smallNumber = "".join(listNumber)
    bigNumber = "".join(reversed(listNumber))

    result = int(bigNumber) - int(smallNumber)
    return result

def createFile(name, link):
    name = name + ".md"
    file = os.path.join("output/", name)

    with open(file, "w") as f:
        f.write("[[" + link + "]]")
        f.close()


for i in range(9999):
    if i <= 999:
        i = toFourDigit(i)
    else:
        i = str(i)

    link = toFourDigit(str(sortNumber(i)))

    createFile(i, link)