# Jina Kim - G00353420
# Project for Grapy Theory Module in Year 3

class State:
    """A state with one or two edges, all edges labeled by label."""
    
    label = None  
    edges = None
    
    # Constructor to initialize the class variables 
    def __init__(self, label=None, edges=None):
        # Every state has 0, 1, or 2 edges from it. (max 2)
        self.edges = edges if edges else []
        # Label for the arrows. None means 'esilon.
        self.label = label

class Fragment:
    """An NFA fragment with a start state and an accept state."""
    
    start = None
    accept = None
    
    # Constructor to initialize the class variables   
    def __init__(self,start,accept):
        # Start state of NFA fragment
        self.start=start
        # Accept state of NFA fragment
        self.accept=accept

# Using shunting yeard algorithm
def shunt(infix):
    """Return the infix regular expression in postfix"""

    # Convert input to a stack-ish list
    infix = list(infix)[::-1]  # put "infix" into the list, [::-1] means it reverses the list

    # This array is used a stack
    opers=[] #Create empty stack named "opers"

    # Postfix regular expression
    # Output list
    postfix=[] # Create empty stack for postfix

    # Declare the operands,
    # Pprecedence setting 
    precedence={'(':1,')':2,'+':3,'|':4,'.':5,'*':6,'%':6,'/':6,'^':7} # create dictionary

    # Loop through the input one character at a time
    while infix:  # while there is still element in infix
    # Pop a character from the input 
        c=infix.pop()

        # Decide what to do based on the character
        # If the character is an '(', push it to stack
        if c=='(':
            # Push an open bracket to the opers stack
            opers.append(c)

        # If the scanned character is an ')', pop and  
        # output from the stack until and '(' is found 
        elif c==')':
            # Pop the operator stack until you find an (
            while opers[-1]!='(':
                postfix.append(opers.pop())

            # Get rid of the '('
            opers.pop()

        elif c in precedence:
            # Push any characters on the opers stack with higher prec to the output

            while opers and precedence[c]<precedence[opers[-1]]:
                postfix.append(opers.pop())

            # Push c to the operator stack
            opers.append(c)

        else:
            # Typically, we just push the character to the output
            postfix.append(c)

    # Pop all operators to the output
    while opers: #stack
        postfix.append(opers.pop())

    # Convert output list to String
    return ''.join(postfix)


# The main function that converts given infix expression to postfix expression 
def compile(infix):
    """Return an NFA fragment representing the infix regular expression."""

    # Convert infix to postfix.
    postfix=shunt(infix)
    # Make postfix a stack of characters.
    postfix=list(postfix)[::-1]

    # Keep track all of the fragment that you've created from the postfix
    # A stack for NFA fragment
    nfa_stack=[] 

    while postfix:
        # Pop a character from postfix
        c=postfix.pop()

        # Concatenation operator
        if c=='.':
            # Pop two fragment off the stack
            frag1=nfa_stack.pop()
            frag2=nfa_stack.pop()

            # Point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)

            # The new start state is frag2's
            start=frag2.start
            # The new accept state is frag1's
            accept=frag1.accept

        # OR opetator
        elif c=='|':
            #pop two fragment off the stack
            frag1=nfa_stack.pop()
            frag2=nfa_stack.pop()

            # Create new start and accept state
            accept=State()
            start=State(edges=[frag2.start, frag1.start])

            # Point the old accept states at the new one
            frag2.accept.edges.append(accept)
            frag1.accept.edges.append(accept)
                
        
        # Zero or more of a charactor
        elif c=='*':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()
            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])

            # Point the arrows
            frag.accept.edges = [frag.start, accept]

        # One or more of a charactor
        elif c=='+':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])

            # Point the arrows
            frag.accept.edges = [frag.start]

        # zero or one of a charactori
        elif c=='?':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])

            # Point the arrows
            frag.accept.edges = [frag.start, accept]
            
        elif c=='%':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            
             # Point the arrows
            frag.accept.edges = [frag.start, accept]
            
        elif c=='/':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            
            # Point the arrows
            frag.accept.edges = [frag.start, accept]
            
        elif c=='^':
            # Pop a single fragment off the stack
            frag = nfa_stack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])
            
            # Point the arrows
            frag.accept.edges = [frag.start, accept]
            

        else:
            accept = State()
            start = State(label=c, edges=[accept])

        # Create new instance of fragment to represent the new NFA
        newfrag=Fragment(start,accept)
        # Push the new NFA to the NFA stack
        nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()


#Add a state to a set, and follow all of the e(psilon) arrows
def followes(state, current):
    """Make current state to follow e arrows"""
    # Only do something when we haven't already seen the state
    if state not in current:
        # Put the state itself into current
        current.add(state)

        # See whether state is labelled by e(psilon)
        if state.label is None:
            #Loop through the states pointed to by this state
            for x in state.edges:
                # Follow all of their e(psilon)s too.
                followes(x,current)

def match(regex,string):#infix and string to match
    """Return true or false value depending on the match result"""

    #This function will return true if and only if the regular expression regex(fully)
    #mactches the string s. It returns false otherwise.

    #Compile the regular expression into an NFA
    nfa = compile(regex)

    # Try to match the regular expression to the string s.

    # The current set of states
    current = set()

    # Add the first state, and follow all e(psilon) arrows.
    followes(nfa.start, current)

    # The previous set of states
    previous = set()

    # Loop through characters in s(string)
    for c in string:
        # Keep track of where we were
        previous = current

        # Create a new empty set for states we are about to be in
        current = set()

        # Loop through the previous states.
        for state in previous:
            # Only follow arrows not labelled by e(psilon).
            if state.label is not None:
                # If the label of the state is equal to the character we have read.
                if state.label == c:
                    # Add the state at the end of the arrow to current
                    followes(state.edges[0], current)

    # Ask the NFA if matches the string s.
    # Return accept state in current states.
    return nfa.accept in current


def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

# Get Infix for a given postfix
# expression
def getInfix(exp) :

    s = []

    for i in exp:

        # Push operands
        if (isOperand(i)) :
            s.insert(0, i)

        # expect operator.
        else:

            op1 = s[0]
            s.pop(0)
            op2 = s[0]
            s.pop(0)
            s.insert(0, "(" + op2 + i +
                             op1 + ")")

    # There must be a single element in
    # stack now which is the required
    # infix.
    return s[0]



print("This is from",__name__)

# This will diaply in main ONLY(regex.py)
# Test if all functions work properly
if __name__ == "__main__":

    #Do multiple tests
    tests=[
        ["a.b|b*","bbbbbb",True],
        ["a.b|b*","bbbbbx",False],
        ["a.b","ab",True],
        ["b**","b",True],
        ["b*","",True],
        ["a.b.b.c","abbc",True],
        ["a.b.b.c","abc",False]

    ]

    for test in tests:
        assert match(test[0], test[1]) == test[2], test[0] + (" should " if test[2] else " should not ") +" match "+ test[1]
    
    
#Give option to the user
print("\n*****************Welcome*****************")
var = input("Press 1- to convert infix to postfix \nPress 2- to test your infix and postfix \nPress 3- to convert postfix to infix \nPress 4- to see examples\nPress 0- to exit\n ")
print("*****************************************")
num = int(var)

if num == 0:
   print("\nBye!") 
while(num != 0):

    # Just check what the postfix is from the user input(infix)
    if num==1:
        print("\nRead infix expression!")
        print("Supported characters : . , | , * , + , ? , \ , ^ , % ")
        #Take infix regular expression from the user input
        infixReg=input("Enter Infix expression : ")
        print("\n****Result****")
        print("\nPostfix expression is:  ",shunt(infixReg))

    # Compare user inputs(infix and postfix)
    elif num==2:
        print("Support characters : . , | , * ")
        #Take infix regular expression from the user
        regexes=input("\nEnter Infix expression :  ")

        #Take the string that the user wants to match
        stringToMatch=input("Enter the string that you want to match : ")

        #To print the result as True or False
        print("\n****Result****\n")
        print(match(regexes,stringToMatch),"\n")

    # Just check what the infix is from the user input(postfix)
    elif num==3:
        #Take postfix regular expression from the user input
        postfixReg=input("\nEnter Postfix expression :")
        print("\n****Result****")
        print("\nInfix expression is:  ",getInfix(postfixReg.strip())) 

    elif num==4:
        #Display examples
        print("\n****Result****")
        print("\n==Infix==                 ==Postfix==                      == Result==")
        print(" a.b|b*                     bbbbbb                           ",match("a.b|b*","bbbbbb"))
        print(" a.b|b*                     bbbbbx                           ",match("a.b|b*","bbbbbx"))
        print("  a.b                         ab                             ",match("a.b","ab"))
        print("  b**                         b                              ",match("b**","b"))
        print("  b*                                                         ",match("b*",""))
        print("a.b.b.c                      abbc                            ",match("a.b.b.c","abbc"))
        print("a.b.b.c                      abc                             ",match("a.b.b.c","abc"))
        print("(a|b).c*                     accccc                          ",match("(a|b).c*","accccc"))
        print("(a|b)*                       abababa                         ",match("(a|b)*","abababa"))


    else:
        print("\nNot a valid choice, try that again!")

    var = input("\nIf you want to continue, press 1 or 2 or 3 or 4, if not, press 0 to exit  :\n ")
    num = int(var)
    if num==0:
        print("Bye!")
