class Matrix:
    def __init__(self, M ):
        self.M=M
    def solve(self, b):
        def lst_complement(r,c,M):
            import copy
            M_copy=copy.deepcopy(M)
            M_copy1=copy.deepcopy(M)
            for i in range(len(M_copy)):
                k=0
                for j in range(len(M_copy[i])):
                    if i==r or j==c: 
                        M_copy1[i].pop(j-k)
                        k+=1
            M_copy1.remove([])
            return M_copy1

        def DET(M):
            d={}
            for k in [[i] for i in [k for sublst in M for k in sublst]]:
                d[str([k])]=k[0]
            def det(M,d):
                if str(M) in d:
                    return d[str(M)]
                else:
                    Sum=0
                    for j in range(len(M[0])):
                        Sum+=M[0][j]*(-1)**(0+j)*det(lst_complement(0,j,M),d)
                    d[str(M)]=Sum
                    return d[str(M)]
            return det(M,d)
        
        def inverse_matrix(M):
            inverse_DET= 1/DET(M)
            lst=[[inverse_DET*DET(lst_complement(i,j,M))*(-1)**(i+j) for j in range(len(M[0])) ] for i in range(len(M))]
            transpose_lst=[[lst[i][j] for i in range(len(M))] for j in range(len(M[0]))]
            return transpose_lst
        
        def mul(M,b):
            result=[[x*y for x,y in zip(M[i],b)] for i in range(len(M))]
            return result
        def convert(x):
            solution=[f'{sum(i):.2f}' for i in x]
            return " ".join(solution)
        return convert(mul(inverse_matrix(self.M),b))
    def mul(self,b):
        if len(self.M[0])==len(b):
            transpose_lst=[[b[i][j] for i in range(len(b))] for j in range(len(b[0]))]
            re=[[[x*y for x,y in zip(self.M[i],transpose_lst[j])] for j in range(len(transpose_lst))] for i in range(len(self.M))]
            result=[[sum(i) for i in re[k] ] for k in range(len(re))]
            return result
        else:
            raise TypeError("Can not mulitiply")
    def __str__(self):
        s=[ "\t".join(str(k) for k in i) for i in self.M ]
        return str("\n".join(s))
class SquareMatrix(Matrix):
    def __init__(self,M) -> None:
        Matrix.__init__(self,M)
    def __pow__(self,k):
        MT=self.M
        def power(MT,k):
            if k==1:
                return MT
            if k==0:
                return [[1,0],[0,1]]
            else:
                return SquareMatrix.mul(self,power(MT,k-1)) # self  represent for instance
        
        return SquareMatrix(power(MT,k))
    
m = SquareMatrix([[1, 0], [0, 1]])
print(isinstance(m, Matrix))
m = SquareMatrix([[1, 1], [0, 1]])
print(m ** 0)
print(m ** 2)

        
            