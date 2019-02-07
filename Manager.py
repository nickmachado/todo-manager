
# Making the Manager class to be able to read, write, and print text
class Manager(object):

    def print_tasks(self):
        # Here we use using the arugment "target" as a place holder for when we use the command "open" on the file fiven to use through the terminal
        target = open("todos.txt", 'r')

        # We targeted a file on the terminal and now we want to read the content within that text file, thats when we use the "read" command
        contents = target.read()
        # Making sure the contents print out so the user can see what theirs tasks are
        print(contents)
        #We opened a file and in python we want to make sure we close that opened file to make sure it doesnt keep running in the background.
        target.close()


    def add_tasks(self):
        target = open("todos.txt", 'a')
        add =  target.write(input("> "))

text = Manager()
text.print_tasks()
