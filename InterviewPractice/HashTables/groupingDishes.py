def solution(dishes):
    d = {}
    for i in range(len(dishes)):
        dish = dishes[i][0]
        ingredients = dishes[i][1:]
        for ingredient in ingredients:
            if ingredient not in d:
                d[ingredient] = []
            d[ingredient].append(dish)
    candidates = []
    for key, value in d.items():
        if len(value) >= 2:
            candidates.append(key)
    candidates.sort()
    result = []
    for name in candidates:
        line = [name] + sorted(d[name])
        result.append(line)
    return result


dishes = [
    ["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
    ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
    ["Quesadilla", "Chicken", "Cheese", "Sauce"],
    ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"],
]
assert solution(dishes) == [
    ["Cheese", "Quesadilla", "Sandwich"],
    ["Salad", "Salad", "Sandwich"],
    ["Sauce", "Pizza", "Quesadilla", "Salad"],
    ["Tomato", "Pizza", "Salad", "Sandwich"],
]

dishes = [
    ["Pasta", "Tomato Sauce", "Onions", "Garlic"],
    ["Chicken Curry", "Chicken", "Curry Sauce"],
    ["Fried Rice", "Rice", "Onions", "Nuts"],
    ["Salad", "Spinach", "Nuts"],
    ["Sandwich", "Cheese", "Bread"],
    ["Quesadilla", "Chicken", "Cheese"],
]
assert solution(dishes) == [
    ["Cheese", "Quesadilla", "Sandwich"],
    ["Chicken", "Chicken Curry", "Quesadilla"],
    ["Nuts", "Fried Rice", "Salad"],
    ["Onions", "Fried Rice", "Pasta"],
]
