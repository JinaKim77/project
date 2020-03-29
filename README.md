# Graph theory project

**Program in Python _to execute regular expressions_ on
strings using an algorithm known as Thompson’s construction.**

### Convert infix expression to postfix expression using Shunting yard algorithm

1. Scan the infix expression from left to right.
2. If the scanned character is an operand, output it.
3. Else,
        3.1 If the precedence of the scanned operator is greater than the precedence of the operator in the stack(or the stack is empty or the stack contains a ‘(‘ ), push it.
        3.2 Else, Pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator. After doing that Push the scanned operator to the stack. 
         (If you encounter parenthesis while popping then stop there and push the scanned operator in the stack.)
4. If the scanned character is an ‘(‘, push it to the stack.
5. If the scanned character is an ‘)’, pop the stack and and output it until a ‘(‘ is encountered, and discard both the parenthesis.
6. Repeat steps 2-6 until infix expression is scanned.
7. Print the output
8. Pop and output from the stack until it is not empty.


The program will ask the user if they want to...
     1. ..get postfix expression from the user input ( infix expression )  or
     2. ..test if the user's inputs are matched ( the user's input will be both infix and postfix expression)

(The user can just type infix regular expression to get porstfix regular expression, 
 or
 the user can type both infix expression and postfix expression to test if they are matched.

# How to get postfix from infix expression
<p>
<img src="Images/IMG_20200329_131743.jpg" width="600" >
</p>


# User guide
### When running the program, the user gets a list of menu options. To select a menu option, enter the corresponding number for the user preference.
<p>
<img src="Images/mainmenu.PNG" width="600" >
</p>

 ### option 1. This allows the user enter infix regular expression and this program will output post regular expression
          (This wasn't what the project asked for, but I just added for the user preference)
          
<p>         
<img src="Images/option1.PNG" width="700" >
</p>

 ### option 2. This allows the user enter infix and postfix regular expression and this program check if they are matched or not.
 
<p>
 <img src="Images/option2.1.PNG" width="700" >
</p>

<p>
 <img src="Images/option2.2.PNG" width="700" >
</p>

 ### option 3. This allows the user enter postfix regular expression and this program will output infix regular expression
          (This wasn't what the project asked for, but I just added for the user preference)
          
<p>
<img src="Images/option3.PNG" width="700" >       
</p>

 ### option 0. To exit 

<p>
<img src="Images/option0.PNG" width="700" > 
</p>
 
 ### When the user enter invalid input, this message will display.

<p>
 <img src="Images/invalidInput.PNG" width="700" >
</p>
 


# References
 - https://www.w3schools.com/python/python_regex.asp
 - https://realpython.com/    
 - https://www.geeksforgeeks.org/infix-to-postfix-using-different-precedence-values-for-in-stack-and-out-stack/?ref=rp
 - https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
 
