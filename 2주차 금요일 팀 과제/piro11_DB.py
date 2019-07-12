people = []
for i in range(0, 20):
    people.append(dict())
people[0] = {'name': '정성모',
             'univ': '남서울대학교',
             'major': '컴퓨터공학과',
             'age': 23, 'hint': 'ㅈㅅㅁ'}
people[1] = {'name': '전현규',
             'univ': '고려대학교',
             'major': '기계공학과',
             'age': 24, 'hint': 'ㅈㅎㄱ'}
people[2] = {'name': '김종혁',
             'univ': '한국외국어대학교',
             'major': '영문과',
             'age': 24, 'hint': 'ㄱㅈㅎ'}
people[3] = {'name': '김용성',
             'univ': '경기대학교',
             'major': '컴퓨터공학과',
             'age': 25, 'hint': 'ㄱㅇㅅ'}
people[4] = {'name': '김지훈',
             'univ': '경기대학교',
             'major': '수학과',
             'age': 24, 'hint': 'ㄱㅈㅎ'}
people[5] = {'name': '최범수',
             'univ': '중앙대학교',
             'major': '컴퓨터공학과',
             'age': 24, 'hint': 'ㅊㅂㅅ'}
people[6] = {'name': '황인준',
             'univ': '한양대학교',
             'major': '정보시스템학과',
             'age': 24, 'hint': 'ㅎㅇㅈ'}
people[7] = {'name': '김상원',
             'univ': '한양대학교',
             'major': '정보시스템학과',
             'age': 25, 'hint': 'ㄱㅅㅇ'}
people[8] = {'name': '이민은',
             'univ': '서울대학교',
             'major': '철학과',
             'age': 28, 'hint': 'ㅇㅁㅇ'}
people[9] = {'name': '이승환',
             'univ': '가천대학교',
             'major': '컴퓨터공학과',
             'age': 24, 'hint': 'ㅇㅅㅎ'}
people[10] = {'name': '곽진현',
              'univ': '한양대학교',
              'major': '물리학과',
              'age': 25, 'hint': 'ㄱㅈㅎ'}
people[11] = {'name': '김경훈',
              'univ': '중앙대학교',
              'major': '중문학과',
              'age': 28, 'hint': 'ㄱㄱㅎ'}
people[12] = {'name': '이한승',
              'univ': '연세대학교',
              'major': '전기전자공학과',
              'age': 23, 'hint': 'ㅇㅎㅅ'}
people[13] = {'name': '신한결',
              'univ': '한양대학교',
              'major': '영문학과',
              'age': 22, 'hint': 'ㅅㅎㄱ'}
people[14] = {'name': '김범수',
              'univ': '연세대학교',
              'major': '경제학과',
              'age': 20, 'hint': 'ㄱㅂㅅ'}
people[15] = {'name': '김지윤',
              'univ': '중앙대학교',
              'major': '응용통계학과',
              'age': 25, 'hint': 'ㄱㅈㅇ'}
people[16] = {'name': '길재은',
              'univ': '홍익대학교',
              'major': '자율전공학과',
              'age': 23, 'hint': 'ㄱㅈㅇ'}
people[17] = {'name': '김소현',
              'univ': '서울대학교',
              'major': '경영학과',
              'age': 23, 'hint': 'ㄱㅅㅎ'}
people[18] = {'name': '김정은',
              'univ': '한양대학교',
              'major': '정보시스템학과',
              'age': 21, 'hint': 'ㄱㅈㅇ'}
people[19] = {'name': '박소윤',
              'univ': '서울교육대학교',
              'major': '수학교육과',
              'age': 22, 'hint': 'ㅂㅅㅇ'}

title = '피로그래밍 11기 인물 게임'

description = '피로그래밍 11기 활동하는 사람들의 이름을 맞추는 게임입니다.\n\n\
주어진 정보(나이,학교,학과)와 일치하는 사람의 이름을 적어주시면 됩니다.\n\n총 20명 중 10명이 랜덤으로 나옵니다.\n\n\
목숨은 3개 주어지며 문제를 틀릴 때마다 목숨 하나를 잃습니다.\n\n문제를 맞출 때 마다 점수를 얻으며 많은 점수를 얻는 게임입니다.\n\n\
한 문제에 10점을 받으며, 남아 있는 목숨도 등급 평가에 반영됩니다.\n\n\
답을 알지 못할 경우 힌트를 통해 도움을 받을 수 있습니다.\n\n2주차 활동에 같이 하는 사람들 이름을 모르는건 아니겠죠??\n'

lambda_question = [0] * 10
lambda_example = [0] * 10
lambda_answer = [0] * 10
lambda_correct_answer = [0] * 10

lambda_question[0] = "a = [1, 2, 3, 4] \n\nb = [17, 12, 11, 10] \n\nlist(map(lambda x, y: x + y, a, b))\n"
lambda_example[0] = ["[14, 14, 14, 14]", "[18, 14, 14, 14]", "[18, 18, 18, 18]", "[20, 20, 20, 20]"]
lambda_answer[0] = "[18, 14, 14, 14]"
lambda_correct_answer[0] = 2
lambda_question[1] = "foo = [2, 18, 9, 22, 17, 24, 8, 12, 27] \n\nlist( filter(lambda x: x % 3 == 0, foo))\n"
lambda_example[1] = ["[18, 9, 24, 12, 27]", "[9, 24, 12, 27]", "[22, 18, 9, 24, 12, 27]", "[]"]
lambda_answer[1] = "[18, 9, 24, 12, 27]"
lambda_correct_answer[1] = 1
lambda_question[2] = "from functools import reduce \n\nreduce(lambda x,y: x+y, [1,2,3,4,5])\n"
lambda_example[2] = ["1", "10", "15", "20"]
lambda_answer[2] = "15"
lambda_correct_answer[2] = 3
lambda_question[3] = "alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**4]\n\nalist[0](10)\n"
lambda_example[3] = ["10", "40", "80", "100"]
lambda_answer[3] = "100"
lambda_correct_answer[3] = 4
lambda_question[4] = "alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**4]\n\nalist[1](2, 20)\n"
lambda_example[4] = ["10", "40", "80", "100"]
lambda_answer[4] = "40"
lambda_correct_answer[4] = 2
lambda_question[5] = "alist = [lambda m:m**2, lambda m,n:m*n, lambda m:m**4]\n\nalist[2](3)\n"
lambda_example[5] = ["10", "40", "81", "100"]
lambda_answer[5] = "81"
lambda_correct_answer[5] = 3
lambda_question[6] = "key = 'm'\n\naDict = {'m': lambda x:2*x, 'n': lambda x:3*x}\n\nprint(aDict[key](9))'\n"
lambda_example[6] = ["10", "15", "18", "20"]
lambda_answer[6] = "18"
lambda_correct_answer[6] = 3
lambda_question[7] = "alist = ['learn', 'python', 'step', 'by', 'step']\n\noutput = list(map(lambda x: x.upper() , alist))\n\nprint(output)\n"
lambda_example[7] = ["['LEARN', 'PYTHON', 'BY', 'STEP']", "['LEARN', 'PYTHON', 'STEP', 'BY']",
                     "['LEARN', 'BY', 'STEP']", "['LEARN', 'PYTHON', 'STEP', 'BY', 'STEP']"]
lambda_answer[7] = "['LEARN', 'PYTHON', 'STEP', 'BY', 'STEP']"
lambda_correct_answer[7] = 4
lambda_question[8] = "alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']\n\nvowels = ['a', 'e', 'i', 'o', 'u']\n\noutput = list(filter(lambda x: (x in vowels) , alphabets))\n\nprint(output)\n"
lambda_example[8] = "['a', 'e', 'i']", "['e', 'i']", "['a', 'e']", "[]"
lambda_answer[8] = "['a', 'e', 'i']"
lambda_correct_answer[8] = 1
lambda_question[9] = "key = 'm'\n\naDict = {'m': lambda x:2*x, 'n': lambda x:3*x}\n\nprint(aDict[key](9))\n"
lambda_example[9] = ["10", "15", "18", "20"]
lambda_answer[9] = "18"
lambda_correct_answer[9] = 3
