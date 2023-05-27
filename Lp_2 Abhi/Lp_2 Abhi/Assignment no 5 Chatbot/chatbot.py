def greet (bot_name, birth_year):
    print ("Hello! My name is {0}.".format (bot_name))
    print ("I was created in {0}.".format (birth_year))
   
def remind_name ():
    print ('Please, remind me your name.')
    name = input ()
    print ("What a great name you have, {0}!".format (name))
   
def guess_age ():
    print ('Let me guess your age.')
    print ('Enter remainders of dividing your age by 3, 5 and 7.')
 
 
    rem3 = int (input ())
    rem5 = int (input ())
    rem7 = int (input ())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
 
    print ("Your age is {0}; that's a good time to start programming!".format (age))
def count ():
    print ('Now I will count till the number you want.')
    num = int (input ())
   

    counter = 0
    while counter<=num:
        print ("{0} ".format (counter))
        counter += 1


def test ():
    print ("Let's test your programming knowledge.")
    print ("Why do we use methods?")
    print ("1. To repeat a statement multiple times.")
    print ("2. To decompose a program into several small subroutines.")
    print ("3. To determine the execution time of a program.")
    print ("4. To interrupt the execution of a program.")
   
   
    answer = 2
    guess = int (input ())
    while guess != answer:
        print ("Please, try again.")
        guess = int (input ())    
    print ('Correct!')
    print ('.................................')
def test1 ():
   
    print (" Which of the following is not a Java features?")
    print ("1. Dynamic")
    print ("2. Architecture Neutral")
    print ("3. Use of pointers")
    print ("4. Object-oriented")
   
   
    answer = 3
    guess = int (input ())
    while guess != answer:
        print ("Please, try again.")
        guess = int (input ())    
    print ('Correct!')
    print ('.................................')
  





def test2 ():
    print (" What does the expression float a = 35 / 0 return?")
    print ("1. 0")
    print ("2. Not a Number")
    print ("3. Infinity")
    print ("4. Run time exception")
   
   
    answer = 3
    guess = int (input ())
    while guess != answer:
        print ("Please, try again.")
        guess = int (input ())    
    print ('Correct!')
    print ('.................................')
    
def end ():
    print ('Congratulations, have a nice day!')
    print ('.................................')
    input ()

greet ('Helper Bot', '2023')
remind_name ()
guess_age ()
count ()
test ()
test1 ()
test2 ()

end ()
