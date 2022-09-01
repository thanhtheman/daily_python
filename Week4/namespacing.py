country = 'USA'
def local():
    country ='Germany'
    print(country)
    print(locals())

print(globals())
local()