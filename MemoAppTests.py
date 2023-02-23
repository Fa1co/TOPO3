import unittest
from My_App import MemoApp


class MemoAppTests(unittest.TestCase):
    def test_add_friend_birthday(self):
        memoApp = MemoApp.Memo_App()
        memoApp.add_friend_birthday('Alex', '20.05.2001')
        self.assertEqual(memoApp.birth_day_dic["birthday"][0], '20.05.2001')
        self.assertEqual(memoApp.birth_day_dic["friend_name"][0], 'Alex')


if __name__=="__main__":
    unittest.main()