def print_triangle(n):
    if n != 0:
        str = ("*" * n)
        print_triangle(n-1)
        print(str)

def print_oposite_triangles(n):
    if n != 0:
        if n == 1:
            print("*")
            print("*")
        else:
            print("*" * n)
            print_oposite_triangles(n - 1)
            print("*" * n)

def print_ruler(n):
    if (n==0) or (n==1):
        print("-")
        return
    print_ruler(n-1)
    str = ""
    for i in range(n):
        str+= "-"
    print(str)
    print_ruler(n-1)
    return
