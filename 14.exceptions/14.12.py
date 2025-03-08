class SampleClass:
    def __init__(self):
        self.existing_field = "Hello, World!"

try:
    obj = SampleClass()
    print(obj.non_existent_field) 
except AttributeError as e:
    print("NoSuchFieldException: The requested field does not exist!", e)
