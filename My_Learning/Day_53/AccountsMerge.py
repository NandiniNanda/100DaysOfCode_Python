from collections import defaultdict

def accountsMerge(accounts):
    # Build the graph
    graph = defaultdict(list)
    email_to_name = {}
    for account in accounts:
        name = account[0]
        emails = account[1:]
        for email in emails:
            graph[emails[0]].append(email)
            graph[email].append(emails[0])
            email_to_name[email] = name
    
    # Perform DFS to traverse connected components
    def dfs(email, component):
        component.add(email)
        for neighbor in graph[email]:
            if neighbor not in component:
                dfs(neighbor, component)
    
    # Perform DFS for each email
    visited = set()
    result = []
    for email in graph:
        if email not in visited:
            component = set()
            dfs(email, component)
            result.append([email_to_name[email]] + sorted(component))
            visited.update(component)
    
    return result

# Test cases
accounts1 = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
accounts2 = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]

print(accountsMerge(accounts1))
print(accountsMerge(accounts2))
