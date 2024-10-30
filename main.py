import heapq

def min_connection_cost_with_order(cables):
    # Ініціалізуємо чергу з пріоритетом (heap) з даними довжинами кабелів
    heapq.heapify(cables)
    
    # Змінна для підрахунку загальних витрат
    total_cost = 0
    
    # Список для збереження порядку об'єднання
    connection_order = []
    
    # Поки залишилося більше одного кабелю
    while len(cables) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Вартість з'єднання цих двох кабелів
        cost = first + second
        total_cost += cost
        
        # Додаємо інформацію про об'єднання до списку порядку
        connection_order.append((first, second, cost))
        
        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)
    
    return total_cost, connection_order


cables = [4, 3, 2, 6]
total_cost, connection_order = min_connection_cost_with_order(cables)

print("Мінімальна вартість з'єднання кабелів:", total_cost)
print("Порядок об'єднання кабелів:")
for first, second, cost in connection_order:
    print(f"З'єднання {first} + {second} = {cost}")
