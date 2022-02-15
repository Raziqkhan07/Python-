lis=[122,10,0,'a',200,-10,1,"Hello"]
for i in lis:
    print("inputs are:",i,end='\n')
    # i=i+1
    # print("After", i / 10)
try:
    for i in lis:
        print(i,end='\t')
        # i=i+1
        print(" : After: \n",i/10)
        raise ZeroDivisionError(i)
        raise TypeError(i)

except SyntaxError:
    print("Syntax Error")
except ValueError:
    print("Value Error")
except IndexError:
    print(" Index Error")
except TypeError:
    print(i,"  Type Error")
except ZeroDivisionError:
    print(i,"Zero Error")
except:
    ("unknow Error")
