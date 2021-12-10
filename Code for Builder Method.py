
class Monobank():

    def report(self):
        self.report = "finance"

    def operations(self):
        self.operations = "Exchange"

    def str(self):
        return "Monobank"

# concrete
class Privatbank():

    def report(self):
        self.report = "General"

    def operations(self):
        self.operations = "Credit"

    def str(self):
        return "Privatbank"

# concrete
class Alfabank():

    def report(self):
        self.report = "Clients"

    def available_batches(self):
        self.operations = "Deposit"

    def str(self):
        return "Alfabank"


# main method
if __name__ == "__main__":
    Monobank = Monobank()  # object for 1
    Privatbank = Privatbank()  # object for 2
    Alfabank = Alfabank()  # object for 3

    print(f'Name of Bank: {Monobank} and its report: {Monobank.report}')
    print(f'Name of Bank: {Privatbank} and its report: {Privatbank.report}')
    print(f'Name of Bank: {Alfabank} and its report: {Alfabank.report}')