MAX, MIN = 1000, -1000
def minmax(depth,nodeIndex,maxpl,valu,alpha,beta):
    if depth == 3:
        return valu[nodeIndex]
    if maxpl:
        best = MIN
        for i in range (0,2):
            val = minmax(depth+1,nodeIndex * 2 + i,False,valu,alpha,beta)
            best = max(best,val)
            alpha = max(alpha,best)
            if beta <=alpha:
                break
        return best
    else:
        best = MAX
        for i in range (0,2):
            val = minmax(depth+1,nodeIndex * 2 + i,False,valu,alpha,beta)
            best = min(best,val)
            beta = min(beta,best)
            if beta <= alpha:
                break
        return best
if __name__ == "__main__":
    valu = [3,5,6,9,1,2,0,-1]
    print("The optimal value is :",minmax(0,0,True,valu,MIN,MAX))
    
