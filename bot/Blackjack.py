import random


class Blackjack:
    def __init__(self, user_id, play_time, session_id, finished, cards, hand) -> None:
        self.user_id = user_id
        self.play_time = play_time
        self.session_id = session_id
        self.finished = finished
        self.cards = cards
        self.hand = hand

    def draw(self):
        self.hand.append(random.choice(self.cards))

    def calculate_hand_value(self):
        total_value = 0
        num_aces = 0

        for card in self.hand:
            if card in ["J", "Q", "K"]:
                total_value += 10
            elif card == "A":
                num_aces += 1
            else:
                total_value += card

        # Handle Aces
        for _ in range(num_aces):
            if total_value + 11 <= 21:
                total_value += 11
            else:
                total_value += 1

        return total_value

    def hit_or_stand(self):
        while True:
            choice = input("Do you want to hit or stand? (h/s): ").lower()
            if choice in ["h", "s"]:
                return choice
            else:
                print("Invalid choice. Please enter 'h' to hit or 's' to stand.")


while True:
    print("Total value of your hand:", player.calculate_hand_value())
    if player.calculate_hand_value() > 21:
        print("Busted! You lose.")
        break
    elif player.calculate_hand_value() == 21:
        print("Blackjack! You win!")
        break
    else:
        choice = player.hit_or_stand()
        if choice == "h":
            player.draw()
            print("Your hand:", player.hand)
        else:
            print("You stand with the hand:", player.hand)
            break
