def greedy_algorithm(items, budget):
    initial_budget = budget
    # Сортування елементів за співвідношенням калорійності до вартості у спадному порядку
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    chosen_items = []

    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            chosen_items.append(item)

    return {"items": chosen_items,
            "total_cal": total_calories,
            "budget_spent": initial_budget - budget}


def dynamic_programming(items, budget):
    # Ініціалізація таблиці DP
    n = len(items)
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    item_list = list(items.items())

    # Побудова таблиці DP
    for i in range(1, n + 1):
        for w in range(1, budget + 1):
            cost = item_list[i - 1][1]['cost']
            calories = item_list[i - 1][1]['calories']
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]

    # Визначення вибраних страв
    chosen_items = []
    total_calories = dp[n][budget]
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            chosen_items.append(item_list[i - 1][0])
            w -= item_list[i - 1][1]['cost']

    chosen_items.reverse()
    return {"items": chosen_items,
            "total_cal": total_calories,
            "budget_spent": budget}

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
print(greedy_algorithm(items, budget))
# {'items': ['cola', 'potato', 'pepsi', 'hot-dog'], 'total_cal': 870, 'budget_spent': 80}
print(dynamic_programming(items, budget))
# {'items': ['pizza', 'pepsi', 'cola', 'potato'], 'total_cal': 970, 'budget_spent': 100}
