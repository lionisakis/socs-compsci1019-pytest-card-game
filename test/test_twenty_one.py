import pytest

from card_game.card.game.TwentyOne.TwentyOne import *
from card_game.card.entity.Hand import *
from card_game.card.entity.Suit import *
from card_game.card.entity.FaceCard import *
from card_game.card.entity.Card import *

def test_stard_hand():
    assert score_hand(create_hand()) == 0

    for suit in suits:
        face = suit[0]+str("J")
        card = suit[0]+str(1)
        assert score_hand([face,face])==get_card_score(face)+get_card_score(face)
        assert score_hand([face,card])==get_card_score(face)+get_card_score(card)
        for number in range(1,10):
            card = suit[0]+str(number)
            assert score_hand([card,card])==get_card_score(card)+get_card_score(card)

    ace = suit[0]+str("A")
    nine = suit[0] + str("9")
    five = suit[0] + str("5")
    eight = suit[0] + str("8")
    assert score_hand([ace,card])==20
    assert score_hand([ace,card,five])==15
    assert score_hand([ace,card,five,eight])==0

ace = suits[0][0]+str("A")
ten = suits[0][0] + str("10")
two = suits[0][0] + str("2")
seven = suits[0][0] + str("7")
nine = suits[0][0] + str("9")
@pytest.mark.parametrize("hand,score",[('',0),([ace,ten],21),([ace,ten,ten,two],0),([ace,ace,nine],21),([seven,seven,seven],21)])
def test_score_hand_combinations(hand,score):
    assert score_hand(hand)==score

