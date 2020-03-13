#Jina Kim
#The shunting year algorithm for regular expression

#The input
infix="(a|b).c*"
print("The input is: ",infix)
#Expected output is : "ab|c*."

#Convert input to a stack-ish list
infix = list(infix)[::-1]
# put "infix" into the list, [::-1] means it reverses the list

#Operator stack
opers=[] #Create empty stack named "opers"

#Output list
postfix=[] #Create empty stack for postfix

#Operator precedence
prec={'*':100, '.':80, '|':60, ')':40, '(':20} # create dictionary

#Loop through the input one character at a time
while infix:  #while there is still element in infix
    #Pop a character from the input 
    #Remove last element from the list
    c=infix.pop()

    #Decide what to do based on the character
    if c=='(':
        #Push an open bracket to the opers stack
        opers.append(c)

    elif c==')':
        #Pop the operator stack until you find an (
        while opers[-1]!='(':
            postfix.append(opers.pop())

        #Get rid of the '('
        opers.pop()

    elif c in prec:
        #Push any characters on the opers stack with higher prec to the output

        while opers and  prec[c]<prec[opers[-1]]:
            postfix.append(opers.push())                 

        #Push c to the operator stack
        opers.append(c)

    else:
        #Typically, we just push the character to the output
        postfix.append(c)

#Pop all operators to the output
while opers:
    postfix.append(opers.pop())

#Convert output list to String
postfix = ''.join(postfix)

#Print the result
print("Ooutput is:", postfix)





                     
