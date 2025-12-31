print("tower of hanoi ")
def tower_hanoi(num,src,helper,dest):
    if num==1:
        print(f"moving disk from {src} to {dest}")
        return
    tower_hanoi(num-1,src,dest ,helper)
    print(f"moving disk from {src} to {dest}")
    tower_hanoi(num-1,helper,src,dest)
num= int(input("enter number of disks : "))
tower_hanoi(num,"A","B","C")