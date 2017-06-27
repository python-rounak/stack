from list_completer import TabCompleter
from database import Database
from customer import Customer

Database.initialise(database='stack', host='localhost', user='a', password='j')
customer_name_list = Customer.get_customer_name_list()
TabCompleter(customer_name_list)
# print(customer_name_list)
customer_name = input("select customer: ")
customer_name_only = customer_name.split("(")[0].strip()
id_customer = Customer.get_customer_id(customer_name_only)
# print(id_customer)
sale_invoice_id = Customer.create_sale_invoice(id_customer)
print(sale_invoice_id)

product_name_list = Customer.get_product_name_list()
product_name_qty = ""
while product_name_qty != "quit":
    TabCompleter(product_name_list)
    # print(product_name_list)
    product_name_qty = input("sale_" + customer_name + ": ")
    if product_name_qty == "quit":
        break
    product_qty = product_name_qty.split(" ")[-1]
    # print(product_qty)
    product_name = product_name_qty.split(product_qty)[0].strip()
    # print(product_name)
    id_product = Customer.get_product_id(product_name)
    # print(product_id)
    rate, discount = Customer.get_rate_discount(id_customer, id_product)
    # print(rate,discount)