class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def formula_cross(l, n, c):
            return ((n[1] - l[1]) * (c[0] - n[0])) - ((n[0] - l[0]) * (c[1] - n[1]))
        def in_between(l, n, c):
            x = ((l[0] <= n[0]) and (c[0] >= n[0])) or ((l[0] >= n[0]) and (c[0] <= n[0]))
            y = ((l[1] <= n[1]) and (c[1] >= n[1])) or ((l[1] >= n[1]) and (c[1] <= n[1]))
            return x and y
        if len(trees) < 4:
            return trees
        fenced_trees = set()
        left_most = 0
        for tree in range(len(trees)):
            if trees[tree][0] < trees[left_most][0]:
                left_most = tree
        l = left_most
        initial = True
        while initial or l != left_most:
            initial = False
            n = (l + 1) % len(trees)
            for c in range(len(trees)):
                if formula_cross(trees[l], trees[c], trees[n]) < 0:
                    n = c
            for c in range(len(trees)):
                if c != l and c != n and formula_cross(trees[l], trees[c], trees[n]) == 0 and in_between(trees[l], trees[c], trees[n]):
                    fenced_trees.add(tuple(trees[c]))
            fenced_trees.add(tuple(trees[n]))
            l = n
        return list(list(i) for i in fenced_trees)
                    
                    
