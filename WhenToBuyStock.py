def findStock(S,n):    
    local_maxima = local_minima = 0
    no_profit = 0
    for i in range(0, n, 1):
        if S[i] > S[local_maxima]:
            local_maxima = i
        else:
            if local_minima != local_maxima:
                print ("({} {})".format(local_minima, local_maxima), end = " ")
                no_profit += 1
            local_minima = i
            local_maxima = i
    if local_minima != local_maxima:
        print ("({} {})".format(local_minima, local_maxima))
        no_profit += 1
    elif no_profit == 0:
        print("No Profit")
    else:
        # Biggest mistake to not change line number
        # it was printing the other use case output here only
        print()
    return

if __name__=='__main__':
    t=1
    for i in range(t):
        n = 7
        S = [100 ,180 ,260 ,310 ,40 ,535 ,695]
        findStock(S, n)
       