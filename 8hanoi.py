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

#common and important problems similar to Tower of Hanoi
#factorial
def fact(n):
    if n==0 and n==1:
        return 1
    else :
        return n* fact(n-1)
print(fact(5))

#fibonacci

def fibo(n):
    if n==0:
        return 0
    if n==1 :
        return 1
    else:
        return fibo(n-1 )+ fibo(n-2)
    
for i in range(6):
    print(fibo(i),end=" ")
 
 # Sum of First n Numbers   
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))
  
# Power of a Number
  
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

print(power(2, 5))
