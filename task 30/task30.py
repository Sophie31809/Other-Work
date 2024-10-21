#An Email Simulation

#creating class for email
class Email:

    #constructor:
    def __init__(self, email_contents, from_address):
        self.email_contents = email_contents
        self.from_address = from_address
        self.has_been_read = False
        self.is_spam = False
    #functions to mark emils as read and as spam
    def mark_as_read(self):
        self.has_been_read = True
        return self.has_been_read
    def mark_as_spam(self):
        self.is_spam = True
        return self.is_spam

#create empty list to reperesent the inbox
inbox = []

#creating function to add an email to the inbox
def add_email( contents, email_address):
    inbox.append(Email(contents, email_address))

#creating function to return tehe number of emails in the inbox
def get_count():
    print(f"There are {len(inbox)} messages in the store")
    return(len(inbox))

#creating a function to read a specifiec email in the inbox
def get_email(email_index):
    print(inbox[email_index].email_contents)
    inbox[email_index].mark_as_read() #mark email as read after reading
    return inbox[email_index].email_contents

#create a function to return all of the unread emails
def get_unread_emails():
    unread_list = []
    for i in inbox:
        if i.has_been_read == False:
            unread_list.append(i)
    return unread_list

#create a function to return all of the spam emails
def get_spam_emails():
    spam_list = []
    for i in inbox:
        if i.is_spam == True:
            spam_list.append(i)
            print(i.email_contents)
    print(len(spam_list))
    return spam_list

#create a function to delete an email from the inbox
def delete(email_index):
    inbox.remove(inbox[email_index])

#creating some emails 
add_email('Hi Just seeing how you are!', 'friend@hotmail.com')
add_email('Would you like to sign up to our subscription?', 'marketer@company.com')
add_email('Hello can we confirm out plans for next week?', 'aquaintence@gmail.com') 



user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/see spam/see unread/see count/delete/quit?")
    if user_choice == "read":
        #ask for index and print the contents using the get email function
        try:
            email_index = int(input("Enter the position in the inbox of the email you would like to read: "))
            get_email(email_index)
        except Exception:
            print('Invalid index entered')
    elif user_choice == "mark spam":
        #taking the index and marking it as spam
        spam_email = int(input("Enter the position in the inbox of the email that you would like to mark spam: "))
        try:
            inbox[spam_email].mark_as_spam()
        except Exception:
            print('Invalid index entered')
        #use the add email function to send an email
    elif user_choice == "send":
        contents = input("Enter the contents of the email")
        address = input("What address has the email been sent from?")
        add_email(contents, address)
    #add option to see all of the emails marked as spam
    elif user_choice == "see spam":
        spam = get_spam_emails()
        for i in spam:
            print(f" Email contents = {i.email_contents}")
    #add option to see all of the unread emails. Once these emails have been viewed, they are marked as read
    elif user_choice == 'see unread':
        unread = get_unread_emails()
        for i in unread:
            print(f"Email contents = {i.email_contents}")
            i.mark_as_read()
    #add option to see the number of emails in the inbox
    elif user_choice == 'see count':
        print(get_count())
    #add the option to delete an email from the inbox
    elif user_choice == "delete":
        index_to_delete = int(input("Please enter the index of the email you would like to delete: "))
        delete(index_to_delete)                    
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")


