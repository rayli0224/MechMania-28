from abc import abstractmethod
from game.game_state import GameState
from game.item import Item
import game.character_class

from game.position import Position

class Strategy(object):

    step = 0
    spawn_point = 0

    @abstractmethod
    def at_spawn(self, game_states: GameState, my_player_index: int) -> bool:
        if GameState.player_state_list[my_player_index].position.x == 0 and GameState.player_state_list[my_player_index].position.y == 0:
            spawn_point = 0
            return True
        elif GameState.player_state_list[my_player_index].position.x == 0 and GameState.player_state_list[my_player_index].position.y == 9:
            spawn_point = 1
            return True
        elif GameState.player_state_list[my_player_index].position.x == 9 and GameState.player_state_list[my_player_index].position.y == 0:
            spawn_point = 2
            return True
        elif GameState.player_state_list[my_player_index].position.x == 9 and GameState.player_state_list[my_player_index].position.y == 9:
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
    def use_action_decision(self, game_state: GameState, my_player_index: int) -> bool:
        return self.at_spawn(self, GameState, my_player_index)


    """Each turn, pick a position on the board that you want to move towards. Be careful not to
    fall out of the board!

    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.

    :returns: A game.Position object.
    """
    @abstractmethod
    def move_action_decision(self, game_state: GameState, my_player_index: int) -> Position:
        if self.at_spawn(self, GameState, my_player_index):
            step = 1
            if self.spawn_point == 0:
                return # move down and right
            elif self.spawn_point == 1:
                return # move down and left
            elif self.spawn_point == 2:
                return # move up and right
            elif self.spawn_point == 3:
                return # move up and left

        if self.spawn_point == 0:
            if step == 0:
                step == 1
                return GameState.player_state_list[my_player_index].position.y + 1
            elif step == 1:
                step == 0
                return GameState.player_state_list[my_player_index].position.x + 1
        elif self.spawn_point == 1:
            if step == 0:
                step == 1
                return GameState.player_state_list[my_player_index].position.y + 1
            elif step == 1:
                step == 0
                return GameState.player_state_list[my_player_index].position.x - 1
        elif self.spawn_point == 2:
            if step == 0:
                step == 1
                return GameState.player_state_list[my_player_index].position.y - 1
            elif step == 1:
                step == 0
                return GameState.player_state_list[my_player_index].position.x + 1
        elif self.spawn_point == 3:
            if step == 0:
                step == 1
                return GameState.player_state_list[my_player_index].position.y - 1
            elif step == 1:
                step == 0
                return GameState.player_state_list[my_player_index].position.x - 1

    """Each turn, pick a player you would like to attack. Feel free to be a pacifist and attack no
    one but yourself.

    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.

    :returns: Your target's player index.
    """
    @abstractmethod
    def attack_action_decision(self, game_state: GameState, my_player_index: int) -> int:
        pass

    """Each turn, pick an item you want to buy. Return Item.None if you don't think you can
    afford anything.

    :param gameState:     A provided GameState object, contains every piece of info on the game board.
    :param myPlayerIndex: You may find out which player on the board you are.

    :returns: A game.Item object.
    """
    @abstractmethod
    def buy_action_decision(self, game_state: GameState, my_player_index: int) -> Item:
        if self.at_spawn(self, GameState, my_player_index) and (game_state.player_state_list[my_player_index].item == Item.NONE) and (game_state.player_state_list[my_player_index].gold >= 5):
            return Item.SPEED_POTION
        


