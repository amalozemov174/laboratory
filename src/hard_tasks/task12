def MassVote(N,Votes):
    winner_id = 0
    winner_amount = 0
    winner_percent = 0
    summ_votes = 0
    check_equals = {}
    for i in range(N):
        if check_equals.get(Votes[i]) == None:
            check_equals[Votes[i]] = 1
        elif check_equals.get(Votes[i]) >= 1:
            check_equals[Votes[i]] = check_equals.get(Votes[i]) + 1
    for i in range(N):
        if i == 0:
            winner_id = i + 1
            winner_amount = Votes[i]
        if Votes[i] > winner_amount:
            winner_id = i + 1
            winner_amount = Votes[i]
    for i in range(N):
        summ_votes += Votes[i]
    winner_percent = (winner_amount / summ_votes) * 100        
    if winner_percent > 50:
        return f"majority winner {winner_id}"
    elif check_equals.get(winner_amount) > 1:
        return 'no winner'
    else:
        return f"minority winner {winner_id}"
