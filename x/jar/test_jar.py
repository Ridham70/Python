from jar import Jar


def test_init():
    jar_1 = Jar()
    jar_2 = Jar(5)
    assert jar_1.capacity == 12
    assert jar_1.size == 0
    assert jar_2.capacity == 5
    assert jar_2.size == 0



def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(7)
    assert jar.size == 7
    jar.deposit(2)
    assert jar.size == 9


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(2)
    assert jar.size == 10

if __name__ == "__main__":
    main()

