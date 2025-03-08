class Example:
    def __init__(self): 
        print("Public Constructor Called")

    def _init_protected(self):  
        print("Protected Constructor Called")

    def __init_private(self):  
        print("Private Constructor Called")

    def call_private(self): 
        self.__init_private()

class SubExample(Example):
    def __init__(self):
        super().__init__()  
        print("Subclass Constructor Called")
    
    def access_protected(self):
        self._init_protected() 

    def access_private(self):
        try:
            self.__init_private()  
        except AttributeError:
            print("Cannot access private constructor directly!")

obj=Example()
obj.call_private()  

sub_obj=SubExample()
sub_obj.access_protected()  
sub_obj.access_private()  
