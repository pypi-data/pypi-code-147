from __future__ import annotations

from typing import List, Dict, Union, Set
from pied_poker.deck.deck import Deck
from pied_poker.card.card import Card
from pied_poker.card.rank import Rank
from pied_poker.card.suit import Suit

# Only 6 thru A can be the highest card on a straight
STRAIGHT_POSSIBLE_HIGH_CARDS = [Rank(str(i)) for i in ['5', '6', '7', '8', '9', '10', 'j', 'q', 'k', 'a']]


def getAllHandsRanked():
    from pied_poker.hand.flush import Flush
    from pied_poker.hand.four_of_a_kind import FourOfAKind
    from pied_poker.hand.full_house import FullHouse
    from pied_poker.hand.high_card import HighCard
    from pied_poker.hand.one_pair import OnePair
    from pied_poker.hand.royal_flush import RoyalFlush
    from pied_poker.hand.straight import Straight
    from pied_poker.hand.straight_flush import StraightFlush
    from pied_poker.hand.three_of_a_kind import ThreeOfAKind
    from pied_poker.hand.two_pair import TwoPair

    return [
        RoyalFlush,
        StraightFlush,
        FourOfAKind,
        FullHouse,
        Flush,
        Straight,
        ThreeOfAKind,
        TwoPair,
        OnePair,
        HighCard
    ]


class StaticProperty(staticmethod):
    def __get__(self, *_):
        return self.__func__(self)


class BaseHand:
    hand_rank: int = -1

    def __init__(self, cards: List[Card]):
        """
        For each type of hand, when initialized, it is assumed all parent hands are not present
        :param cards:
        :type cards:
        """
        self.cards_sorted: List[Card] = sorted(cards, reverse=True) # For comparing high cards
        self.cards_set = set()

        self.ranks_single: List[Rank] = []  # All ranks of single cards, sorted
        self.ranks_pair: List[Rank] = []  # All ranks of pair cards, sorted
        self.ranks_triple: List[Rank] = []  # All ranks of triple cards, sorted
        self.ranks_quad: List[Rank] = []  # All ranks of quad cards, sorted

        self.suit_counts: Dict[Suit, int] = {}
        self.rank_counts: Dict[Rank, int] = {}

        self.flush_suit: Suit = None

        self.top_straight: List[Card] = None
        self.straight_flush: List[Card] = None
        self.all_confirmed_straights: List[List[Card]] = []
        self.possible_straights: List[List[Card]] = []

        for c in self.cards_sorted:
            self.__straight_counter__(self.possible_straights, c)
            self.__suit_counter__(c)
            self.__rank_counter__(c)
            self.cards_set.add(c)

        # Check for case of ace-low straight, which is missed by above logic
        if self.possible_straights:
            if self.possible_straights[-1]:
                if self.possible_straights[-1][-1].rank == Rank('2'):
                    i = 0
                    while self.cards_sorted[i].rank == Rank('a'):  # Add all possible ace straights
                        self.__straight_counter__(self.possible_straights, self.cards_sorted[i])
                        i += 1

        self.top_straight: List[Card] = self.all_confirmed_straights[0] if self.all_confirmed_straights else None

    @StaticProperty
    def ALL_HANDS_RANKED(self):
        return getAllHandsRanked()

    @property
    def is_hand(self):
        return True

    @property
    def cards_in_hand(self):
        return []

    @property
    def cards_not_in_hand(self):
        return self.cards_sorted[:5]

    def as_hand(self, target_class):
        self.__class__ = target_class
        return self

    def as_best_hand(self):
        for hand_class in self.ALL_HANDS_RANKED:
            # outsGetter = self.outs
            new: hand_class = self.as_hand(hand_class)
            if new.is_hand:  # This will always be true for HighCard, so this will always be reached
                return new

    def __suit_counter__(self, c: Card):
        self.suit_counts[c.suit] = self.suit_counts.get(c.suit, 0) + 1
        if self.suit_counts[c.suit] >= 5:
            self.flush_suit = c.suit

    def __rank_counter__(self, c: Card):
        self.rank_counts[c.rank] = self.rank_counts.get(c.rank, 0) + 1

        if self.rank_counts[c.rank] == 1:
            self.ranks_single.append(c.rank)

        if self.rank_counts[c.rank] == 2:
            self.ranks_single.remove(c.rank)
            self.ranks_pair.append(c.rank)

        if self.rank_counts[c.rank] == 3:
            self.ranks_pair.remove(c.rank)
            self.ranks_triple.append(c.rank)

        if self.rank_counts[c.rank] == 4:
            self.ranks_triple.remove(c.rank)
            self.ranks_quad.append(c.rank)

    def __straight_counter__(self, possible_straights: List[List[Card]], c: Card):
        new_straights = []

        for s in possible_straights:
            # If length < 5, we can check for a straight
            # If length == 5, we can only replace the last card_internals on the straight
            lowest_card_in_straight = s[-1]

            if len(s) <= 5:
                if lowest_card_in_straight.rank - c.rank == 1 and len(s) < 5:
                    # Next card_internals for straight is here
                    s.append(c)
                    if len(s) == 5:
                        self.all_confirmed_straights.append(s)
                        self.__straight_flush_counter__(s)
                elif lowest_card_in_straight.rank == c.rank:
                    # Next card is equal to current lowest card in straight
                    # Therefore, we duplicate this list again, but replace the
                    # last element with the current card (in case a straight flush shows up)
                    new_possible_straight = s.copy()[:len(s) - 1] + [c]
                    new_straights.append(new_possible_straight)
                    if len(new_possible_straight) == 5:
                        self.all_confirmed_straights.append(new_possible_straight)
                        self.__straight_flush_counter__(s)

        possible_straights.extend(new_straights)

        if c.rank in STRAIGHT_POSSIBLE_HIGH_CARDS and [c] not in new_straights:
            possible_straights.append([c])

    def __straight_flush_counter__(self, s: List[Card]):
        if not self.straight_flush:
            suits = set([c.suit for c in s])
            if len(suits) == 1:  # This straight is also a flush
                self.straight_flush = s

    def __eq__(self, other):
        return self.hand_rank == other.hand_rank

    def __gt__(self, other):
        return self.hand_rank > other.hand_rank

    def __lt__(self, other):
        return self.hand_rank < other.hand_rank

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f'{self.__class__.__name__}({self.cards_in_hand}, {self.cards_not_in_hand})'

    def __hash__(self):
        return str(self).__hash__()

    def __hand_outs__(self, known_cards: Set[Card]) -> List[Card]:
        """
        The outs, if any, that would make the hand. For example, if the player has a 4 flush, the remaining available
        suited cards would be returned here to complete the flush
        :return:
        :rtype: List[Card]
        """
        return []

    def outs(self, known_cards: Set[Card] = frozenset()) -> Dict[Union[BaseHand.__class__], List[Card]]:
        """
        All of the possible one-carded outs that the player could have that are better than their current hand.
        :return:
        :rtype:
        """
        if isinstance(known_cards, frozenset):
            known_cards = set()

        original_class = self.__class__
        rv: Dict[Union[BaseHand.__class__], List[Card]] = {}
        known_cards_and_outs: Set[Card] = {*known_cards}

        for hand_class in self.ALL_HANDS_RANKED:
            if hand_class.hand_rank > original_class.hand_rank:
                outs = self.as_hand(hand_class).__hand_outs__(known_cards_and_outs)
                if len(outs) > 0:
                    rv[hand_class] = outs

        self.as_hand(original_class)
        return rv

