# taking the input
# splitting the data and create a dictionary
# query the dictionary with unlimited time, return 'Not Found'
phone_book = {}
for i in range(int(input())):
    data = input()
    data_array = data.split(' ')
    phone_book[data_array[0]] = data_array[1]

while True:
    query = input()
    try:
        answer = phone_book[query]
        print(f'{query}={answer}')
    except:
        print('Not Found')