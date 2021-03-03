"""A collection of my functions for creating a bot that generates random passwords. I referenced https://pynative.com/python-generate-random-string/ to develop functions that would generate random strings and our A3 to create my bot. """

import random
import string

def password_generator_letters(length):
    """ Generates a random password with a mix of upper and lower case letters given a specific length.
    
    Parameters  
    ---------
    length : int
        The length of the password.
        
    Returns
    -------
    password : string
        The password generated.
    """
    
    letters = string.ascii_letters
    output = ''
    
    #generating random string from letters, code directly taken from https://pynative.com/python-generate-random-string/
    password = output.join(random.choice(letters) for i in range(length))
    
    return password


def password_generator_letters_and_numbers(length):
    """ Generates a random password containing both letters and digits 0-9 given a specific length.
    
    Parameters
    ----------
    length : int
        The length of the password.
    
    Returns
    -------
    password : string
        The password generated.
    """
    
    mix = string.ascii_letters + string.digits
    output = ''
    
    #generating random string from letters and digits
    password = output.join(random.choice(mix) for i in range(length))
    
    return password


def password_generator_letters_and_punctuation(length):
    """ Generates a random password containing both letters and punctuation given a specific length.
    
    Parameters
    ----------
    length : int
        The length of the password.
    
    Returns
    -------
    password : string
        The password generated.
    """
    
    mix = string.ascii_letters + string.punctuation
    output = ''
    
    #generating random string from letters and punctuation
    password = output.join(random.choice(mix) for i in range(length))
    
    return password


def password_generator_all(length):
    """Generates a random password containing both letters, digits, and punctuation given a specific length.
    
    Parameters
    ----------
    length : int
        The length of the password.

    Returns
    -------
    password : string
        The password generated.
    """
    
    mix = string.ascii_letters + string.digits + string.punctuation
    output = ''
    
    #generating random string from letters, digits, and punctuation
    
    
    return output.join(random.choice(mix) for i in range(length))


def greeting():
    """ Greets the user at the beginning. """
    
    print("Hello, would you like to create a password? Type yes or no.")

    
def wrong_answer(function):
    """Gives user another chance to fix answer if input was not originally "yes" or "no".
    
    Parameters
    ----------
    fuunction : string
        The function where the user input a wrong answer (either include_numbers or include_punctuation).
    
    Returns
    -------
    boolean
        Whether the user inputs "yes", "no", or a different response.
    """
    
    print("I don't understand. Please type yes or no.")
    msg = input()
    
    if msg.lower() == "yes":
        
        return True
    
    elif msg.lower() == "no":
        
        return False
    
    else:
        
        #print statement if the user does not put "yes" or "no"
        print("Do not understand input ):< ... " + function + " will not be added in the password.")
        
        return False

    
def password_length():
    """
    Determines the length of the password and gives different responses based on the user's input
    
    Returns
    -------
    boolean
        Returns False when input is 0 or not in the list of numbers.
        
    password_length, pass_length : int
        The input string converted to an integer.  
    """
    
    #list of numbers that the user may input
    list_of_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11'
                       '12', '13', '14', '15', '16', '17', '18', '19',
                       '20', '21', '22', '23', '24', '25', '26', '27']
    
    length = input("How long do you want your password?")
    
    if length == '0':
        
        #password will not be created if user wants the password to have a length of zero
        print("Okay.. I guess you didn't want a password ):")
        
        return False
    
    elif length in list_of_numbers:
        
        #string response converts to int if in list of numbers
        password_length = int(length)
        
        return password_length
    
    else:
        
        #gives user another chance to input response that is in list of numbers
        print("Please input a number.")
        msg = input()
        
        if msg == '0':
            
            #password will not be created if msg is zero
            print("No password can be created with a length of zero ):<")
            
            return False
        
        elif msg in list_of_numbers:
            
            #string response converts to int if in list of numbers
            pass_length = int(msg)
            
            return pass_length
        
        else:
            
            #password will not be created
            print("Do not understand input. No password will be created. ")
            
            return False

        
def include_numbers():
    """
    Determines if there will be numbers in the password.
    
    Returns
    -------
    boolean
        Whether the user inputs "yes" or "no"
    
    option : boolean
        Calls the wrong_answer function
    """
    
    msg = input("Do you want numbers in your password? Type yes or no. ")
    
    if msg.lower() == "yes":
        
        return True
    
    elif msg.lower() == "no":
        
        return False
    
    else:
        
        #use wrong_answer function if msg is not "yes" or "no"
        option = wrong_answer("numbers")
        
        return option
        
    
def include_punctuation():
    """
    Determines if there will be punctuation in the password.
    
    Returns
    -------
    boolean
        Whether the user inputs "yes" or "no"
    
    option : boolean
        Calls the wrong_answer function
    """
    
    msg = input("Do you want punctuation in your password? Type yes or no. ")
    
    if msg.lower() == "yes":
        
        return True
    
    elif msg.lower() == "no":
        
        return False
    
    else:
        
        #use wrong_answer function if msg is not "yes" or "no"
        option = wrong_answer("punctuation")
        
        return option

    
def generate_password(length, choices):
    """
    Generates a password based on whether the user wanted digits and punctuation in password.
    
    Parameters
    ----------
    length : int
        The length of the password
    
    choices : list
        The list of choices of whether there will be digits and punctuation in the password.
    
    Returns
    -------
    output : string
        The password generated.
    """
    
    if choices == [length, True, True]:
        
        #generate password with letters, digits, and punctuation
        output = password_generator_all(length)
        
        return output
                
    elif choices == [length, True, False]:
        
        #generates password with letters and digits
        output = password_generator_letters_and_numbers(length)
        
        return output
                
    elif choices == [length, False, True]:
        
        #generates password with letters and punctuation
        output = password_generator_letters_and_punctuation(length)
        
        return output
                
    elif choices == [length, False, False]:
        
        #generates password with letters
        output = password_generator_letters(length)
        
        return output

    
def password_creator():
    """Creates a bot that generates a password. """
    
    chat = True
    
    while chat:
        
        #use greeting function to greet user
        greeting()
        msg = input()
        output = None
        
        #moves on to ask about password if msg is "yes"
        if msg.lower() == "yes":
            
            length = password_length()
            
            #generates password if length is integer
            if type(length) == int:
                
                #user decides if numbers will be in password
                want_numbers = include_numbers()
                
                #user decides if punctuation will be in password 
                want_punctuation = include_punctuation()
                
                #creates a list of choices of the user
                choice_list = [length, want_numbers, want_punctuation]
                
                #generates password based on choices
                output = "Your password is " + generate_password(length, choice_list)
                
                #ends chat after password created
                chat = False
             
            #the chat closes if the user does not give a length
            elif length == False:
                
                output = "Goodbye."
                chat = False
        
        #ends chat if msg is "no"
        elif msg.lower() == "no":
            
            output = "Okay... goodbye ):"
            chat = False
        
        #ends chat if msg is not "yes" or "no"
        else:
            
            output = "Do not understand input. Password will not be created."
            chat = False
            
        print(output)
