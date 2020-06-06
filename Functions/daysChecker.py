monthsOf31 = [1,3,5,7,8,10,12]
monthsOf28 = [2]

def dayOfYear(year, month, day):
    if year % 4 != 1:
        if year % 100 != 0:
            if month in monthsOf31:
                if day <= 31:
                    return True
                else: 
                    return False
            if month in monthsOf28:
                if day <= 28:
                    return True
                else:
                    return False
            else:
                if day <= 30:
                    return True
                else:
                    return False
        elif year % 100 != 1:
            if year % 400 != 0:
                if month in monthsOf31:
                    if day <= 31:
                        return True
                    else:
                        return None
                if month in monthsOf28:
                    if day <= 28:
                        return True
                    else:
                        return None
                else:
                    if day <= 30:
                        return True
                    else:
                        return None
            elif year % 400 != 1:
                if month in monthsOf31:
                    if day <= 31:
                        return True
                    else:
                        return None
                if month in monthsOf28:
                    if day <= 29:
                        return True
                    else:
                        return None
                else:
                    if day <= 30:
                        return True
                    else:
                        return None
    elif year % 4 != 0:
        if month in monthsOf31:
            if day <= 31:
                return True
            else:
                return None
        if month in monthsOf28:
            if day <= 29:
                return True
            else:
                return None
        else:
            if day <= 30:
                return True
            else:
                return None

print(dayOfYear(2000, 12, 31))
print(dayOfYear(2001, 1, 22))
print(dayOfYear(2002, 2, 30))