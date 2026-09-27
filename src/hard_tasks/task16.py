def MaximumDiscount(N:int, price: list[int]) -> int:
    res: int = 0
    price.sort(reverse=True)
    for i in range(2, N, 3):
        res += price[i]
    return res
