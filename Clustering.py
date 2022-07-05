import random
import math
import matplotlib.pyplot as plt
s = {}
tis = 0
with open(r"Churn_Modelling.csv", 'r') as f:
    hdr = f.readline()
    hdr = hdr.split(",")
  

    columns = []
    columns.append(hdr[8])
    columns.append(hdr[12])

    k = tis = 7

    data_list=[]
    #Loop this over the first 10000 rows and get the data points in form of list of lists
    #for i in range(20):
    while f.readline()!='': 
        p = f.readline().split(",")
        
        data_list.append([p[8], p[12]])
        
    
   
    #Doing this to get unique centroid values
    while True:
        #It is list of centroids which are tuples
        init_centroids = []
        r = random.sample(range(0, len(data_list)), k)
        for i in r:
            init_centroids.append(tuple(data_list[i]))

        #This will be true when all centroid values are unique
        if len(init_centroids) == len(set(init_centroids)):
            break

    print("Initial Centroid:",init_centroids)
    print()
    iterations = 300
    crt = 0
    for i in range(iterations):
        crt +=1
        clusters = {}
        #Make the elements of init_centroids the keys
        for i in init_centroids:
            clusters[i] = []

        for i in data_list:
            #Dummy Value as in infinity
            min_val = 10000000000
            for j in init_centroids:
                val = math.sqrt((float(i[0])-float(j[0]))*(float(i[0])-float(j[0])) + (float(i[1])-float(j[1]))*(float(i[1])-float(j[1])))
                if val<min_val:
                    min_val = val
                    min_pt = i
                    #key
                    ctrd = j
            clusters[ctrd].append(tuple(i))

        new_centroids = []
        for i in clusters.keys():
            x_val = 0
            y_val = 0
            for j in clusters[i]:
                x_val += float(j[0])
                y_val += float(j[1])
            x_val = x_val//len(clusters[i])
            y_val = y_val//len(clusters[i])
            tup = (x_val, y_val)
            new_centroids.append(tup)
        

        for values in clusters:
            print()
            print(values , ": ",  clusters[values])
            print()
        if set(new_centroids) == set(init_centroids):
            break
        init_centroids = new_centroids
        print("new Centroids:")
        print(new_centroids)
        print()
        s = clusters
    
    

data_list = list(data_list)
x = []
y = []

for i in data_list:
   x.append(float(i[0]))
   y.append(float(i[1]))


plt.scatter(x,y,c='black',label='unclustered data')
plt.xlabel('Balance')
plt.ylabel('Estimated Salary')
plt.legend()
plt.title('Plot of data points')
plt.show()

t = []
    
centroids = []
for k in s:
    centroids.append(k)
Cen_x = []
Cen_y = []
for i in centroids:
    Cen_x.append(float(i[0]))
    Cen_y.append(float(i[1]))

labels=[]
T = 0 
for k in s:
    t.append(s[k])
h = 0
for i in t:
    X =[]
    Y = []
    color = ['red', 'blue', 'pink', 'green', 'yellow', 'black','orange','grey','magenta','beige']
    # r = random.random()
    # g = random.random()
    # b = random.random()
    colors =[]
    b = 0
    while b < tis:
        colors.append(color[b])
        labels.append(b+1)
        b+=1

    for k in i:
        X.append(float(k[0]))
        Y.append(float(k[1]))
    
    plt.scatter(X,Y,c=colors[h],label=labels[T])
    h += 1
    
    T+=1
plt.scatter(Cen_x,Cen_y,c= 'brown',s = 200, label='Centroids')


plt.xlabel('Balance ')
plt.ylabel('Estimated Salary')


plt.legend()
plt.show()