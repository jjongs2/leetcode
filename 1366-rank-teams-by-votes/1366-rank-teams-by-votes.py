class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])
        scores = dict()
        for vote in votes:
            for i, team in enumerate(vote):
                scores.setdefault(team, [0] * n)[i] -= 1
        return "".join(team for team, _ in sorted(scores.items(), key=lambda x: (x[1], x[0])))
