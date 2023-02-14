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

    a1 = 3.6
    a2 = 3.6
    a3 = 3.8
    a4 = 3.8
    a5 = 3.9
    a6 = 3.9

    b1 = 1.675
    b2 = 1.675
    b3 = 1.436
    b4 = 1.436
    b5 = 1.318
    b6 = 1.318

    c1 = 0 
    c2 = -1.195
    c3 = round((b3 - b2) / (a3 - a2), 3)
    c4 = -1.188
    c5 = round((b5-b4) / (a5-a4), 3)
    c6 = -1.182

    d1 = 0
    d2 = 0
    d3 = round((c3-c2) / (a3-a2), 3)
    d4 = round((c4-c3) / (a4-a2), 3)
    d5 = round((c5-c4) / (a5-a3), 3)
    d6 = round((c6-c5) / (a6-a4), 3)

    e1 = 0
    e2 = 0
    e3 = 0
    e4 = round((d4-d3) / (a4-a1), 3)
    e5 = round((d5-d4) / (a5-a2), 3)
    e6 = round((d6-d5) / (a6-a3), 3)

    f1 = 0 
    f2 = 0
    f3 = 0
    f4 = 0
    f5 = (e5-e4) / (a5-a1)
    f6 = (e6-e5) / (a6-a2)

    print(np.matrix([[a1,b1,c1,d1,e1,f1],[a2,b2,c2,d2,e2,f2],[a3,b3,c3,d3,e3,f3], [a4,b4,c4,d4,e4,f4], [a5,b5,c5,d5,e5,f5], [a6,b6,c6,d6,e6,f6]]))
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
    print(np.rot90(r_mat))
    print()

    print(np.rot90(solve(A,r_mat)))

x_points = [3.6,3.8,3.9]
y_points = [1.675,1.436,1.318]
approximating_value = 3.7
print(question_one(x_points,y_points,approximating_value))
print()

question_two_three()

question_four()

question_five()