"""
Leetcode Problem #: 983
Leetcode Problem: Minimum Cost For Tickets
Difficulty: Medium

For each travel day, we can buy a one-day ticket, or use 7-day or 
30-day pass as if we would have purchased it 7 or 30 days ago. We 
need to track rolling costs for at least 30 days back, and use them 
to pick the cheapest option for the next travel day.

Here, we can use two solutions: EITHER track cost for all calendar days, 
OR process only travel days. The first one is simpler to implement, 
but it's slower. The second one is ideally more optimized.

For the second solution, we will use queue to store the cost of the days since 
it's a FIFO data structure.
"""

# First solution: Track cost for all calendar days
class Solution:
    def mincostTickets(self, days, costs):
        calendarDays = 365
        daysSet = set(days)

        # Use an array to track min cost for all calendar days. 
        calendarDaysTable = [0] * (calendarDays + 1)
        
        for i in range(1, calendarDays + 1):
            if i not in daysSet:
                calendarDaysTable[i] = calendarDaysTable[i - 1]
            else:
                calendarDaysTable[i] = min(calendarDaysTable[i - 1] + costs[0],
                                           calendarDaysTable[max(i - 7, 0)] + costs[1],
                                           calendarDaysTable[max(i - 30, 0)] + costs[2])
        return calendarDaysTable[calendarDays]


# Second solution: Process only travel days
class Solution:
    def mincostTickets(self, days, costs):
        from collections import deque

        last7 = deque()
        last30 = deque()
        cost = 0

        for day in days:
            while last7 and last7[0][0] + 7 <= day:
                last7.popleft()
            while last30 and last30[0][0] + 30 <= day:
                last30.popleft()
            last7.append((day, cost + costs[1]))
            last30.append((day, cost + costs[2]))
            cost = min(cost + costs[0], last7[0][1], last30[0][1])
        return cost
            