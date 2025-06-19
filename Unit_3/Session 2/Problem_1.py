def manage_stage_changes(changes):
    scheduled = []
    canceled = []

    for i in changes:   
        parts = i.split(maxsplit=1)
        actions = parts[0]
        
        if actions == "Schedule":
            scheduled.append(parts[1])
        
        elif actions == "Cancel":
            canceled.append(scheduled.pop())
            
        elif actions == "Reschedule":
            scheduled.append(canceled.pop())
            
    return scheduled                
    pass
print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 