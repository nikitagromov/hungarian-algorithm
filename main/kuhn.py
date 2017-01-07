
def kuhn(g):
    matching = [-1 for row in g]
    used = [False for row in g]

    def fill(array, value):
        return [value for item in array]

    def dfs(v):
        if used[v]:
            return False
        used[v] = True
        for to, item in enumerate(g[v]):
            if g[v][to] and (matching[to] == -1 or dfs(matching[to])):
                matching[to] = v
                return True
        return False

    for i in range(0, len(g)):
        used = fill(used, False)
        dfs(i)
    return matching

