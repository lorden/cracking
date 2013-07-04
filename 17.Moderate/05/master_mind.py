def check_guess(guess, solution):
    hits = []
    for i in xrange(0, 4):
        if guess[i] == solution[i]:
            hits.append(guess[i])
            solution[i] = None

    pseudo_hits = []
    for i in xrange(0, 4):
        if guess[i] in solution:
            pseudo_hits.append(guess[i])
            solution[solution.index(guess[i])] = None

    return len(hits), len(pseudo_hits)


guess = ['G', 'G', 'R', 'R']
solution = ['R', 'G', 'B', 'Y']

hits, pseudo_hits = check_guess(guess, solution)
print "Hits: %s" % hits
print "Pseudo hits: %s" % pseudo_hits
