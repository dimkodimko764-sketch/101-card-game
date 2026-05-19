import random
import tkinter as tk

class Interface:
    def __init__(self):
        self.last_move = ""
        self.game = None

        self.window = tk.Tk()
        self.window.title("Game 101")
        self.window.geometry("600x500")

        self.label = tk.Label(self.window, text="Game 101")
        self.label.pack()

        self.text_area = tk.Text(self.window)
        self.text_area.pack()

        self.start_button = tk.Button(self.window, text= "Start game", command=self.start_game)
        self.start_button.pack()

        self.turn_button = tk.Button(self.window, text= "Make a move", command=self.make_turn)
        self.turn_button.pack()

        self.result_button = tk.Button(self.window, text= "Show result", command = self.show_result)
        self.result_button.pack()

        self.window.mainloop()

    def start_game(self):
        self.game = Game()
        self.game.deal_cards()
        self.show_state()

    def make_turn(self):
        self.last_move = self.game.play_turn(self.game.players[0])
        self.show_state()

    def show_result(self):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, self.game.get_winner_info())

    def show_state(self):
        self.text_area.delete("1.0", tk.END)

        self.text_area.insert(tk.END, "Game started!\n\n")
        self.text_area.insert(tk.END, f"Card on table: {self.game.table_card}\n\n")

        for player in self.game.players:
            self.text_area.insert(tk.END, f"{player.name}:\n")

            for card in player.hand:
                self.text_area.insert(tk.END, f"{card}\n")

            self.text_area.insert(tk.END, f"Card on table: {self.game.table_card}\n\n")

            if self.last_move != "":
                self.text_area.insert(tk.END, f"{self.last_move}\n\n")
        pass
        
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.points = self.get_points()

    def get_points(self):
        if self.value == "A":
            return 11
        elif self.value == "10":
            return 10
        elif self.value == "9":
            return 0
        elif self.value == "8":
            return 8
        elif self.value == "7":
            return 7
        elif self.value == "6":
            return 6
        elif self.value == "K":
            return 4
        elif self.value == "Q":
            return 3
        elif self.value == "J":
            return 2
        else:
            return 0

    def __str__(self):
        return f"{self.value} {self.suit}"
    
class Deck:
    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        suits = ["♠️", "♥️", "♦️", "♣️"]
        values = ["6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        for suit in suits:
            for value in values:
                self.cards.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_card(self, card):
        self.hand.append(card)

    def show_hand(self,):
        for card in self.hand:
         print(card)

    def play_card(self):
        return self.hand.pop()
    
    def count_point(self):
        total = 0
        for card in self.hand:
            total += card.points
        return total
    
player = Player("Users")
player.take_card (Card("♠️", "A"))
player.take_card (Card("♥️", "8"))

player.show_hand()
print (player.play_card())

class Game:
    def __init__(self):
     self.deck = Deck()
     self.players = [ Player ("Player 1"),
     Player ("Player 2"),
     Player ("Player 3"),
     Player ("Player 4"),
    ]
     self.table_card = None
     self.current_player = 0

    def deal_cards(self):
        for player in self.players:
         for i in range(5):
             player.take_card(self.deck.draw_card())

        self.table_card = self.deck.draw_card()
    
    def show_game_state(self):
        print ("Card is table", self.table_card)
       
        for player in self.players:
            print (f"\n{player.name}")
            player.show_hand()
    
    def start_game(self):
        self.deal_cards()
        self.show_game_state()
        self.play_turn(self.players[0])
        print ("\nAfter turn:")
        self.show_game_state()
        self.show_winner()

    def play_turn(self, player):
        card = player.play_card()
        self.table_card = card
        return f"{player.name} played: {card}"

    def can_play(self, card, table_card):
        return (card.suit == table_card.suit or card.value == table_card.value)
    
    def show_winner(self):
        winner = min(self.players, key=lambda player: player.count_point())
        print("Winner:", winner.name)

    def get_winner_info(self):
        winner = min(self.players, key=lambda player: player.count_point())
        text = "Points:\n"

        for player in self.players:
            text += f"{player.name}: {player.count_point()} points\n"

        text += f"\nWinner: {winner.name}"
        return text 

app = Interface()
