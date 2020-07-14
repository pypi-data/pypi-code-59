"""
tests the rock paper scissors game
"""
import pytest
from games import rockPaperScissors


@pytest.mark.parametrize("user_choice, computer_choice, expected",
                         # Rock Tests
                         [("R", "rock", "we drew"),
                          ("R", "paper", "you lose"),
                          ("R", "scissors", "you win"),
                          # Paper Tests
                          ("P", "rock", "you win"),
                          ("P", "paper", "we drew"),
                          ("P", "scissors", "you lose"),
                          # Scissors Tests
                          ("S", "rock", "you lose"),
                          ("S", "paper", "you win"),
                          ("S", "scissors", "we drew")
                          ])
def test_check_who_won(user_choice, computer_choice, expected) -> None:
    actual_output = rockPaperScissors.check_who_won(user_choice, computer_choice)
    assert actual_output == expected
