# try:
#     with open('newsample.txt', 'a') as file2:
#         file2.writelines(['That makes him a versatile entrepreneur', '\nHe has the best of both world: tech & business'])
# except Exception as e:
#     print('Error', e)
# list =[]
# with open('new.txt', 'r') as file:
#     data = file.readlines()
#     print(data.index('Yes I am.'))
#     for x in data:
#         if data.index(x) % 2:
#             list.append(x)

# print(list)

# def write_first_line_to_file(file_contents, output_filename):
#     file = open(file_contents, 'r') 
#     with open(output_filename, 'a') as file2:
#         file2.write(file.readline())
# write_first_line_to_file('test.txt', 'new.txt')

# list = []
# file = open('new.txt', 'r')
# for x in file.readlines():
#     list.append(x)
# list.reverse()
# print(list)

def read_file(file_name):
    file = open(file_name, 'r')
    print(file.read())
read_file('new.txt')