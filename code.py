#GP106-computing_group_project
#Group 101 - E/18/301, E/18/302, E/18/303
#11/12/2020

#import required libraries
import math
import argparse
import time

#unit convertion

#convert cm to m
def cm_to_m(len1):
    return len1/100

#convert inches to m
def in_to_m(len2):
    return len2*0.0254

#convert lb to kg
def lb_to_kg(w1):
    return w*0.45359237

#convert minutes to seconds
def min_to_sec(t1):
    return t1*60

#convert hours to seconds
def h_to_sec(t2):
    return t2*3600

#Calculations

#speed
def speed(radius,rev):
    return (2*math.pi*rev*radius)/60

#distance
def distance(time,radius,rev):
    return speed(radius,rev)*time


#calories burnt
def calories(weight,time,radius,rev):
    velo = speed(radius,rev)
    if velo<1.65405:
        oxygen= (0.1 * velo * 60)+ 3.5
    else:
        oxygen= (0.2 * velo * 60)+ 3.5
    return (oxygen * weight * (time/60))/200


#number of steps taken
def steps(height,time,radius,rev):
    return (distance(time,radius,rev))/(0.413*height)



# Don't change the the code below this point
if __name__=="__main__":

    args=argparse.ArgumentParser()
    args.add_argument("--motor", type=int, dest="motor_rate", help="EXAMPLE: 3", default=3)
    args.add_argument("--radius", type=str, dest="radius", help="EXAMPLE: 8 cm", default="8 cm")
    args.add_argument("--weight", type=str, dest="weight", help="EXAMPLE: 50 kg", default="50 kg")
    args.add_argument("--height", type=str, dest="height", help="EXAMPLE: 63 in", default="63 in")
    
    args=args.parse_args()

# Don't change the the code above this point

#all the inputs should be in "value unit" format. ex: "20 cm"
#Assume that combined units will not be given (eg: 1m 50cm)



motor_rev=args.motor_rate

#seperate values and units

list_radius = args.radius.split()

list_weight= args.weight.split()

list_height= args.height.split()




#get radius in meters

try:
    if list_radius[1]=="m":
        radius=float(list_radius[0])
    elif list_radius[1]=="cm":
        radius=cm_to_m(float(list_radius[0]))
    elif list_radius[1]=="in":
        radius=in_to_m(float(list_radius[0]))
    else:
        print(" input for radius should be in m,cm,in only")

except:
    print("wrong input for radius")



#get weight in kilograme
try:
    
    if list_weight[1]=="kg":
        weight=float(list_weight[0])
    elif list_weight[1]=="lb":
        weight=lb_to_kg(float(list_weight[0]))
    else:
        print(" input for weight should be in kg,lb only")

except:
    print("wrong input for weight")

#get height in meters
try:
    
    if list_height[1]=="m":
        height=float(list_height[0])
    elif list_height[1]=="cm":
        height=cm_to_m(float(list_height[0]))
    elif list_height[1]=="in":
        height=in_to_m(float(list_height[0]))
    else:
        print(" input for height should be in m,cm,in only")

except:
    print("wrong input for height")

#start time
start_time = time.time()


#make a infinite loop to get the real time values
while True:
    
    end_time= time.time()

    #time difference
    timeDifference = end_time- start_time
    

    #calculate the "speed/distance/calories burnt/steps walk" with respect to time

    v=speed(radius,motor_rev)#speed

    d=distance(timeDifference,radius,motor_rev)#distance

    c=calories(weight,timeDifference,radius,motor_rev)#calories burnt

    s=steps(height,timeDifference,radius,motor_rev)#number of steps

    print(int(v),"m/s")
    print(int(d),"m")
    print(int(c),"cal")
    print(int(s))

    print("\n") #keep space to make data seperate to view easier