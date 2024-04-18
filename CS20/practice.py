def my_sum(num1, num2):
  return num1 + num2


print(my_sum(4, 5))
print(my_sum(-3, 4))


def oddeven(num):
  if num % 2 == 0:
    return "Even"
  else:
    return "Odd"


print(oddeven(3))
print(oddeven(-5))
print(oddeven(12))


def city_formatting(city, country):
  return (city + ", " + country.upper())


print(city_formatting("Moose Jaw", "Canada"))
print(city_formatting("Shanghai", "China"))


def word_reverse(word):
  return word[3] + word[2] + word[1] + word[0]


print(word_reverse("prey"))
print(word_reverse("slap"))


def f1(numbertobedoubled):
  return numbertobedoubled * 2


def f2(doublednumber):
  if f1(doublednumber) % 3 == 0:
    return "Multiple"
  else:
    return "Not a Multiple"


print(f2(2))
print(f2(12))
';'
';'
';'
';'
';'
