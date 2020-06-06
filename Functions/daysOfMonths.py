
monthsOf31 = [1,3,5,7,8,10,12]
monthsOf28 = [2]

def daysInMonth(year, month):
	#even by 4
    if year % 4 != 1:
		#odd by 100
        if year % 100 != 0:
            if month in monthsOf31:
                return 31
            if month in monthsOf28:
                return 28
            else:
                return 30 
        elif year % 100 != 1:
            if year % 400 != 0:
                if month in monthsOf31:
                    return 31
                if month in monthsOf28:
                    return 28
                else:
                    return 30
            elif year % 400 != 1:
                if month in monthsOf31:
                    return 31
                if month in monthsOf28:
                    return 29
                else:
                    return 30
    elif year % 4 != 0:
        if month in monthsOf31:
            return 31
        if month in monthsOf28:
            return 29
        else:
            return 30

testYears = [1900, 2000, 2016, 1987]
testMonths = [2, 2, 1, 11]
testResults = [28, 29, 31, 30]
for i in range(len(testYears)):
	yr = testYears[i]
	mo = testMonths[i]
	print(yr, mo, "->", end=" ")
	result = daysInMonth(yr, mo)
	if result == testResults[i]:
		print("OK")
	else:
		print("Failed")