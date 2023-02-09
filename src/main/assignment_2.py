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

x_points = [3.6,3.8,3.9]
y_points = [1.675,1.436,1.318]
approximating_value = 3.7
print(question_one(x_points,y_points,approximating_value))
   
   