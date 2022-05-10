from locust import TaskSet, task, User, between, SequentialTaskSet


# Basic TaskSet class - Random in nature. Any task can execute at any time.
class SearchFruits(TaskSet):
    @task
    def likes_mangoes(self):
        print("I like mangoes...")

    @task
    def likes_apples(self):
        print("I like apples...")


# TaskSet with weight. Weights are added to give more probability of execution for a task over the other
class SearchAnimals(TaskSet):
    @task(4)  # Given 4 as weight
    def likes_dogs(self):
        print("I like Dogs...")

    @task(1)  # Given 1 as weight
    def likes_cats(self):
        print("I like Cats...")


# Sequential Task Sets executes task in a sequential manner
class SearchRider(SequentialTaskSet):
    @task
    def likes_cars(self):
        print("I like to drive cars...")

    @task
    def likes_bikes(self):
        print("I like to ride bikes...")


class MyUser(User):
    wait_time = between(1, 2)
    # tasks = [SearchFruits]  # list of classes to execute
    # tasks = [SearchAnimals]
    tasks = [SearchRider]
