from lib.password_checker import PasswordChecker

def test_length_check():
    checker = PasswordChecker()
    assert checker.check("aiaust") == "Password must be at least 20 characters."
    assert checker.check("nakjfhoasadfafaaffekbaenkfqaf") != "Password must be at least 20 characters."

def test_has_numbers():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") != "Password must contain numbers."

def test_has_symbol():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") == "Password must contain symbols."
    assert checker.check("i&^*rakjbajfoiua234jhksss") != "Password must contain symbols."

def test_has_upper_and_lower_case():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") == "Password must contain symbols."
    assert checker.check("i&^*rakjbajfoiua234jhksss") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KJGASOFUB&*^(18234726187)HH") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KOFUB&*^(18234726187)asfkgh") != "Password must contain uppercase and lowercase characters."

def test_has_animal():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") == "Password must contain symbols."
    assert checker.check("i&^*rakjbajfoiua234jhksss") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KJGASOFUB&*^(18234726187)HH") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KOFUB&*^(18234726187)asfkgh") == "Password must contain an animal."
    assert checker.check("KOFUB&*^(1823lIoN187)asfkgh") != "Password must contain an animal."

def test_numbers_add_to_60():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") == "Password must contain symbols."
    assert checker.check("i&^*rakjbajfoiua234jhksss") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KJGASOFUB&*^(18234726187)HH") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KOFUB&*^(18234726187)asfkgh") == "Password must contain an animal."
    assert checker.check("KOFUB&*^(1823lIoN187)asfkgh") == "Password must contain digits that add up to at least 60."
    assert checker.check("KOFUB&*^(9999lIoN999)asfkgh") != "Password must contain digits that add up to at least 60."

def test_question_start_word():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") == "Password must contain symbols."
    assert checker.check("i&^*rakjbajfoiua234jhksss") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KJGASOFUB&*^(18234726187)HH") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KOFUB&*^(18234726187)asfkgh") == "Password must contain an animal."
    assert checker.check("KOFUB&*^(1823lIoN187)asfkgh") == "Password must contain digits that add up to at least 60."
    assert checker.check("KOFUB&*^(9999lIoN999)asfkgh") == "Password must contain a word to start a question."
    assert checker.check("KOFUB&*^(9999lIoN999)Whengh") != "Password must contain a word to start a question."

def test_nums_16_or_less():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") == "Password must contain symbols."
    assert checker.check("i&^*rakjbajfoiua234jhksss") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KJGASOFUB&*^(18234726187)HH") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KOFUB&*^(18234726187)asfkgh") == "Password must contain an animal."
    assert checker.check("KOFUB&*^(1823lIoN187)asfkgh") == "Password must contain digits that add up to at least 60."
    assert checker.check("KOFUB&*^(9999lIoN999)asfkgh") == "Password must contain a word to start a question."
    assert checker.check("KOFUB&*^(9999lIoN999)Whengh") == "Password must not contain consecutive digits adding to more than 16."
    assert checker.check("9KOFU77g9&*^(9lIoN77)When9n77") != "Password must not contain consecutive digits adding to more than 16."

def test_has_english_monarch():
    checker = PasswordChecker()
    assert checker.check("kjafhsl") == "Password must be at least 20 characters."
    assert checker.check("iuoarakjbajfoiuafakjhksss") == "Password must contain numbers."
    assert checker.check("iuoarakjbajfoiua234jhksss") == "Password must contain symbols."
    assert checker.check("i&^*rakjbajfoiua234jhksss") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KJGASOFUB&*^(18234726187)HH") == "Password must contain uppercase and lowercase characters."
    assert checker.check("KOFUB&*^(18234726187)asfkgh") == "Password must contain an animal."
    assert checker.check("KOFUB&*^(1823lIoN187)asfkgh") == "Password must contain digits that add up to at least 60."
    assert checker.check("KOFUB&*^(9999lIoN999)asfkgh") == "Password must contain a word to start a question."
    assert checker.check("KOFUB&*^(9999lIoN999)Whengh") == "Password must not contain consecutive digits adding to more than 16."
    assert checker.check("9KOFU77g9&*^(9lIoN77)When9n77") == "Password must contain the first name of an English monarch."
    assert checker.check("9George77g9&^9lIoN77)When9n77") != "Password must contain the first name of an English monarch."

def test_passes_all():
    checker = PasswordChecker()
    assert checker.check("9George77g9&^9lIoN77)When9n77") == True
