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


(How I wrote this program)
- I started this project by watching all the lab videos and some rearches enhanced this project.



(References)

 1. https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
