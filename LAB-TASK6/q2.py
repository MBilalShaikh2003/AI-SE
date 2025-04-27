def tower_of_hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Disk 1 moved from {source} to {target}")
        return
    # Move n-1 disks from source to auxiliary peg
    tower_of_hanoi(n-1, source, auxiliary, target)
    # Move the nth disk from source to target
    print(f"Disk {n} moved from {source} to {target}")
    # Move the n-1 disks from auxiliary to target
    tower_of_hanoi(n-1, auxiliary, target, source)

# Example usage:
print("Tower of Hanoi with 2 disks:")
tower_of_hanoi(2, 'A', 'C', 'B')

print("\nTower of Hanoi with 3 disks:")
tower_of_hanoi(3, 'A', 'C', 'B')