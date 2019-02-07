import matplotlib.pyplot as plt
import numpy as np

def fit_linear(filename):   #part 1
   def chick_row (data):
    for itam in data[0:len(data)-2]:
        chicked = item.strip("\n").lower().split()
        xx = chicked[0]
        if xx =="x":
            x= list(map(float,chiched[1:]))
        elif xx== "Y":
            Y= list(map(float,chicked[1:]))
        elif xx =="Dx":
            Dx = list (map(float,chicked[1:]))
        elif xx = "dY":
            dY = list(map(float,chicked[1:]))
    if len(x) != len(Y) or len(x) != len(dY) or len(x) != len(Dx):
        print("“Input file error: Data lists are not the same length")
        exit()
    for check2 in Dx:
         if check2 <=0:
            print ("Input file error: Not all uncertainties are positive.")
            exit()
    for check2 in dY:
         if check2 <=0:
            print ("Input file error: Not all uncertainties are positive.")
            exit()
    return (x,Y,Dx,dY)

def column(data):
    checked_data=[]
    for item in data [:len(data)-2]:
        checked = item.strip('\n').lower().split()
        checked_data.append(checken)
    column= len(checked_data[0])
    row= len(checked_data)
    data_che=[]
    try:
        for k in range (column):
            lis=[]
            for i in range (row):
                lis.append(checked_data[i][k])
            data_che.append(lis)
    except:
        print("not the same length.")
        exit()
    for z in data_che :
        xx= z[0]
        if xx == "x":
             x = list(map(float, chiched[1:]))
        elif xx == "Y":
             Y = list(map(float, chicked[1:]))
        elif xx == "Dx":
             Dx = list(map(float, chicked[1:]))
        elif xx = "dY":
             dY = list(map(float, chicked[1:]))
    for check2 in Dx:
         if check2 <=0:
            print ("Input file error: Not all uncertainties are positive.")
            exit()
    for check2 in dY:
         if check2 <=0:
            print ("Input file error: Not all uncertainties are positive.")
            exit()
    return (x,Y,Dx,dY)

data_file="all data.txt"
file=open(data_file)
data = file.readline()
x_list = ['x','Y','Dx' ,'dY']
su=0
y_title= data[len(data)-1].strip("Y title")
x_title= data[len(data)-1].strip("x title")
for item in x_list :
    if item in data[0]:
         su=su+1
if su==4:
    k =input_column(data)
else:
    input_chick_row (data)
print (k)






def function_a(x,Y,dY):  #part 2
    xyavg=0
    sumdy=0
    for i in range(0,len(x)):
        xyavg=xyavg+(x[i]*Y[i])/(dY[i]**2)
        sumdy=sumdy+(1/(dY[i]**2))
    xyavg=xyavg/(sumdy)
    xavg=0
    xavgpow = 0
    for i in range(0,len(x)):
        xavg=xavg+(x[i]/(dY[i]**2))
        xavgpow = xavgpow+(x[i]**2/(dY[i]**2))
    xavg=xavg/(sumdy)
    xavgpow=xavgpow/(sumdy)
    yavg=0
    for i in range(0,len(Y)):
        yavg=yavg+(Y[i]/(dY[i]**2))
    yavg=yavg/(sumdy)

    return ((xyavg-(xavg*yavg))/(xavgpow-(xavg**2)))
def function_da(x,dY):
    dyavgpow=0
    sumdy = 0
    K=0
    for i in range(0,len(dY)):
        dyavgpow=dyavgpow+((dY[i] ** 2)/dY[i] ** 2)
        sumdy=sumdy+(1/(dY[i]**2))
        K=K+1
    dy_power_avarage = dyavgpow / (sumdy)
    xavg = 0
    xavgpow = 0
    for i in range(0, len(x)):
        xavg = xavg + (x[i] / (dY[i] ** 2))
        xavgpow = xavgpow + (x[i] ** 2 / (dY[i] ** 2))
    xavg = xavg / (sumdy)
    xavgpow = xavgpow /(sumdy)

    return ((dyavgpow/(K*(xavgpow-(xavg**2)))))**(0.5)
def function_b(Y,a,x,dY):
    sumdy = 0
    yavg=0
    for i in range(0,len(Y)):
        yavg=yavg+(Y[i]/(dY[i]**2))
        sumdy = sumdy + (1 / (dY[i] ** 2))
    yavg=yavg/(sumdy)
    xavg = 0
    for i in range(0, len(x)):
        xavg = xavg + (x[i] / (dY[i] ** 2))
    xavg = xavg / (sumdy)

    return yavg-a*xavg
def function_db(x,dY):
    dyavgpow = 0
    sumdy = 0
    K = 0
    for i in range(0, len(dY)):
        dyavgpow = dyavgpow + ((dY[i] ** 2) / dY[i] ** 2)
        sumdy = sumdy + (1 / (dY[i] ** 2))
        K = K+ 1
    dyavgpow = dyavgpow / (sumdy)
    xavg = 0
    xavgpow = 0
    for i in range(0, len(x)):
        xavg = xavg + (x[i] / (dY[i] ** 2))
        xavgpow = xavgpow + (x[i] ** 2 / (dY[i] ** 2))
    xavg = xavg / (sumdy)
    xavgpow = xavgpow / (sumdy)

    return ((dyavgpow)*(xavgpow) / (K * (xavgpow - (xavg ** 2))))**(0.5)
def function_chi2red(chi,x):
    K=0
    for i in range(0,len(x)):
        K=K+1
    return chi/(K-2)


def function_chi2(Y,a,b,x,dY):
    Chi2=0
    for i in range(0,len(x)):
        Chi2=Chi2+((Y[i]-(a*x[i]+b))/(dY[i]))**2
    return Chi2
a=function_a(x,Y,dY)
b=function_b(Y,a,x,dY)
chi=function_chi2(Y,a,b,x,dY)
print(function_a(x,Y,dY))
print(function_da(x,dY))
print(function_b(Y,a,x,dY))
print(function_db(x,dY))
print(function_chi2(Y,a,b,x,dY))
print(function_chi2red(chi,x))




print("a=", function_a, "+-", function_da)  #part 3
print("b=", function_b, "+-", function_db)
print("chi2=", function_chi2)
print("chi2_reduced=", function_chi2_reduced)




def the_name_of_lables(axis_titles):   #part 4
    x_title = ''
    y_title = ''

    for item in axis_titles:
        for i in range(len(axis_titles)):

            item = item.lower().strip()
            if item.startswith('x axis:'):
                x_title= axis_titles[i][6:].strip()
            if line.startswith('y axis:'):
                y_title= axis_titles[i][6:].strip()
    return x_title, y_title
    
    
    
import matplotlip.pyplot as plt
from numy imprort np
x = np.array(X)  #row
my_y = np.array(Y)
formula = a * x + b
xe = np.array(DX)
ye = np.array(DY)
y = formula
plt.errorbar(x, my_y, ye=ye, xe=xe, fmt='none', ecolor='b')
plt.plot(x, y, "r")
plt.xlabel(xlabel=Xlable)
plt.ylabel(ylabel=Ylable)
plt.show()
plt.savefig("linear_fit.svg")
my_file.close()


x = np.array(X)#column
my_y = np.array(Y)
formula = a * x + b
xe = np.array(DX)
ye = np.array(DY)

y = formula
plt.errorbar(x, my_y, ye=ye, xe=xe, fmt='none', ecolor='b')
plt.plot(x, y, "r")
plt.xlabel(xlabel=Xlable)
plt.ylabel(ylabel=Ylable)
plt.show()
plt.savefig("linear_fit.svg")
my_file.close()
    
