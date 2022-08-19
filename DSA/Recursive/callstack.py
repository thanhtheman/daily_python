#Build an example of a call stack to understand how each execution content is executed.
# For each time of n, we want to do specific thing = we want to add the value of n.
def sum_to_one(n):
    result = 1
    call_stack = []
    # Step 1 - Adding tasks to the call stack
    while n != 1:
        execution_context = {'n_value': n}
        call_stack.append(execution_context)
        print(call_stack)
        n -= 1
    print("Base case is reached. All tasks are added to the call stack")
    
    #Step 2 Adding the value of n in the execution context
    while len(call_stack) != 0:
        return_value = call_stack.pop()
        print("Returning value {a} is added to result of {b}".format(a = return_value['n_value'], b = result))
        result += return_value['n_value']
    print(result)
    print(call_stack)
sum_to_one(4)

# This is what happen with n = 4, before we add all the numbers 1 + 2 + 3 +4
#[{'n_value': 4}]
#[{'n_value': 4}, {'n_value': 3}]
#[{'n_value': 4}, {'n_value': 3}, {'n_value': 2}]
#Base case is reached. All tasks are added to the call stack
#Returning value 2 is added to result of 1
#Returning value 3 is added to result of 3
#Returning value 4 is added to result of 6
#10
#[]