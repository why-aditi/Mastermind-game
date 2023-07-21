import random


def number():
    mini = 10000
    maxi = 100000
    num = random.randint(mini, maxi)
    return num


def play():
    num = number()
    n = int(input("Guess the number: "))
    tries = 0
    if n == num:
        print("You guessed correctly in first attempt")
    else:
        while n != num:
            tries += 1
            count = 0
            n = str(n)
            num = str(num)
            length = len(num)
            correct = ['X']*length
            for i in range(0, length):
                if n[i] == num[i]:
                    count += 1
                    correct[i] = n[i]
            if count == 0:
                print("None of the numbers in your input match.")
            if count == length:
                print("You've guesses correctly in ", tries, " tries")
                break
            if count != 0 and count != length:
                print("Not quite the number. But you did get ", count, " digit(s) correct!")
                print(correct)
            if tries >= 10:
                print("You lost")
                print("The number was ", num)
                break
            n = int(input("Guess the number: "))


if __name__ == '__main__':
    print(play())
