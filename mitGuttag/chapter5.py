t1 = (1,'two',3)
t2 = (t1,3.25)

print(t2)
print((t1+t2))
print((t1+t2)[3])
print((t1+t2)[2:5])

def intersect(t1, t2):
    """Assumes t1 and t2 are tuples
    Returns a tuple containing elements that are in
    both t1 and t2"""
    result = ()
    for e in t1:
        if e in t2:
            result += (e,)
    return result

t1 = (1,2,3,4)
t2 = (2,4)
print(intersect(t1,t2))

def findExtremeDivisors(n1, n2):
    """Assumes that n1 and n2 are positive ints
    Returns a tuple containing the smallest common divisor > 1 and
    the largest common divisor of n1 and n2. If no common divisor,
    returns (None, None)"""
    minVal, maxVal = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if minVal == None:
                minVal = i
            maxVal = i
    return (minVal, maxVal)

minDivisor, maxDivisor = findExtremeDivisors(1000, 1010)
print(minDivisor, maxDivisor)