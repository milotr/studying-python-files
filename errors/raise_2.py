def badFun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        #re-raise the error again
        raise

try:
    badFun(0)
#the error comes here which prints "I see"
except ArithmeticError:
    print("I see!")

print("THE END.")

#The instruction will immediately
#  re-raise the same exception as currently handled.


#REMEMBER:
#this kind of raise instruction may be used 
#
#-----------INSIDE THE EXCEPT BRANCH ONLY------------
# 
# sing it in any other 
#context causes an error.