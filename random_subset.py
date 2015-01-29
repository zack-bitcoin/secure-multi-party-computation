#this code is for learning about what subsets of SMPC nodes are needed in order to recreate the data.
import random
def r():
    a=lambda: random.randint(0,2)
    return [a(), a(), a()]
def ran_list(l):
    a=random.randint(0, len(l)-1)
    return l[a]
def remove_repeats(l):
    out=[]
    for i in l:
        if i not in out:
            out.append(i)
    return out
def random_subset(n):
    out=[]
    while len(out)<n:
        out.append(r())
        out=remove_repeats(out)
    return out
def same_row(a, b):
    return (a[0]==b[0] and a[1]==b[1]) or (a[0]==b[0] and a[2]==b[2]) or (a[1]==b[1] and a[2]==b[2])
def extend(a, b):
    if a[0]==b[0]: return [a[0]]+extend(a[1:], b[1:])
    if a[-1]==b[-1]: return extend(a[:-1], b[:-1])+[a[-1]]
    c=[0,1,2]
    c.remove(a[0])
    c.remove(b[0])
    return c
def improve(l):
    for i in range(1000):
        a=ran_list(l)
        b=ran_list(l)
        if a==b:
            pass
        elif same_row(a, b):
            third=extend(a, b)
            l.append(third)
            l=remove_repeats(l)
    return l
def test(n):
    s=0
    for i in range(100):
        if len(improve(random_subset(n)))==27:
            s=s+1
    print(s)
test(8)
test(9)
test(10)
test(11)
test(12)
test(13)
test(14)
test(15)

