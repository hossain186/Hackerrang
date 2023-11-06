if __name__ == '__main__':
    
    new = {}
    numbers = []
    for _ in range(int(input())):
        name = input()
        number = float(input())
        
        
        
        
        

        new[name] = number

        numbers.append(number)



    for i in range(1,len(numbers)):

        key = numbers[i]
        j = i-1

        while j>=0 and numbers[j]>key:

            numbers[j+1] = numbers[j]
            j-=1

        numbers[j+1] = key


    min = numbers[0]
    num = []
    for i in numbers:
        if i == min:
            continue

        else:
            num.append(i)

        value = num[0]


    names = []
    for i in new:
        if new.get(i) == value:
            names.append(i)

    for i in range(1,len(names)+1):
        print(names[-i])