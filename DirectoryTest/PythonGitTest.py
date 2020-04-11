import random
# random fun code
class GitTest:
    number = 0
    def __init__(self):
        print("This is GitTest no.{}\n".format(self.generate_git_test_number()) + str(self))

    def generate_git_test_number(self):
        GitTest.number += 1
        return self.number

    def __str__(self):
        return self.__class__.__name__ + str(self.number)

for num in range(random.randint(1, 11)):
    gitTestInstance = "gitTest" + str(num)
    gitTestInstance = GitTest()

# gitTest1 = GitTest()
# gitTest2 = GitTest()
