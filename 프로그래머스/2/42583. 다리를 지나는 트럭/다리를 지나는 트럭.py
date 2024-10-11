from collections import deque
def solution(bridge_length, weight, truck_weights):
    truck = deque(truck_weights)
    n = len(truck_weights)
    on_bridge = deque([])
    cnt = 0
    time = 0
    weights = deque([])
    weight_sum = 0
    while truck:
        time += 1
        if cnt < bridge_length and weight_sum + truck[0] <= weight:
            on_bridge.append(0)
            tmp = truck.popleft()
            weights.append(tmp)
            weight_sum += tmp
            cnt += 1
        for j in range(len(on_bridge)):
            on_bridge[j] += 1
        if on_bridge[0] == bridge_length:
            on_bridge.popleft()
            weight_sum -= weights.popleft()
            cnt -= 1
    time += bridge_length
    return time