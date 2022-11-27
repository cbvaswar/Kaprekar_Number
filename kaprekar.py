length=4 #Choose the length/digit of number
knclist=[]
knccyc=[]


def ctuple(x):
    y=str(x)
    y=list(y)
    i=0
    while i<len(y):
        y[i]=int(y[i])
        i=i+1
    while len(y)<length:
        y=[0]+y
    z=tuple(y)
    return z

def isvalid(x):
    a=ctuple(x)
    a=sorted(a)
    b=ctuple(x)
    b=sorted(b,reverse=True)
    return a!=b

def convtn(h):
    j=len(h)
    sum=0
    while j>0:
        sum=sum+(10**(j-1))*h[len(h)-j]
        j=j-1
    return sum

start=10**(length-1)
end=10**(length)-1

def knc(x):
    a=ctuple(x)
    b=ctuple(x)
    a=sorted(a)
    b=sorted(b,reverse=True)
    a=convtn(a)
    b=convtn(b)
    return abs(a-b)

def isrepeat(x):
    l=sorted(x)
    i=0
    while i<len(l)-1:
        if l[i]==l[i+1]:
            return True
        i=i+1
    return False


def knctest(x):
    global knclist
    global knccyc
    #print "x=",x
    a=x
    l=[a]
    while isrepeat(l)==False:
        last=l[len(l)-1]
        if last==knc(last):
            #print ("The fixed point is ", last)
            #print "\n"
            if (last in knclist)==False:
                knclist+=[last]
                print ("Fixed point found",last)
            return
        else:
            l=l+[knc(last)]
    if (last in knccyc)==False:
        knccyc+=[last]
        print ("Cyclic point found :",last)
    #print ("Cycle detected!",l)
    #print "\n"
    return last

x=start
while x<end:
    #print "***\n"
    knctest(x)
    x=x+1
    if x%(10**7)==0:
        print ("Tested so far till:",x)
        print ("So far results, \n ***")
        print ("Knc Fixed points :",knclist),"\n"
        print ("Knc Cyclic points : ",knccyc),"\n"
    #print "***\n"
print ("Final KnC=",knclist)
print ("Final KnC cycle=",knccyc)
