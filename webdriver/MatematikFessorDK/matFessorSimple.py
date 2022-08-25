from MatFessorUtils import *
from EquationSolver import solveForX

#email = 'dicexem843@anlubi.com'
#password = 'sgkA54Kfdg'
email = 'ticoda7567+lasse@agrolivana.com'
password = 'pa45sswodgf4rd'

login(email, password)

chooseGrade(4)

chooseLesson(618)

startTest()

while True:
  for currentPage in range(1, 6):
    print('currentPage: ', currentPage)
    equation = findQuestion()
    while len(equation) < 1:
      equation = findQuestion()
      print('equation:', equation)
    solution = solveForX(equation)
    print('solution:', solution)
    choices = findChoices()
    while len(choices) < 1:
      choices = findChoices()
      print('choices:', list(choices))
    for i, choice in enumerate(choices):
      if choice == solution:
        print('choice:', choice)
        print('i:', i)
        setAnswer(i)
        break
    submitAnswer()
  turnInTest()
  again()


  

time.sleep(5)