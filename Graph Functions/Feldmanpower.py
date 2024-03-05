def print_graph(n):
    print('*' * n, end='\n')

def get_power(x, n):
    return(x**n)

for i in range(-8, 9):
    x=i
    y=get_power(x, 2)
    print_graph(y)