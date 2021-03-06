# Jina Kim - G00353420
# Project for Grapy Theory Module in Year 3

# import the necessary packages
import argparse
import sys


# Define the program description
text = 'Program in Python _to execute regular expressions on strings using an algorithm known as Thompson’s construction. Thompsons" construction is used to convert a regular expression to a NFA. This NFA is then used to match a String against the original regular expression. The main goal of this project is to accept a regular expression with the special characters to match it against an input string from the user. '

guide = 'When running the program, you get a list of menu options. To select a menu option, enter the corresponding number for the user preference.'

#Initiate the parser
#parser = argparse.ArgumentParser(description=text) # display description of this program
parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="show program version", action="store_true") # display program version
parser.add_argument("-D", "--description", help="show program description", action="store_true")
parser.add_argument("-T", "--howtorun", help="show how to run this prgram", action="store_true")
parser.add_argument("-R", "--regex" , help="explain what the regular expression is", action="store_true")

#Read arguments from the command line
#parser.parse_args()
args = parser.parse_args()

# Check for --version or -V
if args.version:
    print("This is my program version 0.1")

# Check for --description or -D
if args.description:
    print(text)

# Check for --howtorun or -T
if args.howtorun:
    print(guide)
    print("option 1. This allows the user enter infix regular expression and this program will output post regular expression")
    print("option 2. This allows the user enter infix and postfix regular expression and this program check if they are matched or not.")
    print("option 3. This allows the user enter postfix regular expression and this program will output infix regular expression")
    print("option 4. This allows the user to see examples of output")
    print("option 0. This allows the user to exit the program")

# Check for --regex or -R   
if args.regex:
    print("A regular expression is a special sequence of characters that helps you match or find other strings or sets of strings, using a specialized syntax held in a pattern. Regular expressions are widely used in UNIX world. The Python module re provides full support for Perl-like regular expressions in Python.")

#This displays the regular expression special charaters for the user before using the program.
group1 = parser.add_argument_group('Regular Expression', 'The special characters are:')
group1.add_argument('a.b', help='a followed by b')
group1.add_argument('a*',help='any number of a"s, zero or more, a* will match either empty string or a....') 
group1.add_argument('a|b',help='an a or a b')
group1.add_argument('+',help='Causes the resulting RE to match 1 or more repetitions of the preceding RE. a+ will match either a or aaaa...')
group1.add_argument('?',help='Causes the resulting RE to match 0 or 1 repetitions of the preceding RE. b? will match either empty string or b')

parser.print_help() 

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

# NFA
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
            # Join the new start state to NFA's start state
            start = State(edges=[frag.start])

            # Point the arrows
            frag.accept.edges = [frag.start, accept]

        # zero or one of a charactori
        elif c=='?':
            # Pop a single fragment off the stack
            frag= nfa_stack.pop()

            # Create new start and accept states
            accept = State()
            start = State(edges=[frag.start, accept])

            # Point the arrows
            frag.accept.edges = [accept]
            
        

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
        ["a.b.b.c","abc",False],
        ["(a.b*)","abbb",True],
        ["(11)*","",True],
        ["(11)*","1111",True],
        ["(a+b)*","bbbb",True],
        ["(a+b)*","",True],
        ["a|b*","a",True],
        ["a|b*","aa",False],
        ["(a|b)*","aa",True],
        ["a?","a",True],
        ["a?","aa",False],
        ["b+","",False],
        ["b+","b",True],
        ["b+","bbbb",True]
    ]

    for test in tests:
        assert match(test[0], test[1]) == test[2], test[0] + (" should " if test[2] else " should not ") +" match "+ test[1]
    
    
#Give option to the user
print("\n******************************Welcome*******************************")
print("Please choose from one of the following options: ")
var = input("Press 1- to convert infix to postfix \nPress 2- to check matches between your infix and postfix \nPress 3- to convert postfix to infix \nPress 4- to see examples\nPress 0- to exit\n ")
print("**********************************************************************")
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
        print("Support characters : . , | , * , ? , + ")
        #Take infix regular expression from the user
        regexes=input("\nEnter Infix expression that you want to string to be checked:  ")

        #Take the string that the user wants to match
        stringToMatch=input("Enter the string that you want to match a regular expression : ")

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
        print("\n*******************************Result*********************************\n")
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
        print("(a.b*)                       a                               ",match("(a.b*)","a"))
        print("(a.b*)                       abbb                            ",match("(a.b*)","abbb"))
        print("(a.b*)                       ba                              ",match("(a.b*)","ba"))
        print("(11)*                        1111                            ",match("(11)*","1111"))
        print("(11)*                                                        ",match("(aa)*",""))
        print("(a+b)*                       bbbb                            ",match("(a+b)*","bbbb"))
        print("(a+b)*                                                       ",match("(a+b)*",""))
        print("a|b*                         a                               ",match("a|b*","a"))
        print("a|b*                         b                               ",match("a|b*","b"))
        print("a|b*                         bbbb                            ",match("a|b*","bbbb"))
        print("a|b*                                                         ",match("a|b*",""))
        print("a|b*                         aa                              ",match("a|b*","aa"))
        print("(a|b)*                       aa                              ",match("(a|b)*","aa"))
        print("a?                                                           ",match("a?",""))
        print("a?                           a                               ",match("a?","a"))
        print("a?                           aa                              ",match("a?","aa"))
        print("b+                                                           ",match("b+",""))
        print("b+                           b                               ",match("b+","b"))
        print("b+                           bbbb                            ",match("b+","bbbb"))
        print("\n\n*********************************************************************\n") 
    else:
        print("\nNot a valid input, Please try again!")

    var = input("\nIf you want to continue, press 1 or 2 or 3 or 4, if not, press 0 to exit  :\n ")
    num = int(var)
    if num==0:
        print("Bye!")

