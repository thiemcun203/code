def heapify(A,N,i):
    L=2*i+1
    R=2*i+2
    max=i
    if L<N and A[max] < A[L]:
        # A[i],A[2*i]=A[2*i],A[i]
        # heapify(A,N,2*i)
        max=L
    elif R <N and A[max] < A[R]:
        # A[i],A[2*i+1]=A[2*i+1],A[i]
        # heapify(A,N,2*i+1)
        max=R
    elif max!=i:
        (A[max],A[i])=(A[i],A[max])
        heapify(A,N,max)
        
def heapsort(A):
    N=len(A)
    for i in range(N//2-1,-1,-1):
        heapify(A,N,i)
        print(A)
    print(A)
    for i in range(N-1,0,-1):
        (A[0], A[i])=(A[i],A[0])
        heapify(A,i,0) # after build max-heap, we just need heapify from root cuz every child <= parent node
    return A



def Mergesort(L,R,A):
    if L>=R:
        return
    M=(L+R)//2
    Mergesort(L,M,A)
    Mergesort(M+1,R,A)
    Merge(L,M,R,A)

def Merge(L,M,R,A):
    TA=A[:]
    #merge to sorted list A[L..M] and A[M+!..R] into a unique sort list A[L,...,R]
    i=L
    j=M+1
    for k in range(L,R+1):
        if i>M: # if A[L..M] is full
            TA[k]=A[j]
            j+=1
        elif j>R:  # if A[M+1...R] is full
            TA[k]=A[i]
            i+=1
        else:
            if A[i]<A[j]:
                TA[k]=A[i]
                i+=1
            else:
                TA[k]=A[j]
                j+=1
    for k in range(L,R+1):
        A[k]=TA[k]        
    return A  
A=[1,5,2,3,10,8]  
print(Mergesort(0,5,A))  
print(A)  