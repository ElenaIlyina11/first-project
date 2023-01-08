from random import randint


class TestCase:

    def __init__(self, name, result):
        self.id = randint(111, 999)
        self.name = name
        self.steps = {}
        self.result = result

    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    def delete_step(self, step_number):
        if step_number in self.steps:
            del self.steps[step_number]
        else:
            print('The step {} is not found.'.format(step_number))

    def get_steps(self):
        return self.steps

    def set_result(self, result):
        self.result = result

    def get_test_case(self):
        print({
            'id': self.id,
            'Название': self.name,
            'Шаги': self.steps,
            'Ожидаемый результат': self.result
        })


test1 = TestCase('Добавление товара в корзину', 'Товар окажется в корзине')
test1.set_step(1, 'Перейти на сайт')
test1.set_step(2, 'Перейти в раздел Товары')
test1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test1.get_test_case()
