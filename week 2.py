print("welcome")
# /n gives the code on a new line
# /t gives a backslash before the output of the code
distance_to_point_in_km = 75
waiting_time_before_leaving = 0.25
travel_type = "riding"
walking = 5
cycling = 20
riding = 60

final_walking_time = (((distance_to_point_in_km / walking) * 60) + waiting_time_before_leaving) / 60
final_cycling_time = (((distance_to_point_in_km / cycling) * 60) + waiting_time_before_leaving) / 60
final_riding_time = (((distance_to_point_in_km / riding) * 60) + waiting_time_before_leaving) / 60


if travel_type == "walking" :
    print("Your walking time to your destination is ", final_walking_time, "hours")
elif travel_type == "cycling" :
    print("Your cycling time to your destination is ", final_cycling_time, "hours")
elif travel_type == "riding":
    print("Your riding time to your destination is ", final_riding_time, "hours")




