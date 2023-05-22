class Human:
    favorite_drink = 'beer'

    def __init__(self, age: int):
        self.age = age
        if age < 18:
            self.favorite_drink = 'juice'

    def drink(self):
        print(f"I'm {self.__class__.__name__} and I drink {self.favorite_drink}.")


class Worker(Human):
    def __init__(self, age: int, salary: int):
        super().__init__(age)
        self.salary = salary
        if salary >= 1000 and age >= 18:
            self.favorite_drink = "whiskey"

    def drink(self):
        print(f"I'm {self.__class__.__name__} my salary is {self.salary} and I drink {self.favorite_drink}.")


# Example usage
print(Human.favorite_drink)  # Output: beer

human = Human(15)
human.drink()  # Output: I'm Human and I drink juice.

worker1 = Worker(25, 1500)
worker1.drink()  # Output: I'm Worker and I drink whiskey.

worker2 = Worker(16, 1200)
worker2.drink()  # Output: I'm Worker and I drink juice.

worker3 = Worker(25, 500)
worker3.drink()  # Output: I'm Worker and I drink beer.
