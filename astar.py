def h(n):
    h_distance = {'a':11,'b':9,'c':3,'d':4,'e':12}
    return h_distance[n]
g_node ={'a':[('b',9),('c',5),('e',12)],
        'b':[('a',9),('d',4)],
        'c':[('a',5),('d',4)],
        'd':[('b',4),('c',3),('e',5)],
        }
        
def aStar(start_n,stop_n):
    opn_set = set(start_n)
    cls_set = set()
    g = {}
    p_node = {}
    g[start_n] = 0
    p_node [start_n] = start_n 
    while len(opn_set)>0:
        n = None
        
        for v in opn_set:
            if n == None or g[v] + h(v) < g[n] + h(n):
                n =v 
        if n == stop_n or g_node[n] == None:
            pass
        else:
            for(m,weight) in get_neighb(n):
                if m not in opn_set and m not in cls_set:
                    opn_set.add(m)
                    p_node[m] = n 
                    g[m] = g[n] + weight 
                else:
                    if g[m]>g[n] + weight:
                        g[m] = g[n]  + weight
                        p_node[m] = n
                        if m in cls_set:
                            cls_set.remove(m)
                            opn_set.add(m)
        if n ==None:
            print("path does not exist ")
            return None
        if n == stop_n:
            path = []
            while p_node[n] != n:
                path.append(n)
                n = p_node[n]
            path.append(start_n)
            print("path found")
            path.reverse()
            print(path)
            return path
        opn_set.remove(n)
        cls_set.add(n)
    print("path does not exist")
    return None
def get_neighb(v):
    if v in g_node:
        return g_node[v]
    else:
        return None
aStar('a','d')
    
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
                        
