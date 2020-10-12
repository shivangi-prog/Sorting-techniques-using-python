__author__ = 'TARUNCH'
import random
import time
#header files
# added some comments for better understanding of program and participating in hacktoberfest
def msort(a):#define a function
    if len(a) > 1:
        mid = len(a)/2
        b = a[:mid]
        c = a[mid:]


        msort(b)
        msort(c)
        i = 0
        j = 0
        k = 0
        while i < len(b) and j < len(c):
            if b[i] < c[j]:#comparing the number in a and b array
                a[k] = b[i]
                i = i + 1
            else:
                a[k] = c[j]
                j = j + 1
            k = k + 1

        while i < len(b):
            a[k] = b[i]
            i = i + 1
            k = k + 1
        while j < len(c):
            a[k] = c[j]
            j = j + 1
            k = k + 1

st = time.time()
a = random.sample(range(1,1000),999)
a.sort(reverse=True)
msort(a)
print ("%s sec" ,(time.time()-st)*1000)


