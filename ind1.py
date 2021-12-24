import moduleConv

if __name__ == "__main__":
    to_tuple = moduleConv.converter('tup')
    print(to_tuple('1 3 4 55 6'))
    
    to_list = moduleConv.converter('list')
    print(to_list('1 3 4 55 6'))