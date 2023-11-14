import math
def evaluate(game_state):
    return game_state.count('X') - game_state.count('O')
def alpha_beta_pruning(game_state, depth, alpha, beta, is_max_player):
    if depth == 0 or game_over(game_state):
        return evaluate(game_state)
    if is_max_player:
        max_eval = -math.inf
        for move in get_possible_moves(game_state):
            new_state = make_move(game_state, move, 'X')
            eval_score = alpha_beta_pruning(new_state, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval_score)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for move in get_possible_moves(game_state):
            new_state = make_move(game_state, move, 'O')
            eval_score = alpha_beta_pruning(new_state, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval_score)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval
def game_over(game_state):
    return not (' ' in game_state)
def get_possible_moves(game_state):
    return [i for i in range(len(game_state)) if game_state[i] == ' ']
def make_move(game_state, move, player):
    new_state = list(game_state)
    new_state[move] = player
    return ''.join(new_state)
def alpha_beta_search(game_state, depth):
    alpha = -math.inf
    beta = math.inf
    best_score = -math.inf
    best_move = None
    for move in get_possible_moves(game_state):
        new_state = make_move(game_state, move, 'X')
        score = alpha_beta_pruning(new_state, depth - 1, alpha, beta, False)
        if score > best_score:
            best_score = score
            best_move = move
        alpha = max(alpha, score)
    return best_move
if __name__ == "__main__":
    initial_game_state = " " * 9  
    depth = 4  
    best_move = alpha_beta_search(initial_game_state, depth)
    print("Best move:", best_move)
