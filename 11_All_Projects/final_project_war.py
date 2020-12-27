"""
Implement the card game war. Rules are:

1. Deal out deck of 52 cards between two users.
2. Each player plays a card. Higher card wins (Highest card value is Ace). Winner takes both cards.
3. If players tie, then each player puts down next two cards, and the third
   card competes.
   If a player has less than 3 cards, then they put down all of their cards
   and their final card competes against the other player's third card.
   Continue doing this until tie is broken.
   Winner takes all cards.
4. Game is over when a player doesn't have any cards left.
"""


from random import shuffle


class Deck:
    def __init__(self):
        self.cards = ["2", "3", "4", "5", "6", "7",
                      "8", "9", "10", "J", "Q", "K", "A"] * 4

    def shuffle_deck(self):
        shuffle(self.cards)
        return self.cards


class Player:
    def __init__(self, player_name, primary_deck=[]):

        self.primary_deck = primary_deck
        self.secondary_deck = []
        self.table = []
        self.overall_cards_counter = self.summary_card_counter()
        self.primary_deck_counter = self.primary_card_counter()
        self.secondary_deck_counter = self.secondary_card_counter()
        self.player_name = player_name

    def summary_card_counter(self):
        return self.primary_card_counter() + self.secondary_card_counter()

    def primary_card_counter(self):
        self.primary_deck_counter = 0
        for _card in self.primary_deck:
            self.primary_deck_counter += 1
        return self.primary_deck_counter

    def secondary_card_counter(self):
        self.secondary_deck_counter = 0
        for _card in self.secondary_deck:
            self.secondary_deck_counter += 1
        return self.secondary_deck_counter

    def draw_card(self):
        drawn_card = self.primary_deck.pop()
        self.table.append(drawn_card)
        self.primary_deck_counter = self.primary_card_counter()
        self.secondary_deck_counter = self.secondary_card_counter()
        self.overall_cards_counter = self.summary_card_counter()
        return self.primary_deck

    def get_card_value(self):
        card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
                      "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

        for key, value in card_value.items():
            if key == self.table[-1]:
                return value

    def new_hand(self):
        if self.primary_deck == []:
            self.primary_deck = self.secondary_deck
            shuffle(self.primary_deck)
        self.secondary_deck = []
        return self.primary_deck

    def __str__(self):
        primary_deck_str = ", ".join(self.primary_deck)
        secondary_deck_str = ", ".join(self.secondary_deck)
        final_status = f"Overall cards: {self.overall_cards_counter}\nmain deck card number: {self.primary_deck_counter}\n{primary_deck_str}\nside deck card number: {self.secondary_deck_counter}\n{secondary_deck_str}\n"
        return final_status


class Game(Deck, Player):
    def __init__(self):
        self.card_deck = Deck()
        self.create_deck = self.card_deck.shuffle_deck()
        self.a_deck = self.create_deck[:26]
        self.b_deck = self.create_deck[26:]
        self.player1 = Player(player1_name, self.a_deck)
        self.player2 = Player(player2_name, self.b_deck)

    def win(self):
        return self.player1.summary_card_counter() == 52 or self.player2.summary_card_counter() == 52

    def game_rule(self):

        if self.player1.get_card_value() > self.player2.get_card_value():
            take_card = self.player2.table.pop()
            self.player1.secondary_deck.append(take_card)
            self.player1.secondary_deck += self.player1.table + self.player2.table
            self.player1.table = []
            self.player1.primary_deck_counter = self.player1.primary_card_counter()
            self.player1.secondary_deck_counter = self.player1.secondary_card_counter()
            self.player1.overall_cards_counter = self.player1.summary_card_counter()
            print(f"{player1_name} wins the round\n")
            return self.player1.secondary_deck
        else:
            take_card = self.player1.table.pop()
            self.player2.secondary_deck.append(take_card)
            self.player2.secondary_deck += self.player1.table + self.player2.table
            self.player2.table = []
            self.player2.primary_deck_counter = self.player2.primary_card_counter()
            self.player2.secondary_deck_counter = self.player2.secondary_card_counter()
            self.player2.overall_cards_counter = self.player2.summary_card_counter()
            print(f"{player2_name} wins the round\n")
            return self.player2.secondary_deck


def main():
    try:
        while game.player1.overall_cards_counter != 52 or game.player1.overall_cards_counter != 52:
            game.player1.draw_card()
            game.player2.draw_card()
            game.game_rule()
            if game.player1.primary_deck == []:
                game.player1.primary_deck = game.player1.secondary_deck
                shuffle(game.player1.primary_deck)
                game.player1.secondary_deck = []
            if game.player2.primary_deck == []:
                game.player2.primary_deck = game.player2.secondary_deck
                shuffle(game.player2.primary_deck)
                game.player2.secondary_deck = []
            print(game.player1)
            print(game.player2)
    except:
        pass

    if game.player1.overall_cards_counter == 52:
        print(f"CONGRATULATIONS! {player1_name} won the game!")
    else:
        print(f"CONGRATULATIONS! {player2_name} won the game!")


player1_name = str(input("Player 1, please enter your name:\n"))
player2_name = str(input("Player 2, please enter your name:\n"))
game = Game()
main()
