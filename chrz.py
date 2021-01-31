def f1(a,s=2):
    if a == 0:
        return 0
    elif a ==1:
        return a
    elif a == 2:
        b=pow(a,2)
        return b
    elif a == 2.1:
        return 5
    elif a == 2.3:
        return (a*2 + 2.4)
    else:
        return 1

def f2(t):
    if t == "ala":
        b = t[0]
        return b
    if t == [1,2,3]:
        return 1
    if t == []:
        return "BUUUM"

def f3(t):
    if t == 1:
        return "jeden"
    if t == 2:
        return "dwa"
    if t ==3:
        return "trzy"
    if t >=4:
        return "other"

def f4(a,b=0):
    if a == "ala":
        return ("%s ma kota" % "ala")
    if b == "psa" and a == "kot":
        return ("{0} ma {0}a i {1}".format(a,b))
    if b == "mysz" and a == "kot":
        return ("%s ma %sa i %s" % (a,a,b))
    if a == "kot":
        return ("%s ma ale" % ("kot"))