
b = [[1,2,3],
    [4,5,6],
    [7,8,9]]

def print_matrix(b):
    for i in range(len(b)):
        for j in range(len(b[i])):
            print(b[i][j], end = " ")
        print()
b[1][1] = 100

def create_2d_arr(m, n):
    arr_2d =[]
    for i in range(m):
        internal_arr = []
        for j in range(n):
            internal_arr.append(0)
        arr_2d.append(internal_arr)
    return arr_2d
arr_50_1000 = create_2d_arr(50, 1000)
print_matrix(arr_500_1000)


        