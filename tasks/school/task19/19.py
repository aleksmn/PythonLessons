def solve():
    # Чтение входных данных
    with open(r'tasks\school\task19\19.txt', 'r') as f:
        P, N = map(int, f.readline().split())
        weights = [int(f.readline()) for _ in range(N)]
        print(weights)

    # Сортируем веса по возрастанию
    weights.sort()


    # Шаг 1: Находим максимальное количество пакетов k
    # (первые k самых легких пакетов)
    prefix_sum = 0
    k = 0
    for i in range(N):
        if prefix_sum + weights[i] <= P:
            prefix_sum += weights[i]
            k += 1
        else:
            break

    print(prefix_sum, k)
    # Если нельзя взять ни одного пакета
    if k == 0:
        print(0, 0)
        return

    # Шаг 2: Находим максимальный возможный вес самого тяжелого пакета
    # Сумма k-1 самых легких пакетов
    sum_k_minus_1 = sum(weights[:k-1]) if k-1 > 0 else 0

    # Ищем максимальный i, такой что sum_k_minus_1 + weights[i] <= P
    # i должно быть >= k-1, потому что после взятия k-1 самых легких,
    # самый тяжелый пакет может быть любым, начиная с позиции k-1 и далее
    max_weight = 0
    for i in range(k-1, N):
        if sum_k_minus_1 + weights[i] <= P:
            max_weight = weights[i]
        else:
            break

    print(k, max_weight)


if __name__ == "__main__":
    solve()
