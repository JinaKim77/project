# project

Program in Python to execute regular expressions on
strings using an algorithm known as Thompson’s construction.

   (Convert infix expression to postfix expression using Shunting yard algorithm)

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


User guide
When running the program, the user gets a list of menu options. To select a menu option, enter the corresponding number for the user preference.
![](images/mainmenu.PNG)
 option 1. This allows the user enter infix regular expression and this program will output post regular expression
          (This wasn't what the project asked for, but I just added for the user preference)
![](images/option1.PNG)
 option 2. This allows the user enter infix and postfix regular expression and this program check if they are matched or not.
![](images/option2.1.PNG)
![](images/option2.2.PNG)
 option 3. This allows the user enter postfix regular expression and this program will output infix regular expression
          (This wasn't what the project asked for, but I just added for the user preference)
![](images/option3.PNG)        
 option 0. To exit 
![](images/option0.PNG)   
 
 When the user enter invalid input, this message will display.
 ![](images/invalidInput.PNG)  
 
 
 
 
 


(References)
 1. https://www.w3schools.com/python/python_regex.asp
 2. https://realpython.com/    
 3. https://www.geeksforgeeks.org/infix-to-postfix-using-different-precedence-values-for-in-stack-and-out-stack/?ref=rp
 4. https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
 
