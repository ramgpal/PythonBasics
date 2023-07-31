# Tower of Hanoi

def Toh(n, source, destination, medium):
    if(n == 1):
        print("Move disk 1 from", source, "to", destination)
    Toh(n-1, source, medium, destination)
    print("Move disk n from", source, "to", destination)
    Toh(n-1, destination,, source, medium)
Toh(3, 'A', 'B', 'C')

# def tower_of_hanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print("Move disk 1 from", source, "to", destination)
#         return
#     tower_of_hanoi(n - 1, source, auxiliary, destination)
#     print("Move disk", n, "from", source, "to", destination)
#     tower_of_hanoi(n - 1, auxiliary, destination, source)


# # Example usage
# n = 3  # Number of disks
# tower_of_hanoi(n, 'A', 'C', 'B')
