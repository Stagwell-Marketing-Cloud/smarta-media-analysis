def sc_integration(row):
    scene_change_flag = 0
    
    if row["integration_ts"][1] != 0:
        for j in range(len(row["scenes"])):
            if row["integration_ts"][0] < row["scenes"][j][0] and row["integration_ts"][1] > row["scenes"][j][1]:
                scene_change_flag = 1
                break
    
    return scene_change_flag



### Integration
def integration_between(ts, lower_bound, upper_bound):
    return 1 if (ts >= lower_bound and ts <= upper_bound) else 0

