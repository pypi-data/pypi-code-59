def try_again():
    vote = input("\nChcesz sprobowac jeszcze raz? (T/t/Y/y - Tak; N/n - Nie): ")
    votes_map = {
        "T": True,
        "t": True,
        "Y": True,
        "y": True,
        "N": False,
        "n": False
    }

    return votes_map[vote]
