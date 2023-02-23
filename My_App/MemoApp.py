import unittest


class Memo_App:
    def __init__(self):
        self.birth_day_dic = {
            "birthday": [],
            "friend_name": []
        }

    def add_friend_birthday(self, friend_name, birthday):

        birthdays = self.birth_day_dic["birthday"]
        birthdays.append(birthday)
        self.birth_day_dic["birthday"] = birthdays
        friends_name = self.birth_day_dic["friend_name"]
        friends_name.append(friend_name)
        self.birth_day_dic["friend_name"] = friends_name