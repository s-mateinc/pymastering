#the get method on dicts and its default arguments
student_numbers ={
    102: "Jason",
    109: "Alice",
    904: "Peterson",
    123: "Margie"}

def greeting(studentId):
    return "Hi %s!" % student_numbers.get(studentId,"there")

print(greeting(102))
print(greeting(1112))