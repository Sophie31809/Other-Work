operators = ['+', '-', 'x', '/' ,'^'] #create a list of accepted operators
#defining the booleans for the while loops
choice_option = True
calculator = True
file_name = True
while choice_option == True:
    choice = input("Would you like to enter a calculation (0) or read previous calculations from a text file (1)? ")
    #if calculator selected, go into calculator while loop
    if choice == '0':
        while calculator == True:
            calculation = input("""Please enter the calculation using two numbers and one of the following operators:
        +, -, x, /, ^
            :""")
            for o in operators:
                if o in calculation:
                    #will split the input into the first and second numner (the phrases either side of the operator)
                    calculation_list = calculation.split(o)
                    #anticipate that users might enter more than one operator, or incorrect operators, or other characters other than those accepted
                    try:
                        #try turning the phrases either side of the operator to floats - if this doesn't work, an incorrect character has been entered
                        first_number = float(calculation_list[0])
                        second_number = float(calculation_list[1])
                        #open the file to write the result to 
                        f = open('calculator_result.txt', 'a')
                        #go through the accepted operators. perform the desired calcuation, and print the result as well as writing it to the file. 
                        if o == '+':
                            print(f"{first_number} {o} {second_number} = {first_number + second_number}" )
                            f.write(f"{first_number} {o} {second_number} = {first_number + second_number}\n" )
                        elif o == '-':
                            print(f"{first_number} {o} {second_number} = {first_number - second_number}" )
                            f.write(f"{first_number} {o} {second_number} = {first_number - second_number}\n" )
                        elif o == 'x':
                            print(f"{first_number} {o} {second_number} = {first_number * second_number}" )
                            f.write(f"{first_number} {o} {second_number} = {first_number * second_number}\n" )
                        elif o == '/':
                            print(f"{first_number} {o} {second_number} = {first_number / second_number}" )
                            f.write(f"{first_number} {o} {second_number} = {first_number / second_number}\n" )
                        elif o == '^':
                            print(f"{first_number} {o} {second_number} = {first_number ** second_number}" )
                            f.write(f"{first_number} {o} {second_number} = {first_number ** second_number}\n" )
                        #close the text file. 
                        f.close()
                        #set to false to the while loop is exited
                        calculator = False
                    #if incorrect characters are entered, print a statement and exit the for loop. Go back to the top of the while loop  
                    except ValueError:
                        print("You may only enter 2 numbers and 1 operator from the list. Please try again. \n")
                    except ZeroDivisionError:
                        print("Division by zero is not allowed. Please enter a different calculation")
    #if reading the text file selected, enter the reading the text file while loop               
    elif choice == '1':
        while file_name == True:
            #while loop for text file existing
            text_file = input("Please enter the name of the text file containing the calculations: ")
            try:
                #open the text file and print every line in it. 
                f = open(text_file, 'r')
                for line in f:
                    print(line)
                f.close()
                #set boolean to false to exit while loop
                file_name = False
            #anticipate the file name being entered incorrectly and print a prompt before going back to the top of the while loop to try again
            except FileNotFoundError:
                print("The file does not exist. Please ensure that you have spelt it correctly and included the file extension. \n")
            

    else:
        #if anything other than 0 or 1 is entered, the user is asked to try again
        print("Incorrect option entered. Please try again. \n")
    #if a correct choice is entered, the choice_opetion boolean is set to false and the while loop is exited
    if choice == '0' or choice == '1':
        choice_option = False
    else:
        choice_option == True



                
        
