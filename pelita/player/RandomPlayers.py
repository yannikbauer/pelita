
def random_player(bot, state):
    """ A player that makes moves at random. """
    return bot.random.choice(bot.legal_positions), state


def nq_random_player(bot, state):
    """ Not-Quite-RandomPlayer that will move randomly but not stop or reverse. """

    legal_positions = bot.legal_positions[:]
    # Remove stop
    try:
        legal_positions.remove(bot.position)
    except ValueError:
        pass
    # now remove the move that would lead to the previous_position
    # unless there is no where else to go.
    if len(legal_positions) > 1:
        if len(bot.track) >= 2:
            try:
                legal_positions.remove(bot.track[-2])
            except ValueError:
                # if we did not move in the last round,
                # there will be nothing left to delete
                pass
    # just in case, there is really no way to go to:
    if not legal_positions:
        return datamodel.stop
    # and select a move at random
    return bot.random.choice(legal_positions), state


TEAM_NAME = "The Random Players"
def move(bot, state):
    if bot.turn == 0:
        return random_player(bot, state)
    else:
        return nq_random_player(bot, state)
