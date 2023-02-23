import datetime
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

    def delete_friend_birthday(self, friend_name, birthday):
        birthdays = self.birth_day_dic["birthday"]
        friends_name = self.birth_day_dic["friend_name"]
        counter = 0

        for i in birthdays:
            if i == birthday and friends_name[counter] == friend_name:
                birthdays.pop(counter)
                friends_name.pop(counter)
            counter += 1
        self.birth_day_dic["birthday"] = birthdays
        self.birth_day_dic["friend_name"] = friends_name

    def birthday_reminder(self):
        date_now = datetime.datetime.now()

        date_now = date_now.strftime("%d.%m.%Y")



        birthdays = self.birth_day_dic["birthday"]
        friends_name = self.birth_day_dic["friend_name"]
        counter = 0

        friends_list = list()

        for i in birthdays:

            if i == date_now:
                friends_list.append(friends_name[counter])

            counter += 1
        if len(friends_list) > 0:
            return True, friends_list
        return False, friends_list
