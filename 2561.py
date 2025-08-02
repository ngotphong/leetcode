from collections import Counter

def minCost(basket1, basket2):
    freq = Counter(basket1)
    freq.subtract(Counter(basket2))
    to_swap = []
    for fruit_cost, count in freq.items(): # going through the differences for different fruits 
        if count % 2 != 0:
            return -1
        for _ in range(abs(count) // 2):
            to_swap.append(fruit_cost)
    to_swap.sort()
    min_overall_fruit = min(basket1 + basket2)
    cost = 0
    for i in range(len(to_swap) // 2):
        direct_swap_cost = to_swap[i]
        indirect_swap_cost = 2 * min_overall_fruit
        cost += min(direct_swap_cost, indirect_swap_cost)
    return cost

print(minCost([1,2,3,4,5], [5,4,3,2,1]))
print(minCost([84,80,43,8,80,88,43,14,100,88],
[32,32,42,68,68,100,42,84,14,8]))