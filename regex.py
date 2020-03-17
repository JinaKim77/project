# Jina Kim
# Classes used in Thompson's construction

class State:
    #Every state has 0,1, or 2 edges from it.
    edges =[]

    # Label for the arrows. None means epsilon.
    label=None

    # Constructor for the class
    def __init__(self, label=None, edges=[]):
        self.edges=edges
        self.label=label

class Fragment:
    # Start status of NFA fragment
    start=None

    # Accept state of NFA fragment
    accept=None

    #Constructor
    def __init__(self,start,accept):
        self.start=start
        self.accept=accept


def shunt(infix):
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

            while opers and prec[c]<prec[opers[-1]]:
                postfix.append(opers.pop())

            #Push c to the operator stack
            opers.append(c)

        else:
            #Typically, we just push the character to the output
            postfix.append(c)

            #Pop all operators to the output
    while opers:
        postfix.append(opers.pop())

    #Convert output list to String
    return ''.join(postfix)

    #Print the result
    #print("Ooutput is:", postfix)



def compile(infix):

    postfix=shunt(infix)
    postfix=list(postfix)[::-1]

    # Keep track all of the fragment that you've created from the postfix
    nfa_stack=[] 

    while postfix:
        # Pop a character from postfix
        c=postfix.pop()

        if c=='.':
            # Pop two fragment off the stack
            frag1=nfa_stack.pop()
            frag2=nfa_stack.pop()

            # Point frag2's accept state at frag1's start state
            frag2.accept.edges.append(frag1.start)

            # Create new instance of fragment to represent the new NFA
            newfrag=Fragment(frag2.start, frag1.accept)
            
            #Push the new NFA to the NFA stack
            nfa_stack.append(newfrag)


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

            # Create new instance of fragment to represent the new NFA
            newfrag=Fragment(start,accept)
                
            # Push the new NFA Stack
            nfa_stack.append(newfrag)


        elif c=='*':
            # Pop a single fragment off the stack
            frag=nfa_stack.pop()
            # Create new start and accept states
            accept =State()
            start =State(edges=[frag.start, accept])

            # Point the arrows
            frag.accept.edges.append(frag.start)
            frag.accept.edges.append(accept)

            # Create new instance of fragment to represent the new NFA
            newfrag=Fragment(start,accept)

            # Push the new NFA stack
            nfa_stack.append(newfrag)


        else:
            accept=State()
            start=State(label=c, edges=[accept])

            # Create new instance of fragment to represent the new NFA
            newfrag=Fragment(start,accept)
                
            # Push the new NFA Stack
            nfa_stack.append(newfrag)

    # The NFA stack should have exactly one NFA on it.
    return nfa_stack.pop()

#Add a state to a set, and follow all of the e(psilon) arrows
def followes(state, current):
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

def match(regex,s):
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

    # Loop through characters in s.
    for c in s:
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

    #Ask the NFA if matches the string s.
    return nfa.accept in current

#Take value from the user
regex = input("Enter your value: ")  

#Take expected value from the user.
stringToMatch = input("Enter the string to be checked:  ");

#To print the result True or False
print(match(regex,stringToMatch))







