import random


truth_guestions = [
    "какой самый неловкий момент в вашей жизни?",
    "кого из своих друзей вы считаете самым странным?",
    "какое ваше самое большое секретное желание?",
    "что вы сделали бы, если бы знали, что вас никто не осудит?",
    "кто ваш самый большой кумир и почему?"
]
dare_tasks = [
    "сделайте 10 отжиманий",
    "станцуйте 30 секунд под любую песню",
    "позвоните другу и скажите ему, что вы его любите",
    "сделайте селфи с самой смешной гримасой",
    "покажите всем свою лучшую танцевальную паузу"
]


def get_random_item(item_list):
    return random.choice(item_list)


def main():
    print("добро пожаловать в игру 'правда или действие'")


while True:
    choce = input("выберите 'правда' или 'действие' (или 'выход' для завершения): ").strip().lower()

    if choce == 'правда':
        guestion = get_random_item(truth_guestions)
        print(f"ваш вопрос: {truth_guestions}")
    elif choce == 'действие':
        task = get_random_item(dare_tasks)
        print(f"ваше задание: {task}")

    elif choce == 'выход':
        print("спасибо за игру! До свидания")
        break

    else:
        print("пожалуйста, введите 'правда', 'действие' или 'выход'")
if __name__ == "__main__":
    main()
