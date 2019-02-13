import Item
import datetime
# Making the Manager class to be able to read, write, and print text
class Manager(object):

    def print_tasks(self):
        # Here i am simply using with open in order to be able to interact with the file and not have to close it later in the module, and also it looks way cleaner than my old method.
        with open("todos.txt", 'r') as x: # Opening my file and Specifiying i want to READ it.
            view = x.read()
            print(f"""+----------------------------+
~ Here are your tasks so far ~
+----------------------------+
{view}""")
    # This is a method to let the users add items to the todos.txt file and that way they can actually interact with their todo-manager
    def add_tasks(self):
        # This version that im using to add tasks into my todo list is a little more cleaner because by using with open I dont have to worry about closing that opened file later in the module.
        with open("todos.txt", 'a') as y: # Opening my file and Specifiying i want to APPEND it to the input of the user.
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            add = y.write("- " + (input( """------------
+Add a task+
------------
> """)) + f" |CREATED|: {time_stamp}" + "\n")

        with open("todos.txt", 'r') as y: # Since the other argument opened files with the intent to APPEND here  I am making open argument so I am able to READ and view the file.

            # I just wanted the user to be able to view their new added task before the program stopped running.
            view = y.read()
            print(f"""+----------------------------------+
| You added one task to your list! |
|                                  |
|      Now it looks like this      |
+==================================+
                LIST:
{view}""")

    # This method makes sure the user is greeted and also directs the module in the right direction on what the user wants to do by using if statements
    def start():
        print("""+----------------------------------+
| Welcome to your to task manager! |
| What would you like to do today? |
|..................................|
|                                  |
|       1. "view" your tasks       |
|       2. "add" a task            |
|       3. "complete" a task       |
|                                  |
+==================================+""")



        # I wanna accept user input here so i can direct the module towards the correct if statement
        choice = input("> ")

        # Takes you to the add method in the Manager class
        if choice == 'add':
            add = Manager()
            add.add_tasks()
        # Takes you to the view method in the Manager Class
        if choice == 'view':
            view = Manager()
            view.print_tasks()
