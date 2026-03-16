def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def has_twoletters(s):
    c1,c2=s[0],s[1]
    if not c1.isalpha() or not c2.isalpha():
       return False                                             
    else:
        return True


def middle_number(s):
    for char in s:
        if char.isdigit() and char !="0":
            if s[s.index(char):].isdigit():
                return True
            else:
                return False
        elif char.isdigit() and char=="0":
            return False
    return True


def has_spchars(s):
    c=0
    for i in s:
        if not i.isalnum():
            c+=1
        else:
            continue
    if c!=0:
        return False
    else:
        return True


def is_valid(s):
    if 2<=len(s)<=6 and has_twoletters(s) and has_spchars(s) and middle_number(s):
        return True
    else:
        return False

if __name__=="__main__":
    main()
