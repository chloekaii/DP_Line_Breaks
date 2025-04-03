def get_line_length(w, b, i, j):
    line_len = 0
    for k in range(i, j + 1):
        line_len += w[k]
    return line_len + (j - i) * b


def get_slack_squared(l, line_len):
    return (l - line_len) ** 2


def optimal_line_breaking(w, b, l, n, i, min_slack, break_at):
    if i > n - 1:  # out of bounds
        return 0

    if min_slack[i] is not None:  # prevents unnecessary recursion
        return min_slack[i]

    res = float("inf")
    for j in range(i, n):
        line_len = get_line_length(w, b, i, j)

        if line_len > l:  # line too long
            break

        slack = get_slack_squared(l, line_len)
        # i guess get_slack_squared and get_line_length are kind of unnecessary, but since i defined
        # helper functions in my recurrence equation i am keeping it for my brain's sake

        if j == n - 1:  # last line
            res = 0
            break_at[i] = n
        else:  # 2 options: break after current word or dont
            break_at_slack = slack + optimal_line_breaking(w, b, l, n, j + 1, min_slack, break_at)
            if break_at_slack < res:  # when break was optimal
                res = break_at_slack
                break_at[i] = j + 1

    min_slack[i] = res
    return res


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        w = list(map(int, file.readline().split()))
        b = int(file.readline())
        l = int(file.readline())

    n = len(w)
    min_slack = [None] * n  # keeps track of the minimum cost
    break_at = [None] * n  # keeps track of where line breaks should occur

    optimal_line_breaking(w, b, l, n, 0, min_slack, break_at)
    break_at = list(set(break_at))  # get rid of duplicate line breaks

    print(f"Minimum slack: {min_slack[0]}")
    print(f"Optimal line breaks: {break_at}")
