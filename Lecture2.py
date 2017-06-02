
import math

def sim(v1, v2):
    # compute cosine similarity of v1 to 2 : (v1 dot v2)/{||v1|| * ||v2||} 
    
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i];  y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy / math.sqrt( sumxx * sumyy )

 
kitten = [0,1,0,0,1,1,0,1]
cat    = [0,1,1,0,1,0,0,0]
dog    = [1,0,1,1,0,0,1,0]

print( "sim(kitten,cat) = " , cosine_similarity(kitten ,cat))  # 0.58
print( "sim(kitten,dog) = " , cosine_similarity(kitten ,dog))  # 0.00
print( "sim(cat,dog) = " ,    cosine_similarity(cat ,dog))     # 0.29