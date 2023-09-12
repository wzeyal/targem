import unittest

from utils import translate_sentence


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sen1 = "מה נשמע ?"
        arabic = translate_sentence(sen1)
        self.assertEqual(arabic, "אֵיש (אִנְסַמַע)")

    def test_verbs(self):
        sen1 = "קראתי"
        arabic = translate_sentence(sen1)
        self.assertEqual(arabic, "(קִרִי)")

    def test_multiple_verbs(self):
        sen1 = "רציתי לפתוח"
        arabic = translate_sentence(sen1)
        self.assertEqual(arabic, "(כַּאן בִּדוֹ) (פַתְח)")

    def test_noun(self):
        sen1 = "מכונית"
        arabic = translate_sentence(sen1)
        self.assertEqual(arabic, "סַיַארַה")

    def test_verb_and_nouns(self):
        sen1 = "רציתי לפתוח את המכונית"
        arabic = translate_sentence(sen1)
        print(arabic)
        self.assertEqual(arabic, "(כַּאן בִּדוֹ) (פַתְח)  סַיַארַה")

    def test_long_sen1(self):
        sen1 = 'לא ראיתי אותך קודם, למה אתה בוכה?'
        arabic = translate_sentence(sen1)
        print(arabic)
        self.assertEqual(arabic, "מַא (שַאף) אִיַאכִּי סַאבֵּק לֵיש אִנְתֵ (בַּכַּא)")

    def test_long_sen2(self):
        sen1 = 'הם לא רוצים לפתוח את החלונות!'
        arabic = translate_sentence(sen1)
        print(arabic)
        self.assertEqual(arabic, "הֻםֵ מַא (כַּאן בִּדוֹ) (פַתְח)  שַבַּאבִּיכּ")

    def test_single_verb(self):
        sen1 = 'אוהב'
        arabic = translate_sentence(sen1)
        print(arabic)
        self.assertEqual(arabic, "(חַבּ)")

    def test_mixed_hebrew(self):
        sen1 = "קוראים לי אפרים קישון"
        arabic = translate_sentence(sen1)
        print(arabic)
        self.assertEqual(arabic, "(קִרִי) אִלַא **אפרים** **קישון**")

    def test_close_transaltion(self):
        sen1 = "לפתוח"
        arabic = translate_sentence(sen1)
        print(arabic)
        self.assertEqual(arabic, "~לַאפְתַה *פַתְח*")


if __name__ == '__main__':
    unittest.main()
