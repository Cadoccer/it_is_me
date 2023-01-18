months = {'January': 31, 'February': 29, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

electricty_power_cost = 100 # bill comes at end of month so this is just a placeholder number rn
gas_power_cost = 124 # cost of one gas bottle as I prob will only use one before yall arrive but if i use 2 i will decrease this proportionally
total_internet_cost = 93

current_month = 'February'
num_days_in_month = months[current_month]

def counts_total_days(people):
    total_days = 0
    for person in people:
        name, day = person
        total_days += (num_days_in_month) - (day-1) #the -1 is needed eg 30-1=29 should be 30-0=30
    return total_days

def i_do_the_thing(person, total_days):
    """ it does the thing """
    name, day = person
    return (((num_days_in_month) - (day-1)) / total_days)

def nice_message(person, payment_percentage):
    name, day = person
    print('-' * 60)
    print (f" {name}: {payment_percentage * 100 :.2f}% of electrical power which is ${payment_percentage * electricty_power_cost:.2f}\n 20% of the $124 second gas bottle which is ${0.2 * 124:.2f}\n The internet plan is ${payment_percentage * 93:.2f}\n This comes to a total of:\n {payment_percentage * electricty_power_cost:.2f} + {0.2 * 124:.2f} + {payment_percentage * 93:.2f} = ${payment_percentage * electricty_power_cost + 0.2 * 124 + 0.2 * 93:.2f}")

def main():
    cade = ['Cade', 1]
    max_d = ['Max', 10]
    ben = ['Ben', 2]
    will = ['Will', 11]
    jake = ['Jake', 14]
    people = [cade, max_d, ben, will, jake]
    total_days = counts_total_days(people)
    for person in people:
        payment_percentage = i_do_the_thing(person, total_days)
        nice_message(person, payment_percentage)
main()
