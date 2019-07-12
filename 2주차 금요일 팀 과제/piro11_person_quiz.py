from random import randint
import random, piro11_DB
from time import sleep
import os
cls = lambda: os.system('cls')

def clear():
    cls()
    print()

def input_int(text):
    try:
        return int(input(text).strip())
    except Exception as e:
        print("\n입력 오류입니다. 다시 입력해주세요.\n")
        return input_int(text)
def print_board(text, n):
    print("┌", "─"*n, "┐", sep="")
    print("│", text, '│')
    print("└", "─"*n, "┘\n", sep="")

class game_start:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        clear()

    def question_start(self):
        print_board(self.title, 27)
        print('게임을 시작하시겠습니까?\n\n(시작하려면 \'START\' 를 입력해주세요.)\n')
        a = input('>> ')
        if a.upper() == 'START':
            clear()
            self.print_description()
            return True
        else:
            return False

    def print_description(self):
        print_board(self.title+" 설명", 32)
        print(self.description, '\n')

class user:
    def __init__(self):
        self.name = ''
        self.life = 3
        self.score = 0
        self.create_user()

    def create_user(self):
        print_board("캐릭터 생성", 13)
        self.name = input("캐릭터 이름을 입력해주세요.\n\n>> ")
        print()
        self.print_user_info()
        print('잠시 후 문제가 시작됩니다.\n')
        sleep(2)
        clear()

    def print_user_info(self):
        print('{0}님의 목숨은 {1}개 입니다.\n'.format(self.name, self.life))
        print('현재 점수는 {0}점 입니다.\n'.format(self.score))

    def print_user_result(self):
        print_board("게임 결과", 11)
        print('게임이 끝났습니다!\n')
        print('{0} 님의 점수는 {1}입니다.\n\n'.format(self.name, self.score))
        # 한번에 맞추면 10점, 힌트로 맞추면 5점, 틀리면 0점
        # 목숨 하나당 10점 130 115 100 85 70 0
        if self.life * 10 + self.score >= 115:
            print('당신의 등급은 A입니다! 피로그래밍 11기 인물을 잘 알고 있습니다!\n')
        elif self.life * 10 + self.score >= 100:
            print('당신의 등급은 B입니다! 피로그래밍 11기 인물을 대충 알고 있습니다.\n')
        elif self.life * 10 + self.score >= 85:
            print('당신의 등급은 C입니다... 피로그래밍 11기에 더 많은 관심을 가져주세요.\n')
        elif self.life * 10 + self.score >= 70:
            print('당신의 등급은 D입니다... 피로그래밍 11기에 더 많은 관심을 가져주세요.\n')
        else:
            print('당신의 등급은 F입니다... 피로그래밍 11기에 더 많은 관심을 가져주세요.\n')
        print("\n종료 하시려면 엔터를 입력해주세요. ", end="")
        input(">> ")
        cls()

    def solve_quiz(self, people, count):
        hint = Hint()
        num_list = []
        for i in range(0, count):
            if not self.check_end():
                self.print_user_result()
                return
            hint_check = False
            num = randint(0, len(people) - 1)
            while num_list.count(num) > 0:
                num = randint(0, len(people) - 1)
            num_list.append(num)

            print_board("{}번 문제".format(str(i + 1).zfill(2)), 11)

            case = randint(1, 3)
            if case == 1:
                print("다음 피로그래밍 11기 회원님의 이름을 맞춰 주세요!\n")
                print("나이 : {}\n\n학교 : {}\n\n학과 : {}\n\n".format(people[num]['age'], people[num]['univ'], people[num]['major']))
                print("이름에 대한 힌트가 필요하시다면, '힌트' 혹은 'HINT'를 입력하세요.\n\n(힌트를 사용하고 정답을 맞추면 5점입니다.)\n")
                answer = input("정답 입력 >> ")

                if answer.strip() == '힌트' or answer.strip().lower() == 'hint':
                    if hint.question():
                        print("위 회원님의 이름 초성은 '{hint}'입니다.\n".format(hint=people[num]['hint']))
                    answer = input("정답 입력 >> ")
                    hint_check = True
                result = answer.strip() == people[num]['name']
                self.quiz_result(result, hint_check, people[num], 'name')
            elif case == 2:
                print("피로그래밍 11기 '{}'님의 나이를 맞춰 주세요!\n".format(people[num]['name']))
                answer = input_int("정답 입력 >> ")
                result = answer == people[num]['age']
                self.quiz_result(result, False, people[num], 'age')
            elif case == 3:
                print("피로그래밍 11기 '{}'님의 학교를 맞춰 주세요!\n".format(people[num]['name']))
                print("학교 이름을 정확하게 입력해주세요. ex) OO대학교\n")
                answer = input("정답 입력 >> ")
                result = answer.strip() == people[num]['univ']
                self.quiz_result(result, False, people[num], 'univ')
            self.print_user_info()

            if result:
                sleep(2)
            else:
                sleep(2.5)
            clear()
        self.print_user_result()

    def quiz_result(self, result, hint_check, person, key):
        if self.processing_result(result, hint_check):
            print("\n\n정답입니다!\n")
        else:
            print("\n\n틀렸습니다!\n\n정답은 {correct}입니다! {name}씨에게 관심을 가져주세요.\n".format(name=person['name'], correct=person[key]))

    def processing_result(self, result, hint_check):
        if result and hint_check:
            self.score += 5
            return True
        elif result:
            self.score += 10
            return True
        else:
            self.life -= 1
            return False

    def check_end(self):
        if self.life > 0:
            return True
        else:
            return False

class Hint:
    def __init__(self):
        self.randlist = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.randlist = random.sample(self.randlist, 10)
        self.randlist_index = 0

        self.lambda_question = piro11_DB.lambda_question
        self.lambda_example = piro11_DB.lambda_example
        self.lambda_answer = piro11_DB.lambda_answer
        self.lambda_correct_answer = piro11_DB.lambda_correct_answer

    def question(self):
        print("\n\n다음 람다식을 풀어주세요. 문제를 맞추면 초성 이름이 주어집니다.\n")
        print("────────────────────────────────────────────────────────────────\n")
        print(self.lambda_question[self.randlist[self.randlist_index]])
        print("────────────────────────────────────────────────────────────────\n")

        print("1. {}\n\n2. {}\n\n3. {}\n\n4. {}\n\n".format(self.lambda_example[self.randlist[self.randlist_index]][0],
                                                    self.lambda_example[self.randlist[self.randlist_index]][1],
                                                    self.lambda_example[self.randlist[self.randlist_index]][2],
                                                    self.lambda_example[self.randlist[self.randlist_index]][3]))
        answer = input("정답을 입력해주세요. >> ").strip()
        if int(answer) == self.lambda_correct_answer[self.randlist[self.randlist_index]]:
            print("\n맞았습니다!\n")
            self.randlist_index += 1
            return True
        else:
            print("\n틀렸습니다! 정답은 {}번입니다.\n".format(self.lambda_correct_answer[self.randlist[self.randlist_index]]))
            print("\n다시 본 문제를 풀어주세요.\n")
            self.randlist_index += 1
            return False


people = piro11_DB.people
title = piro11_DB.title
description = piro11_DB.description

game = game_start(title, description)
if game.question_start():
    player = user()
    player.solve_quiz(people, 10)
else:
    cls()
