def solution(bridge_length, weight, truck_weights):
    list=[0 for i in range(bridge_length-1)]
    sum=0
    sec=0
    
    while truck_weights and list:
        if sum + truck_weights[0] <= weight:
            list.append(truck_weights[0])
            sum += truck_weights.pop(0)      
        else:
            list.append(0)
        sum-=list.pop(0)
        sec+=1
        
    return sec+bridge_length