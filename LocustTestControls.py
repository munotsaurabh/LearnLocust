from locust import events, SequentialTaskSet, task, User, between


@events.test_start.add_listener
def on_test_start(**kwargs):
    print("###### Initiating Load test #####")


@events.test_stop.add_listener
def on_test_stop(**kwargs):
    print("###### Completing Load test #####")


class SearchRider(SequentialTaskSet):

    def on_start(self):
        print("Task execution started...")

    def on_stop(self):
        print("Task execution completed...")

    @task
    def likes_cars(self):
        print("I like to drive cars...")

    @task
    def likes_bikes(self):
        print("I like to ride bikes...")

    @task
    def exit_execution(self):
        self.interrupt()


class MyUser(User):
    wait_time = between(1, 2)
    tasks = [SearchRider]

    def on_start(self):
        print("Hatching new user...")

    def on_stop(self):
        print("Deleting the user...")
