#startsWith(), endsWith() and compareTo()
s1= "HemaKumari"
s2 = "Hema"
s3 = "Kumari"

print("Starts with 'HemaKumari':", s1.startswith(s2))
print("Ends with 'Kumari':", s1.endswith(s3))  

print("Comparing 'apple' and 'banana':",(lambda a,b:(a>b)-(a<b))("apple", "banana"))  # -1
print("Comparing 'banana' and 'apple':",(lambda a,b:(a>b)-(a<b))("banana", "apple"))  # 1
print("Comparing 'hello' and 'hello':", (lambda a,b:(a>b)-(a < b))("hello", "hello"))  # 0
