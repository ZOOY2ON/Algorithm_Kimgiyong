a = "I eat %d apples."%3
b = "I eat " + str(3) + " apples"

print(a)
print(b)

number = 10
day = "three"
c = "I ate %d apples. so I was sick for %s days."%(number, day)
print(c)

d = "{}하세요. 반갑습니다.".format("안녕")
print(d)

e = "{name}님 안녕하세요. 반갑습니다.".format(name = "박주연")
print(e)

f = "{major} {name}님 안녕하세요. 반갑습니다.".format(name = "박주연", major = "게임공학과")
print(f)

name = "박주연"
g = f"나의 이름은 {name}입니다."
print(g)