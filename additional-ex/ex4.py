# Exercise 4: Coin game
#     Alice and Bob are playing a game using a bunch of coins. The players pick several coins out
#     of the bunch in turn. Each player can pick either 1, 2 or 4 coins in each turn. Each time a player
#     is allowed to pick coins, the player that gets the last coin is the winner. Assume that both players
#     are very smart, and he/she will try his/her best to work out a strategy to win the game. It is
#     known that at last, when 1, 2 or 4 coins are left, the player with first turn will definitely pick 1,
#     2 or 4 coins as required and win. For example, if there are 2 coins in end and Alice is the first
#     player to pick, she will definitely pick 2 coins and win. If there are 3 coins and Alice is still the
#     first player to pick, no matter she picks 1 or 2 coins, Bob will get the last coin and win the
#     game. Given the number of coins and the order of players (which means the first and the second
#     players to pick the coins), you are required to write a program to calculate the winner of the
#     game, and calculate how many different strategies there are for he/she to win the game.

def coin_game_winner(num_coins:int, first_player:str, second_player:str) -> tuple[str, int]:
    OPTIONS = (1, 2, 4)
    memo = {}

    def can_win(total:int) -> bool:
        if total in memo:
            return memo[total]
        if total in (1, 2, 4):
            memo[total] = True
            return True
        if total == 3:
            memo[total] = False
            return False

        for o in OPTIONS:
            if total - o >= 0 and not can_win(total - o):
                memo[total] = True
                return True
            
        memo[total] = False
        return False

    first_can_win = can_win(num_coins)
    winner = first_player if first_can_win else second_player

    def count_strategies(total:int, current_turn:bool = True) -> int:
        if total == 0:
            return 1
        if current_turn != first_can_win:
            return 0
        
        count = 0

        for o in OPTIONS:
            if total - o >= 0 and not can_win(total - o):
                count += 1

        return count

    strategies = count_strategies(num_coins) if first_can_win else 0
    return winner, strategies