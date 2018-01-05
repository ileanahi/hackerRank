if __name__ == '__main__':
    s = raw_input()
    alnumRes = False
    alphaRes = False
    digitRes = False
    lowerRes = False
    upperRes = False

    for i in s:
        if i.isalnum() == True:
            alnumRes = True
        if i.isalpha() == True:
            alphaRes = True
        if i.isdigit() == True:
            digitRes = True
        if i.islower() == True:
            lowerRes = True
        if i.isupper() == True:
            upperRes = True

    print alnumRes
    print alphaRes
    print digitRes
    print lowerRes
    print upperRes
