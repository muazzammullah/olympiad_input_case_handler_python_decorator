# olympiad_input_case_handler_python_decorator
Python Decorator to help handle test cases in olympiad questions.

Just get the decorator and add @case to the function you want to handle input for.the decorator injects an array argument into the decorated function
you must have passed array argument into a function.

for example
@case
def myfunction(arr):
  print(arr)
