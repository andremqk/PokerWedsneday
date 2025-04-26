from Deck import Deck, Card

class PokerHand:
    '''
    A class that represents a poker hand with 5 cards.
    '''
    def __init__(self, deck):
        '''
        Initialize (create and set up) a PokerHand object.
        :param deck: a Deck object to deal cards from
        '''

        cards = []
        for i in range(5):
            cards.append(deck.deal())
        self._cards = cards

    @property
    def cards(self):
        '''
        Getter (returns) for the list of cards in the hand.
        :return: list of 5 Card objects
        '''
        return self._cards

    def __str__(self):
        '''
        Represents the poker hand as a string
        :return: string listing the 5 cards
        '''
        return str(self.cards)

    @property
    def is_flush(self):
        '''
        Check if all cards have the same suit (check if its a flush).
        :return: True if hand is a flush, False otherwise
        '''
        for card in self.cards[1:]:
            if self.cards[0].suit != card.suit:
                return False
        return True

    @property
    def is_full_house(self):
        '''
        Check if hand is a full house (3 of a kind + a pair).
        :return: True if full house, False otherwise
        '''
        return self.number_matches == 8


    @property
    def number_matches(self):
        '''
        Calculate the total number of matching pairs between cards.
        :return: number of pairs
        '''
        matches = 0
        for i in range(len(self.cards)):
            for j in range(len(self.cards)):
                if i == j:
                    continue
                if self.cards[i].rank == self.cards[j].rank:
                    matches += 1
        return matches


    @property
    def is_pair(self):
        '''
        Check if hand has exactly one pair.
        :return: True if exactly one pair, False otherwise
        '''
        if self.number_matches == 2: #simple
            return True
        return False


    @property
    def is_two_pair(self):
        '''
        Check if hand has exactly two pairs.
        :return: True if two pairs, False otherwise
        '''
        return self.number_matches == 4 #more advanced

    @property
    def is_trips(self):
        '''
        Check if hand has three of a kind.
        :return: True if trips, False otherwise
        '''
        if self.number_matches == 6:
            return True
        return False

    @property
    def is_quads(self):
        '''
        Check if hand has four of a kind.
        :return: True if quads, False otherwise
        '''
        if self.number_matches == 12:
            return True
        return False

    @property
    def is_straight(self):
        '''
        Check if hand has 5 cards in sequence (straight).
        :return: True if straight, False otherwise
        '''
        self.cards.sort()
        distance = Card.RANKS.index(self.cards[4].rank) - \
                   Card.RANKS.index(self.cards[0].rank)
        return self.number_matches == 0 and distance == 4


count = 0
matches = 0
while matches < 10000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_pair:
        matches += 1
        #print(hand)
    count += 1

print(f"probability of a pair is {100*matches/count}%")

count = 0
matches = 0
while matches < 1000:
    deck = Deck()
    deck.shuffle()
    hand = PokerHand(deck)
    if hand.is_straight:
        matches += 1
        #print(hand)
    count += 1

print(f"probability of a straight is {100*matches/count}%")



#HOMEWORK FIRST 5 SESSIONS ADD DOCSTRING IN THE METHODS,CLASSES,