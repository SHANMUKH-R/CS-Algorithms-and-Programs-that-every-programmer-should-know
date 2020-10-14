def bubble_sort(n):
    for i in range(len(n)):
        for j in range(0,len(n)-i-1):
            if n[j]>n[j+1]:
                temp=n[j]
                n[j]=n[j+1]
                n[j+1]=temp
    print(n)
x=[5,6,4,3,2,1,7,8,9,0]
bubble_sort(x)


def selection_sort(n):
    for i in range(0,len(n)-1):
        smallest=i
        for j in range(i+1,len(n)):
            if (n[j]<n[smallest]):
                smallest=j
                temp=n[i]
                n[i]=n[smallest]
                n[smallest]=temp
n=[5,6,3,8,9,1]
selection_sort(n)
print(n)


def insertion_sort(n):
    for i in range(1,len(n)):
        fixed=n[i]
        j=i-1
        while j>=0 and fixed<n[j]:
            n[j+1]=n[j]
            j=j-1
        n[j+1]=fixed
        
n=[3,4,5,1,2,8,6]
insertion_sort(n)
print(n)
for i in range(len(n)):#this gives output vertically
    print("%d"%n[i])
        
        