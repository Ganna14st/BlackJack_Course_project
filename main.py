import itertools
import random
from tkinter import *
from PIL import Image, ImageTk

continue_game = True
# TODO restart

# make 52 cards deck
vals = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
suits = ['♣', '♦', '♥', '♠']
deck = list(itertools.product(vals, suits))
random.shuffle(deck)


class Gamer:
    def __init__(self):
        self.cards_set = random.choices(deck, k=2)
        for _ in self.cards_set:
            deck.remove(_)

    def sum_cards(self):
        row_score = [card[0] for card in self.cards_set]
        score = []
        for i in row_score:
            if i in ['J', 'Q', 'K']:
                i = 10
                score.append(i)
            elif i == 'A':
                i = 11
                score.append(i)
            else:
                score.append(i)
        return sum(score)

    def __str__(self):
        return "Your cards are {}, your score is {}".format(self.cards_set, self.sum_cards())


class Dealer(Gamer):
    def __str__(self):
        return f"Dealer's one card is {self.cards_set[0]}"


# make first route
def start_game():
    start_button.destroy()
    print(f"Your cards are {player.cards_set}, your score is {player.sum_cards()}")
    print(f"Dealer's cards are {dealer.cards_set}, dealer score is {dealer.sum_cards()}")
    if_blackjack()

    dealer_label.config(text='Dealer cards', background='#5D9C59')
    player_label.config(text='Your cards', background='#5D9C59')
    dealer_view.config(text=dealer, background='#5D9C59')
    player_view.config(text=player, background='#5D9C59')
    hit_button = Button(window, text='Hit', borderwidth=0, highlightthickness=0, command=take_more)
    stand_button = Button(window, text='Stand', borderwidth=0, highlightthickness=0, command=check_dealer)

    dealer_label.place(x=50, y=50)
    player_label.place(x=50, y=150)
    dealer_view.place(x=200, y=50)
    player_view.place(x=200, y=150)
    hit_button.place(x=150, y=280)
    stand_button.place(x=350, y=280)


def take_more():
    add = random.choice(deck)
    deck.remove(add)
    player.cards_set.append(add)
    player_score = player.sum_cards()
    player_view.config(text=player)
    print(f"you've got a {player.cards_set[-1]}. Your cards are {player.cards_set}, current score is {player_score}")
    if_blackjack()


def win_or_loose(result):
    global continue_game
    if result == 'win':
        text = 'GAME OVER\tYOU WON\t😎'
    else:
        text = 'GAME OVER\tYOU LOOSE\t😩'
    print(f"player cards is {player.cards_set}, dealer cards is {dealer.cards_set}")
    dealer_view.config(text='Dealers cards are {}, score is {}'.format(dealer.cards_set, dealer.sum_cards()))
    game_over.place(x=100, y=100)
    game_over.config(text=text, background='#C7E8CA')
    continue_game = False


def if_blackjack():
    global continue_game
    dealer_score = dealer.sum_cards()
    player_score = player.sum_cards()
    if player_score > 21 or dealer_score == 21:
        win_or_loose(result='loose')
    elif player_score == 21:
        win_or_loose(result='win')
    else:
        continue_game = True
    return continue_game


def compare(score1, score2):
    global continue_game
    if 21 - score1 == 21 - score2:
        print(f"Your score is {score1}, dealer score is {score2} Its a draw")
        continue_game = False
    elif 21 - score1 < 21 - score2:
        win_or_loose(result='win')
    else:
        pass


def check_dealer():
    if dealer.sum_cards() < 16:
        add = random.choice(deck)
        deck.remove(add)
        dealer.cards_set.append(add)
        dealer_score = dealer.sum_cards()
        print(dealer.cards_set)
        print(dealer_score)
        if_blackjack()
        if continue_game:
            compare(player.sum_cards(), dealer.sum_cards())


# setting up GUI
window = Tk()
window.title("BlackJack")
window.geometry('617x360')
img = Image.open("images/bj-bg.jpg")
bg = ImageTk.PhotoImage(img)
window_label = Label(window, image=bg)
window_label.place(x=0, y=0, relwidth=1, relheight=1)
start_button = Button(window, text='Start Game', relief="flat", borderwidth=0, highlightthickness=0, command=start_game)
start_button.pack(pady=20)
dealer_label = Label(window)
player_label = Label(window)
dealer_view = Label(window, wraplength=350, anchor='w')
player_view = Label(window, wraplength=350, anchor='w')
game_over = Label(window)

player = Gamer()
dealer = Dealer()


window.mainloop()
