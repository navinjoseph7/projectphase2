# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self.todolist = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.todolist.append(todo)
    
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return list(filter(lambda x : x.complete is False, self.todolist))

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return list(filter(lambda x : x.complete is True, self.todolist))
       # return list(k for k,v in self.todolist.items() if v == True)


    def give_up(self):
        for item in self.todolist:
            item.mark_complete()
       
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
       # for key in self.todolist:
           # self.todolist[key]= False
