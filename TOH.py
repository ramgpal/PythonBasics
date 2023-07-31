def TowerOfHanoi(n, source, medium, destination):
    if n == 1:
        print("Move disc " + str(n) + " from Source: " + source + " to Destination: " + destination)
        return
    TowerOfHanoi(n-1, source, destination, medium)
    print("Move disc " + str(n) + " from Source: " + source + " to Destination: " + destination)
    TowerOfHanoi(n-1, medium, source, destination)

print("Steps to solve Tower of Hanoi with 3 disks:")
TowerOfHanoi(3, "A", "B", "C")
