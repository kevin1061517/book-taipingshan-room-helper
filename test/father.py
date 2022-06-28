from son import son_func

# print('Call it remotely')
# son_func()

class Cars:
    pi = 0.36

    def __int__(self, color, seat, weight):
        self.color = color
        self.seat = seat
        self.weight = weight
        # self.set_weight(weight)

    # def get_weight(self):
    #     return self.__weight
    @property
    def weight(self):
        return self.__weight

    # def set_weight(self, value):
    #     if value < 0:
    #         raise ValueError('Car weight cannot be 0 or less..')
    #     self.__weight = value

    @weight.setter
    def weight(self, value):
        if value < 0:
            raise ValueError('Car weight cannot be 0 or less..')
        self.__weight = value

    def drive(self):
        self.test = 'test'
        print(f'My car is {self.test} and {self.seat} seats.')

mazda = Cars()
benz = Cars()
# print(isinstance(mazda, Cars))
Cars.pi = 0.123

values = [*range(10)] # 同 list(range(10))
names = ['Kevin']
combined = [*values, *names, *'python']
# print(combined)

heights = {'Mike': 170, 'Peter': 166}
combineds = {**heights, 'Test': 999}
# print(combineds)


