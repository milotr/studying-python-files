def mysplit(strng):
    list = []
    while 1:
        for i in strng:
            list.append(i)
        return list


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))