# %%
import numpy as np
X = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])
# %%
print(X)
# %%
print(y)
# %%
def gradiant_decent(X,y):
    w_curr=b_curr = 0 # itilise the random values
    iteration = 10000
    learning_rate = 0.01
    n = len(X)
    for i in range(iteration):
        y_pred = b_curr+w_curr*X
        error = (y-y_pred)
        cost_function  = (1/n)*sum(val**2 for val in error)
        
        wd = (-2/n)*sum(X*(y-y_pred))
        bd = (-2/n)*sum(y-y_pred)
        
        w_curr = w_curr-learning_rate*wd
        b_curr = b_curr-learning_rate*bd
        print(f'w{w_curr},b{b_curr} ,cost{cost_function},iteration{i}')
# %%
gradiant_decent(X,y)
# %%
w=2.0000000000000218
b = 2.999999999999924
y_pred = b+w*2
y_pred
# %%
