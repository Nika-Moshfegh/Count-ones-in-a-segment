def count_ones(left, right):
    def count_up_to(n):
        if n < 0:
            return 0

        total = 0
        bit = 1

        while bit <= n:
            cycle = bit * 2
            full_cycles = (n + 1) // cycle
            remainder = (n + 1) % cycle

            total += full_cycles * bit
            total += max(0, remainder - bit)

            bit <<= 1

        return total

    return count_up_to(right) - count_up_to(left - 1)


print(count_ones(4,7))