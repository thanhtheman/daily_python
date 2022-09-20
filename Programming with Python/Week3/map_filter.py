menu = ['cappucino', 'da chanh', 'expresso', 'iced cofee', 'cortano', 'matcha latte']

def find_coffee(item):
    if item[0] == 'c':
        return item

# coffee = map(find_coffee, menu)
coffee = filter(find_coffee, menu)
print(coffee)

for x in coffee:
    print(x)