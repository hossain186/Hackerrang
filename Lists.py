if __name__ == '__main__':
    N = int(input())
    
    list = []

    for i in range(N):

        s = input()

        if "insert" in s:

            value = s[9:]
            indx =  s[7:-(len(value))]
            list.insert(int(indx),int(value))
        elif s == "print":
            print(list)

        elif "remove" in s:

            value = s[7:]
            list.remove(int(value))

        elif "append" in s:

            value = s[7:]
            list.append(int(value))
        elif s == "sort":
            list.sort()
        elif s == 'pop':
            list.pop()
        elif s == "reverse":
            list.reverse()