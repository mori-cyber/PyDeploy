import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv
import pandas as pd


def predict():
        X = np.random.randint(60, 198, (100,1))
        M=np.random.uniform(0.3,0.5,(100,1))
        B=np.random.uniform(5,10,(100,1))
        Y=X*M+B

        N = np.random.uniform(0.2, 0.8, 5)
        # plt.scatter(X,Y)
        # plt.xlabel('person_Weight')
        # plt.ylabel('person_height')
        # for m in M:
        #     y_pred = np.matmul(X, [N])    
        #     plt.plot(X, y_pred, c='red', lw=2)
        #     # plt.imshow() 
        #     plt.show() 
            
        m = np.matmul(inv(np.matmul(X.T,X)), np.matmul(X.T,Y))
        
        Y_pred = np.matmul(X,m)
        plt.scatter(X,Y)
        plt.plot(X,Y_pred,c='red',lw=2)
        plt.xlabel('person_Weight')
        plt.ylabel('person_height')
        plt.show()
if __name__=="__main__":
        predict()