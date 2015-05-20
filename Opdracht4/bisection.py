def findRoot(f, a, b, epsilon):
    m = float((a + b) / 2)

    if b - a <= epsilon:
        return m
    if f(a) <= 0 and f(m) >= 0:
        return findRoot(f, a, m, epsilon)
    if f(m) <= 0 and f(b) >= 0:
        return findRoot(f, m, b, epsilon)
    if f(m) >= 0 and f(b) <= 0:
        return findRoot(f, m, b, epsilon)
    if f(a) >= 0 and f(m) <= 0:
        return findRoot(f, a, m, epsilon)
        
def recursion(f, a, b, epsilon, roots):
    if b - a <= epsilon:
        if (f(a) <= 0 and f(b) >= 0) or (f(b) <= 0 and f(a) >= 0): roots.append(findRoot(f, a, b, epsilon))
    else:
        m = float((a + b) / 2)
        recursion(f, a, m, epsilon, roots)
        recursion(f, m, b, epsilon, roots)
    
def findAllRoots(f, a, b, epsilon):
    roots = []
    recursion(f, a, b, epsilon, roots)
    return roots
    
    
    