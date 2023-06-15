class GrammarStats:
    def __init__(self):
        self.count = 0
        self.t = 0
    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        c = text[0]
        self.count +=1
        if c.isupper() == True:
            if text[-1] == '.':
                self.t +=1
                return True
            else:
                return False
        else:
            return False    
    def percentage_good(self):
        p = (self.t/self.count)*100
        return int(p)
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        