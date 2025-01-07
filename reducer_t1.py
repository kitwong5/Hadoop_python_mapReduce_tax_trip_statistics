#!/usr/bin/env python3
import sys

# count the number of trip, max fare, min fare, avg fare for each taxi and type of trips 
# That is, taxi_no trip_type is the key. 

# initize values
curr_taxi_no = None
curr_trip_type = None
curr_count = 0
curr_fare = 0
trip_type_count = None
min_fare = 0
max_fare = 0

# input comes from STDIN
for line in sys.stdin:
    # strip line into values
    line = line.strip()
    map_taxi_no,map_trip_type,map_max_fare,map_min_fare,map_fare,map_count = line.split('\t')
    # convert string to numberic values
    try:
        map_count = int(map_count)
        map_fare = float(map_fare)
        map_max_fare = float(map_max_fare)
        map_min_fare = float(map_min_fare)
    except ValueError:
        continue
    if curr_trip_type == map_trip_type and curr_taxi_no == map_taxi_no:# for same taxi_no and trip_type 
        curr_count += map_count
        curr_fare += map_fare
        if map_max_fare > max_fare:
            max_fare = map_max_fare
        if map_min_fare < min_fare:
            min_fare = map_min_fare
    else:# for new taxi no or trip type 
        if curr_taxi_no: #emit pervious line values before assign values for new line
               print('%s\t%s\t%s\t%s\t%s\t%s' % (curr_taxi_no, curr_trip_type, curr_count, max_fare, min_fare, round(curr_fare/curr_count,2)))
        # assign values for the new taxi_no or trip_type
        curr_count = map_count
        curr_trip_type = map_trip_type
        curr_taxi_no = map_taxi_no
        curr_fare = map_fare
        min_fare = map_min_fare
        max_fare = map_max_fare
if curr_trip_type == map_trip_type and curr_taxi_no == map_taxi_no: #emit the last line
    print('%s\t%s\t%s\t%s\t%s\t%s' % (curr_taxi_no, curr_trip_type, curr_count, round(max_fare,2), round(min_fare,2), round(curr_fare/curr_count,2)))