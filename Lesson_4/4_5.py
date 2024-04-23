class Employee:
    def get_paid(self):
        pass


class Manager(Employee):
    def get_paid(self):
        return 35_000


class Worker(Employee):
    def get_paid(self):
        return 20_000