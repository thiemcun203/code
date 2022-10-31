from re import M


class Matrix:
    def __init__(self,M):
        self.M=M
    def mul(self,b):
        if len(self.M[0])==len(b):
            transpose_lst=[[b[i][j] for i in range(len(b))] for j in range(len(b[0]))]
            re=[[[x*y for x,y in zip(self.M[i],transpose_lst[j])] for j in range(len(transpose_lst))] for i in range(len(self.M))]
            result=[[sum(i) for i in re[k] ] for k in range(len(re))]
            return result
        else:
            raise TypeError("Can not mulitiply")
    def power(self,k):
        def pow(M,k): # ko đc call trực tiếp vì đây là method
            if k==0 or k==1:
                return M
            else:
                return Matrix.mul(self,pow(M,k-1))
        return pow(self.M,k)
m=Matrix([[1,0,6],[0,1,5],[2,4,5]])
# print(Matrix.mul(m,[[1,0,6], [0,1,5]]))
print(Matrix.power(m,100))



