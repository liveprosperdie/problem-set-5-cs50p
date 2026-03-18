def main():
    p=convert(input("Fraction: "))
    s=gauge(p)
    print (s)


def convert(frac):
    x,y= frac.split("/")
    x,y=int(x),int(y)
    if y==0:
        raise ZeroDivisionError
    if x>y or x<0 or y<0:
        raise ValueError
    p=round((x/y)*100)
    return p


def gauge(percent):
    if percent<=1:
        return "E"
    elif percent>=99:
        return "F"
    else:
        return f"{percent}%"


if __name__=="__main__":
    main()