## Task - 3 Password Generator

import random
import string
def main():
    length=int(input("Enter The Length of Password: "))
    lowerD=string.ascii_lowercase
    upperD=string.ascii_uppercase
    digitD=string.digits
    symbolsD=string.punctuation
    combine=lowerD + upperD + digitD + symbolsD
    x=random.sample(combine,length)
    password="".join(x)
    print(password)
    main()
main()