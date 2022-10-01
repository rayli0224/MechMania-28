from abc import abstractmethod
from game.game_state import GameState
from game.item import Item
import game.character_class

from game.position import Position
from random import Random

class Strategy(object):

    direction = 0
    spawn_point = 0

    
    def at_spawn(self, game_states: GameState, my_player_index: int) -> bool:
        if game_states.player_state_list[my_player_index].position.x == 0 and game_states.player_state_list[my_player_index].position.y == 0:
            spawn_point = 0
            return True
        elif game_states.player_state_list[my_player_index].position.x == 0 and game_states.player_state_list[my_player_index].position.y == 9:
            spawn_point = 1
            return True
        elif game_states.player_state_list[my_player_index].position.x == 9 and game_states.player_state_list[my_player_index].position.y == 0:
            spawn_point = 2
            return True
        elif game_states.player_state_list[my_player_index].position.x == 9 and game_states.player_state_list[my_player_index].position.y == 9:
            spawn_point = 3
            return True
        else:
            return False

    """Before the game starts, pick a class for your bot to start with.
    :returns: A game.CharacterClass Enum.
    """
    @abstractmethod
    def strategy_initialize(self, my_player_index: int) -> None:
        return game.character_class.CharacterClass.KNIGHT

    """Each turn, decide if you should use the item you're holding. Do not try to use the
    legendary Item.None!
    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.
    :returns: If you want to use your item
    """
    @abstractmethod
    def use_action_decision(self, game_states: GameState, my_player_index: int) -> bool:
        return self.at_spawn(game_states, my_player_index)
        # if game_states.player_state_list[my_player_index].position.x == 0 and game_states.player_state_list[my_player_index].position.y == 0:
        #     spawn_point = 0
        #     #return True
        # elif game_states.player_state_list[my_player_index].position.x == 0 and game_states.player_state_list[my_player_index].position.y == 9:
        #     spawn_point = 1
        #     #return True
        # elif game_states.player_state_list[my_player_index].position.x == 9 and game_states.player_state_list[my_player_index].position.y == 0:
        #     spawn_point = 2
        #     #return True
        # elif game_states.player_state_list[my_player_index].position.x == 9 and game_states.player_state_list[my_player_index].position.y == 9:
        #     spawn_point = 3
        #     #return True
        # #else:
        # return False

    
    """Each turn, pick a position on the board that you want to move towards. Be careful not to
    fall out of the board!
    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.
    :returns: A game.Position object.
    """
    @abstractmethod
    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        # if self.use_action_decision(game_state, my_player_index) and (game_state.player_state_list[my_player_index].item == Item.SPEED_POTION):
        #     if self.spawn_point == 0:
        #         destination = Position(game_state.player_state_list[my_player_index].position.x + 2, game_state.player_state_list[my_player_index].position.y + 2)
        #         return destination

        #     elif self.spawn_point == 1:
        #         destination = Position(game_state.player_state_list[my_player_index].position.x - 2, game_state.player_state_list[my_player_index].position.y + 2)
        #         return destination

        #     elif self.spawn_point == 2:
        #         destination = Position(game_state.player_state_list[my_player_index].position.x + 2, game_state.player_state_list[my_player_index].position.y - 2)
        #         return destination

        #     elif self.spawn_point == 3:
        #         destination = Position(game_state.player_state_list[my_player_index].position.x - 2, game_state.player_state_list[my_player_index].position.y - 2)
        #         return destination

        if self.spawn_point == 0:
                destination = Position(game_state.player_state_list[my_player_index].position.x + 1, game_state.player_state_list[my_player_index].position.y + 1)
                return destination

        elif self.spawn_point == 1:
            destination = Position(game_state.player_state_list[my_player_index].position.x - 1, game_state.player_state_list[my_player_index].position.y + 1)
            return destination

        elif self.spawn_point == 2:
            destination = Position(game_state.player_state_list[my_player_index].position.x + 1, game_state.player_state_list[my_player_index].position.y - 1)
            return destination

        elif self.spawn_point == 3:
            destination = Position(game_state.player_state_list[my_player_index].position.x - 1, game_state.player_state_list[my_player_index].position.y - 1)
            return destination

    """Each turn, pick a player you would like to attack. Feel free to be a pacifist and attack no
    one but yourself.
    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.
    :returns: Your target's player index.
    """
    @abstractmethod
    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        return Random().randint(0, 3)

    """Each turn, pick an item you want to buy. Return Item.None if you don't think you can
    afford anything.
    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.
    :returns: A game.Item object.
    """
    @abstractmethod
    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        return Item.NONE
        # if self.use_action_decision(game_state, my_player_index) and (game_state.player_state_list[my_player_index].item == Item.NONE.name) and (game_state.player_state_list[my_player_index].gold >= 5):
        #     return Item.SPEED_POTION
