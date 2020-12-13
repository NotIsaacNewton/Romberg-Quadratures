#MIDPOINT METHOD
def mid_one_d(steps, a, delta_x, f):
    i = 0
    for n in range(0,steps):
        x = a + (n * delta_x) #UPDATE X BY ADDING N * DELTA-X
        i += f(x + (delta_x * 0.5)) * delta_x #UPDATE INTEGRAL SUM USING MIDPOINT METHOD
    return i

#TRAPEZOIDAL ORDINAL SUM
def trapezoidal_ordsum(steps, a, b, a_new, b_new, delta_x, f):
    ordsum = 0
    x = a_new #SET STARTING POINT FOR X
    
    if a == a_new and b == b_new: #CHECK IF THIS IS THE FIRST ITERATION OR NOT
        ordsum += 0.5 * f(x) #ADD HALF OF THE STARTING ENDPOINT
        for n in range(1,steps-1): #REPEAT LOOP FROM FROM AFTER STARTING ENDPOINT TO BEFORE ENDING ENDPOINT
            x = a + (n * delta_x) #UPDATE X BY ADDING N * DELTA_X
            ordsum += f(x) #ADD TO ORDINATE SUM
        ordsum += 0.5 * f(x + delta_x) #ADD HALF OF THE ENDING ENDPOINT
    else:
        for n in range(0,steps): #REPEAT LOOP FROM FROM AFTER STARTING ENDPOINT TO BEFORE ENDING ENDPOINT
            if (x + (delta_x/2)) <= b:
                x = a_new + (n * delta_x) #UPDATE X BY ADDING N * DELTA_X
                ordsum += f(x) #ADD TO ORDINATE SUM
            
    return ordsum