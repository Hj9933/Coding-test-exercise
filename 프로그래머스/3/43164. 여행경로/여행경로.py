from collections import deque
def solution(tickets):
    answer = []
    for ticket in tickets:
        ticket.append(0) # 방문표시 위해
    tickets.sort(key=lambda x: x[1])
    length = len(tickets)+1
    t = ["ICN"]

    def dfs(start):
        for ticket in tickets:
            if ticket[0] == start and ticket[2] == 0:
                t.append(ticket[1])
                ticket[2] = 1
                if len(t) == length or dfs(ticket[1]):
                    return t
                ticket[2] = 0
                t.pop()
    answer = dfs("ICN")

    return answer