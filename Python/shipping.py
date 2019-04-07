# This program finds the lowest shipping method

premium = 125.00

def ground(weight):
    if weight <= 2:
        return weight*1.5+20
    elif (weight > 2) and (weight <= 6):
        return weight*3+20
    elif (weight > 6) and (weight <= 10):
        return weight*4+20
    elif (weight > 10):
        return weight*4.75+20
    else:
        return "Could not calculate Ground Shipping"
                                    
def drone(weight):
    if weight <= 2:
        return weight*4.5
    elif (weight > 2) and (weight <= 6):
        return weight*9
    elif (weight > 6) and (weight <= 10):
        return weight*12
    elif (weight > 10):
        return weight*14.25
    else:
        return "Could not calculate Drone Shipping"
                                                       
def cheapest(weight):
    if (ground(weight) < drone(weight)) and (ground(weight) < premium):
        return "Ground Shipping at: " +str(ground(weight))
    elif (drone(weight) < ground(weight)) and (drone(weight) < premium):
        return "Drone Shipping at: " + str(drone(weight))
    elif (premium < ground(weight)) and (premium < drone(weight)):
        return "Premium Shipping at: " + str(premium)
    else:
        return "Could not calculate the cheapest price"
