from cmd import Cmd
from customer import Customer
from database import Database


class SaleInvoicePrompt(Cmd):
    Database.initialise(database='stack', host='localhost', user='a', password='j')
    customer_name_list = Customer.get_customer_name_list()
    prompt = "sale_invoice: "

    def do_n(self, args):
        if len(args) != 0:
            name = args
            if name not in self.customer_name_list:
                print("The customer name \'" + name + "\' does not exist")
                if name.count("(") == 1 and name.count(")") == 1:
                    new_name = input("Do you want to create a new customer \'" + name + "\'? (y/n): ")
                    if new_name == 'y':
                        Customer.add_customer(name)
                        self.customer_name_list.append(name)
                        self.prompt = name + ":"
                else:
                    print("New name must be entered in the format: name (place)")
            else:
                self.prompt = "sale_" + name + ": "

    def complete_n(self, text, line, start_index, end_index):
        # line = line.split("new ")[1]
        # print("Line is {}".format(line))
        mline = line.partition(' ')[2]
        # print("mline is "+ mline)  # Sh
        offs = len(mline) - len(text)  # negative value
        new_list = []
        for s in self.customer_name_list:
            if s.startswith(mline):
                new_list.append(s[offs:])
        return new_list
        # return [s[offs:] for s in customer_name_list if s.startswith(mline)]

    def do_quit(self, args):
        """Quits the program."""
        print("Quitting.")
        raise SystemExit
