def accountsMerge(accounts):
    # Build the graph
    graph = {}
    for account in accounts:
        name = account[0]
        for email in account[1:]:
            if email not in graph:
                graph[email] = set()
            graph[email].add(account[1])  # Add the first email as a representative

            graph[account[1]].add(email)  # Add other emails

    # DFS function to traverse the graph
    def dfs(email, visited, component):
        visited.add(email)
        component.append(email)
        for neighbor in graph[email]:
            if neighbor not in visited:
                dfs(neighbor, visited, component)

    merged_accounts = []
    visited = set()
    for email in graph:
        if email not in visited:
            component = []
            dfs(email, visited, component)
            merged_accounts.append([accounts[0][0]] + sorted(component))

    return merged_accounts

# Example usage:
accounts1 = [["John","johnsmith@mail.com","john_newyork@mail.com"],
             ["John","johnsmith@mail.com","john00@mail.com"],
             ["Mary","mary@mail.com"],
             ["John","johnnybravo@mail.com"]]
print(accountsMerge(accounts1))

accounts2 = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
             ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
             ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
             ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m
