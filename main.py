# using the Abstract factory
# method in class
class Monobank:

    def report(self):
        return "finance"

    def __str__(self):
        return "Monobank"

class Privatbank:

    def report(self):
        return "General"

    def __str__(self):
        return "Privatbank"

class Alfabank:

    def report(self):
        return "Clients"

    def __str__(self):
        return 'Alfabank'

# main method
if __name__ == "__main__":
    Monobank = Monobank()  # object for 1 class
    Privatbank = Privatbank()  # object for 2 class
    Alfabank = Alfabank()  # object for 3 class

    print(f'Name of the Bank is {Monobank} and its report is {Monobank.report()}')
    print(f'Name of the Bank is {Privatbank} and its report is {Privatbank.report()}')
    print(f'Name of the Bank is {Alfabank} and its report is {Alfabank.report()}')