def mochila(pesos, valores, capacidade):
    n = len(pesos)
    dp = [[0] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacidade + 1):
            if pesos[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - pesos[i - 1]] + valores[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacidade]

pesos = [1, 2, 3, 4, 1]
valores = [1, 3, 4, 5, 3]
capacidade = 5
print(mochila(pesos, valores, capacidade))
