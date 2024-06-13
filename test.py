import numpy as np

mat1=np.array([[0,1,2,3],
                [4,5,6,7],
                    [8,9,10,11]])

indA=np.array([[2,2],[1,1]])
indB=np.array([[2,1],[1,0]])

mat1[indA,indB]=np.array([[100,90],[50,40]])
print(mat1)