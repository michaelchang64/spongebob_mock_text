import sys, random

def mockText(str):
    # iterate through string str and randomly capitalize text
    newStr = ""
    for i in range(0, len(str)):
        # get random float between 0 and 1.0, inclusive
        n = random.random()
        # two routes: if character is uppercase, see if lowercase, and vice versa
        # given random number, if n >= 0.5 then uppercase, else retain case
        if str[i].islower():
            if n >= 0.56:
                newStr += str[i].upper()
            else:
                newStr += str[i]
        else:
            if n >= 0.54:
                newStr += str[i].lower()
            else:
                newStr += str[i]
    return newStr

def main():
    for arg in sys.argv[1:]:
        print(mockText(arg))

if __name__ == "__main__":
    main()
