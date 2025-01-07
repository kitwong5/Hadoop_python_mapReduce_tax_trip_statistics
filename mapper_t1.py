#!/usr/bin/env python3
import sys

# Consider three types of taxi trips:
# short trips <100;
# medium trips >=100 and <200; 
# long trips>=200; 

# Perform the follow count for each taxi and each type of trips
# (i) the total number of trips
# (ii) the maximum fare of trips
# (iii) the minimum fare of trips
# (v) the average fare per trip

mylist = [];
# input comes from standard input STDIN
for line in sys.stdin:
    # remove leading and trailing whitespaces
    line = line.strip() 
    # split the line into values
    trip_no, taxi_no, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y = line.split(",") 

    # assign trip type
    if float(distance)<100: trip_type = "short_trips" 
    elif float(distance)>=100 and float(distance)<200: trip_type = "medium_trips" 
    elif float(distance)>=200:trip_type = "long_trips"   
    else: trip_type = None

    # perform in-mapper combining
    flag = False
    i=0
    min_fare = 0
    max_fare = 0
    for ml in mylist: 
        ml_item = ml.split(" ")
        ml_taxi_no = ml_item[0]
        ml_trip_type = ml_item[1]
        ml_max_fare = ml_item[2]
        ml_min_fare = ml_item[3]
        ml_fare = ml_item[4]
        ml_count = ml_item[5]
        # for taxi_no and trip type already exist in mylist, perform update on fare and counter
        if taxi_no == ml_taxi_no and trip_type == ml_trip_type:
            # define total fare and latest counter
            new_fare = float(ml_fare) + float(fare)
            new_count = int(ml_count) + 1
            # define max_fare and min_fare
            if float(fare) > float(ml_max_fare):
                max_fare = float(fare)
            else:
                max_fare = float(ml_max_fare)
            if float(fare) < float(ml_min_fare):
                min_fare = float(fare)
            else:
                min_fare = float(ml_min_fare)
            # update mylist with latest values
            mylist[i] = ml_taxi_no+" "+ml_trip_type+" "+str(round(max_fare,3))+" "+str(round(min_fare,3))+" "+str(round(new_fare,3))+" "+str(new_count)
            flag = True
            break
        i = i + 1
    # for taxi_no and trip type no need to perfrom combine, store fare and counter in mylist 
    if not flag:
        mylist.append(taxi_no+" "+trip_type+" "+fare+" "+fare+" "+fare+" "+"1")    

# emit pairs <taxi_no, trip_type, fare, counter>   
for ml in mylist:
    ml_item = ml.split(" ") 
    print('%s\t%s\t%s\t%s\t%s\t%s' % (ml_item[0],ml_item[1],ml_item[2],ml_item[3],ml_item[4],ml_item[5]))
#    print('%s\t%s\t%s\t%s' % (taxi_no,trip_type,fare,"1")) #Emit <taxi_no,trip_type,max_fare,min_fare,fare,counter> pairs  
