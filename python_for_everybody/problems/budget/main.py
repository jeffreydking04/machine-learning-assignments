class Category:
    ledger = []
    balance = 0
    total_withdrawals = 0

    def __init__(self, name):
        self.name = name

    def __str__(self):
        stars_length = (30 - len(self.name)) / 2
        int_stars = int(stars_length)

        if stars_length == int_stars:
            stars_1 = stars_2 =  '*' * int_stars
        else:
            stars_1 = '*' * int_stars
            stars_2 = '*' * (int_stars + 1)
        
        return_str = f'{stars_1}{self.name}{stars_2}\n'
        
        for transaction in self.ledger:
            description = transaction['description'][:23]
            if len(description) < 23:
                description += ' ' * (23 - len(description))
            amount = transaction['amount']
            str_amount = str(amount)
            if amount == int(amount):
                str_amount += '.00'
            if len(str_amount) < 7:
                str_amount = ' ' * (7 - len(str_amount)) + str_amount
            return_str += f'{description}{str_amount}\n'
        
        return_str += f'Total: {self.balance}'
        return return_str

    def check_funds(self, amount):
        if self.balance - amount < 0:
            return False
        return True

    def get_balance(self):
        return self.balance

    def deposit(self, amount, description=''):
        self.balance += amount
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        self.deposit(-amount, description)
        self.total_withdrawals += amount
        return True

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True

    def clear_info(self):
        self.ledger = []
        self.balance = 0

def create_spend_chart(categories):
    total_withdrawals = 0
    max_name_length = 0
    the_gathering = {}

    for category in categories:
        name_length = len(category.name)
        total_withdrawals += category.total_withdrawals
        if name_length > max_name_length:
            max_name_length = name_length
        the_gathering[category.name] = {
            'name_length': name_length,
            'expenditures': category.total_withdrawals
        }

    these_strings_length = 12 + max_name_length

    histogram = 'Percentage spent by category\n'
    column_one = '1' + ' ' * (these_strings_length - 1)
    column_two = '0987654321' + ' ' * (these_strings_length - 10)
    column_three = '0' * 11 + ' ' * (these_strings_length - 11)
    column_four = '|' * 11 + ' ' * (these_strings_length - 11)
    dash_column = ' ' * 11 + '-' + ' ' * (these_strings_length - 11)

    these_strings = [
        column_one,
        column_two,
        column_three,
        column_four,
        dash_column
    ]

    for key, category in the_gathering.items():
        add_spaces = max_name_length - len(key)
        decile = int(category['expenditures'] * 10 / total_withdrawals)
        histogram_string = ' ' * (10 - decile) + 'o' * (decile + 1)
        histogram_string += '-' + key + (' ' * add_spaces) 
        these_strings.extend([histogram_string, dash_column, dash_column])

    for i in range(12 + max_name_length):
        for line in these_strings:
            histogram += line[i]
        histogram += '\n'

    return histogram[:-1]