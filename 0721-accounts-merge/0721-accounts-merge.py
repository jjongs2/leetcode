from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = dict()

        def find(v):
            while (p := parents[v]) != v:
                parents[v] = parents[p]
                v = parents[p]
            return v

        def union(v1, v2):
            parents[find(v2)] = parents[find(v1)]

        owners = dict()
        for name, *emails in accounts:
            primary_email = emails[0]
            for email in emails:
                if email not in parents:
                    parents[email] = email
                owners[email] = name
                union(primary_email, email)
        merged = defaultdict(list)
        for v in parents:
            merged[find(v)].append(v)
        return [[owners[root], *sorted(emails)] for root, emails in merged.items()]
