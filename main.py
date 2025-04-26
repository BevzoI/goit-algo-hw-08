import heapq

def min_cost_to_connect_cables(cables):
    if not cables:
        return 0

    heapq.heapify(cables)  
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)  # Найкоротший кабель
        second = heapq.heappop(cables) # Другий найкоротший кабель
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)   # Новий об'єднаний кабель назад у купу

    return total_cost

# Приклад використання:
cables = [8, 4, 6, 12]
print("Мінімальні загальні витрати:", min_cost_to_connect_cables(cables))
