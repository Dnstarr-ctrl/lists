def squares(start, end):

    even = []
    odd = []
    

    for num in range(start, end + 1):
        square = num ** 2
        

        if square % 2 == 0:
            even.append(square)
        else:
            odd.append(square)
            

    print(f"Even square values: {even}")
    print(f"Odd square values: {odd}")
squares(1, 5)
