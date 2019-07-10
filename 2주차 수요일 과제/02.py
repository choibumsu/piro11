from random import randint

class character:
    def __init__(self, name):
        self.name = name
        self.decide_job()

    def decide_job(self):
        self.intelligent = randint(6, 8)
        self.strength = randint(6, 8)
        if self.intelligent < self.strength:
            self.job = "전사"
        elif self.intelligent == self.strength:
            self.job = "궁수"
        else:
            self.job = "법사"

    def print_info(self):
        print("캐릭터 이름: {}".format(self.name))
        print("캐릭터 정보: 힘({}), 지력({})".format(self.strength, self.intelligent))
        print("캐릭터 직업: {}".format(self.job))


user_character = character(input("캐릭터의 이름을 입력하세요: "))
user_character.print_info()