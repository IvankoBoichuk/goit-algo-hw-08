import heapq

def min_connection_cost(cables):
    # Ініціалізуємо мін-купу
    heapq.heapify(cables)
    
    total_cost = 0

    # Об'єднуємо, поки залишиться один кабель
    while len(cables) > 1:
        # Дістаємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість об'єднання двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost

print(min_connection_cost([4, 3, 2, 6]))  # 58