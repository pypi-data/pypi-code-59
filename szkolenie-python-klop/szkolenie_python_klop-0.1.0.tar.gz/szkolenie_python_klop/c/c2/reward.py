def get_reward(times):
    if times <= 10:
        print("Gratulacje, wygrałeś samochód!")
    elif 10 < times <= 25:
        print("Gratulacje, wygrałeś wycieczke!")
    elif 25 < times <= 50:
        print("Gratulacje, wygrałeś nagrode pocieszenia!")
    else:
        print("Niestety, moze nastepnym razem Ci sie poszczesci...")