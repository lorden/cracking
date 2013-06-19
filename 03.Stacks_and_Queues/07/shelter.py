import time


class Animal:
    name = None
    date_received = None

    def __init__(self, name):
        self.name = name
        self.date_received = time.time()

    def __str__(self):
        return self.name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class ShelterQueue:
    dogs = []
    cats = []
    oldest_dog = None
    oldest_cat = None

    def enqueue(self, animal):
        if isinstance(animal, Dog):
            if self.oldest_dog is None:
                self.oldest_dog = animal.date_received
            self.dogs.append(animal)
        else:
            if self.oldest_cat is None:
                self.oldest_cat = animal.date_received
            self.cats.append(animal)

    def dequeueDog(self):
        dog = self.dogs.pop(0)
        if self.dogs:
            self.oldest_dog = self.dogs[0].date_received
        else:
            self.oldest_dog = None
        return dog

    def dequeueCat(self):
        cat = self.cats.pop(0)
        if self.cats:
            self.oldest_cat = self.cats[0].date_received
        else:
            self.oldest_cat = None
        return cat

    def dequeueAny(self):
        if self.oldest_dog <= self.oldest_cat:  # Let's adopt more dogs
            return self.dequeueDog()
        else:
            return self.dequeueCat()


sq = ShelterQueue()
sq.enqueue(Dog('Max'))
sq.enqueue(Dog('Molly'))
sq.enqueue(Cat('Bella'))
sq.enqueue(Cat('Jack'))
print sq.dequeueAny()  # Max
print sq.dequeueCat()  # Bella
