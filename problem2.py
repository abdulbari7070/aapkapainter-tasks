# Write a code that prints out individual scores of two players in a game of cricket where score is given as runs per ball in an array. In a game of cricket a person changes strike if he scores an odd number, and keeps strike with him if he scores an even number. No need to consider changing strike after every 6 balls or an over.
#     Sample Input1: [1,2]
#     Output1: p1: 1, p2: 2
#     Sample Input2: [1,2,3,2,1]
#     Output2: p1: 4, p2: 5


# Solution
# strike is a boolean variable which solves this problem.
# Initially strike is set to True which means p1 is on the batting side or having strike
# If p1 scores odd runs then strike rotates that means strikes changes to False.
# If strike is False then that means p2 is on the batting side. If he scores even runs then 
# Strike is False and If he scores odd runs then strike changes again.


def calculate_player_scores(input):
    p1 = 0
    p2 = 0
    strike = True
    for runs in input:
        if strike:
            if runs%2==0:
                p1+=runs
                strike=True
            else:
                p1+=runs
                strike=False
        else:
            if runs%2==0:
                p2+=runs
                strike = False
            else:
                p2+=runs
                strike=True
    return p1, p2

input = [1,2,2,2,4,5,1]
p1, p2 = calculate_player_scores(input)
print("Player 1 : ", p1)
print("Player 2 : ", p2)