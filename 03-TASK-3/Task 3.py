def WaterJug(X, Y, T):
    Stack = [(0,0)]
    Visited = set()
    while Stack:
        x, y = Stack.pop()
        print(x,y)

        if x == T or y == T:
            print("Possible")
            return
        if (x, y) in Visited:
            continue
        Visited.add((x, y))
        Stack.append((X, y))
        Stack.append((x, Y))
        Stack.append((0, y))
        Stack.append((x, 0))
        N_X = max(0,x - (Y-y))
        N_Y = min(Y, y+x)
        Stack.append((N_X,N_Y))
        N_X = min(X,x+y)
        N_Y = max(0, y-(X-x))
        Stack.append((N_X,N_Y))

WaterJug(7,5,1)        