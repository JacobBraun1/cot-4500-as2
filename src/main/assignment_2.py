import numpy as np
from scipy.linalg import solve
np.set_printoptions(precision=7, suppress=True, linewidth=100)

def question_one(x_points, y_points, approximating_value):
    n = len(x_points)
    p = n*[0]
    for k in range(n):
        for i in range(n-k):
            if k == 0:
                p[i] = y_points[i]
            else:
                p[i] = ((approximating_value-x_points[i+k])*p[i]+ \
                        (x_points[i]-approximating_value)*p[i+1])/ \
                        (x_points[i]-x_points[i+k])
    return p[0]
   
def question_two_three():

    point_1 = (25.3913-23.5492) / (7.4-7.2)
    q_1 = (26.8224-25.3913) / (7.5-7.4)
    k_1 = (27.4589-26.8224) / (7.6-7.5)

    point_2 = (q_1-point_1) / (7.5-7.2)
    q_2 = (k_1-q_1) / (7.6-7.4)

    point_3 = (q_2-point_2) / (7.6-7.2)
    print([point_1, point_2, point_3])
    print()


    #QUESTION 3

    point_1_2 = 23.5492 + point_1*(7.3-7.2)
    point_2_2 = point_1_2 + point_2*(7.3-7.4)*(7.3-7.2)
    point_3_2 = point_2_2 + point_3*(7.3-7.5)*(7.3-7.4)*(7.3-7.2)
    print(point_3_2)
    print()



def question_four():
   
    c3 = round((1.436 - 1.675) / (3.8 - 3.6), 3)
    c5 = round((1.318-1.436) / (3.9-3.8), 3)
    
    d3 = round((c3-(-1.195)) / (3.8-3.6), 3)
    d4 = round((-1.188-c3) / (3.8-3.6), 3)
    d5 = round((c5-(-1.188)) / (3.9-3.8), 3)
    d6 = round((-1.182-c5) / (3.9-3.8), 3)

    e4 = round((d4-d3) / (3.8-3.6), 3)
    e5 = round((d5-d4) / (3.9-3.6), 3)
    e6 = round((d6-d5) / (3.9-3.8), 3)

    r1 = [3.6,1.675,0,0,0,0]
    r2 = [3.6,1.675,-1.195,0,0,0]
    r3 = [3.8,1.436,c3,d3,0,0]
    r4 = [3.8,1.436,-1.188,d4,e4,0]
    r5 = [3.9,1.318,c5,d5,e5,(e5-e4) / (3.9-3.6)]
    r6 = [3.9,1.318,-1.182,d6,e6,(e6-e5) / (3.9-3.6)]

    print(np.matrix([r1,r2,r3, r4, r5, r6]))
    print()

def question_five():

    x0 = 2
    x1 = 5
    x2 = 8
    x3 = 10
    y0 = 3
    y1 = 5
    y2 = 7
    y3 = 9

    h0 = x1-x0
    h1 = x2-x1
    h2 = x3-x2

    r1 = [1,0,0,0]
    r2 = [h0,2*(h0+h1),h1,0]
    r3 = [0,h1,2*(h1+h2),h2]
    r4 = [0,0,0,1]
    A = np.matrix([r1,r2,r3, r4], dtype='float')
    print(A)
    print()

  
    r_mat = np.matrix([[0],[((3/h1)*(y2-y1)) - ((3/h0)*(y1-y0))],[((3/h2)*(y3-y2)) - ((3/h1)*(y2-y1))],[0]])
    print(np.ravel(np.rot90(r_mat)))
    print()

    print(np.ravel(np.rot90(solve(A,r_mat))))
    
x_points = [3.6,3.8,3.9]
y_points = [1.675,1.436,1.318]
approximating_value = 3.7
print(question_one(x_points,y_points,approximating_value))
print()

question_two_three()

question_four()

question_five()