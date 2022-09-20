# list comprehension
# data = [2,3,5,7,11,13,17,19,23,29,31]

# data = [x+3 for x in data]
# print('updating the list', data)

# new_data = [x*2 for x in data]
# print('creating a new list', new_data)

# fourx = [x-1 for x in new_data if x %4 == 0]
# print('creating a new list with condition', fourx)

# new_list = [x+3 for x in range(100) if x%5 == 0 and x%2 == 0 and x >= 5]
# print('creating a new list out of a range', new_list)

#dictionary comprehension

# months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# number = [1,2,3,4,5,6,7,8,9,10,11,12]

# numdict = {x:x*2 for x in number}
# print('creating a dict from a list', numdict)

# months_dict = { key:value for (key,value) in zip(number, months)}
# print('combining 2 lists to create a dict', months_dict)

#set comprehension
# set_1 = {x for x in range(10,20) if x %2 ==0}
# print(set_1)

#generator comprehension
# data = [2,3,5,7,11,13,17,19,23,29,31]

# gen_obj = (x for x in data)
# print(gen_obj)
# for x in gen_obj:
#     print(x)



employee_list = [
   {"id": 12345, "name": "John", "department": "Kitchen"},
   {"id": 12456, "name": "Paul", "department": "House Floor"},
   {"id": 12478, "name": "Sarah", "department": "Management"},
   {"id": 12434, "name": "Lisa", "department": "Cold Storage"},
   {"id": 12483, "name": "Ryan", "department": "Inventory Mgmt"},
   {"id": 12419, "name": "Gill", "department": "Cashier"}
]

def mod(employee_list):
   temp = employee_list['name'] + "_" + employee_list["department"]
   return temp

def to_mod_list(employee_list):
    map_emp = map(mod, employee_list)
    list = [x for x in map_emp]
    return list

mod_list = to_mod_list(employee_list)

def generate_usernames(mod_list):
    username = [x.replace(" ","_") for x in mod_list]
    return username

print(generate_usernames(mod_list))

def map_id_to_initial(employee_list):
    id_to_initial = {x['name'][0]:x['id'] for x in employee_list}
    return id_to_initial

print(map_id_to_initial(employee_list))