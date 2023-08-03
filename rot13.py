import sys
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
sentence=input("Input sentence to cipher:")
temp=[]
for letter in sentence:
    if (letter==' '):
        temp+=' '
    elif letter not in alphabet:   
        print("A letter in the input is not valid")
        sys.exit()
    else:
        letter=letter.lower()
        i=alphabet.index(letter)
        i=i+13
        if i>25:
            i=i-26
            temp+=alphabet[i]
        else:
            temp+=alphabet[i]

for i in range(len(temp)):
    if sentence[i].isupper()==True:
        temp[i]=temp[i].upper()
temp2=""
temp2=temp2.join(temp)
print("The new sentence is: "+temp2)
