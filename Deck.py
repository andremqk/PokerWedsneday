import random


class Card:
    '''
    A class that represents a playing card with a suit and a rank.
    '''
    RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    SUITS = ["Clubs", "Spades", "Hearts", "Diamonds"]
    def __init__(self, suit, rank):
        '''
         Initialize (create and set up) a Card object.
        :param suit: the suit of the card (must be in SUITS listt)
        :param rank: the rank of the card (must be in RANKS list)
        '''
        if rank not in self.RANKS:
            raise ValueError("Invalid Rank")
        if suit not in self.SUITS:
            raise ValueError("Invalid Suit")
        self._suit = suit
        self._rank = rank

    def __eq__(self,other):
        '''
        Check if two cards have the same rank.
        :param other: another Card object
        :return: True if ranks are the same, False otherwise
        '''
        return self.rank == other.rank

    def __gt__(self, other):
        '''
        Compare two cards by their ranks.
        :param other: another Card object
        :return: True if this card is greater than self, False otherwise
        '''
        return self.RANKS.index(self.rank) > self.RANKS.index(other.rank)

    def __str__(self):
        '''
        Represents the Card as a String
        :return: rank and suit as a string
        '''
        return f"{self._rank} of {self._suit}"

    def __repr__(self):
        '''
        Official string representation of the self card.
        :return: same as __str__
        '''
        return self.__str__()

    @property
    def suit(self):
        '''
        Getter (returns) for suit.
        :return: the suit of the card
        '''
        return self._suit

    @property
    def rank(self):
        '''
        Getter (returns) for rank.
        :return: the rank of the card
        '''
        return self._rank

class Deck:
    '''
    A class that represents a deck of 52 playing cards.
    '''
    def __init__(self):
        '''
        Initialize (create and set up) a full deck of 52 cards.
        '''
        self._deck = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._deck.append(Card(suit,rank))

    def __str__(self):
        '''
        Represents the deck as a string
        :return: string of all cards in the deck
        '''
        return str(self._deck)

    def shuffle(self):
        '''
        Shuffle the deck randomly using random.
        :return: the deck
        '''
        random.shuffle(self._deck)

    def deal(self):
        '''
        Deal (remove and return) the top card of the deck.
        :return: a Card object
        '''
        return self._deck.pop(0)

if __name__ == "__main__":
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
    print(deck.deal())
