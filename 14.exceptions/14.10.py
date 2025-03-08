class SampleClass:
    pass  

try:
    cls_name="NonExistentClass"  
    cls = getattr(__name__, cls_name)  
except AttributeError as e:
    print("Error: Class not found!", e)
