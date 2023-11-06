if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    a = list(arr)
    
    for i in range(1,len(a)):

        key = a[i]
        j = i-1

        while j>=0 and a[j]>key:

            a[j+1] = a[j]
            j = j-1
        a[j+1] = key


    new = []

    max = a[-1]

    for i in a:

        if i == max:
            continue
        else:
            new.append(i)

    print(new[-1])
        
