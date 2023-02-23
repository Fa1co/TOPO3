import datetime
import unittest
from My_App import MemoApp


class MemoAppTests(unittest.TestCase):
    def test_add_friend_birthday(self):
        memoApp = MemoApp.Memo_App()
        memoApp.add_friend_birthday('Alex', '20.05.2001')
        self.assertEqual(memoApp.birth_day_dic["birthday"][0], '20.05.2001')
        self.assertEqual(memoApp.birth_day_dic["friend_name"][0], 'Alex')


    def test_delete_friend_birthday(self):
        memoApp = MemoApp.Memo_App()
        memoApp.add_friend_birthday('Alex', '20.05.2001')
        memoApp.add_friend_birthday('Alex1', '20.05.2001')
        memoApp.add_friend_birthday('Alex2', '20.05.2001')
        memoApp.add_friend_birthday('Alex', '20.05.2001')
        memoApp.delete_friend_birthday('Alex', '20.05.2001')
        self.assertEqual(memoApp.birth_day_dic["birthday"], ['20.05.2001', '20.05.2001'])
        self.assertEqual(memoApp.birth_day_dic["friend_name"], ['Alex1', 'Alex2'])

    def test_birthday_reminder(self):
        memoApp = MemoApp.Memo_App()

        date_now = datetime.datetime.now()
        date_now = date_now.strftime("%d.%m.%Y")
        memoApp.add_friend_birthday('Alex', date_now)
        memoApp.add_friend_birthday('Alex1', date_now)
        memoApp.add_friend_birthday('Alex2', '23.02.2001')

        status, friend_name = memoApp.birthday_reminder()
        self.assertEqual(friend_name, ['Alex', 'Alex1'])
        self.assertTrue(status)

if __name__=="__main__":
    unittest.main()