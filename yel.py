
# from logic import login as lg
# from logic import account

from logic import description as des

# data = []
# with open('yel_data.csv', newline='') as f:
#     reader = csv.reader(f)
#     # Skip title
#     for val,row in enumerate(reader):
#         if val == 0:
#             continue
#         data.append(row)
# print(data)

# 1
# call = lg.Login()

# # 2
# call = account.SelectTopic()

# 3
# call = des.ProdectDiscrib()
# call.addProduct()

# data = [['Ring 23', 'long ring', 'Ring 23', '10001', 'Fixed Rate', '1', '0', '0', '950', '2', '1000', '1', '10'], ['chine', 'golden chine with diamond', 'chine', '10012', 'Per Gram', '100', '24k', '0', '0', '4', '800', '2', '30'], ['croun', 'silver with gold', 'croun', '10050', 'Fixed Rate', '200', '0', '800', '0', '5', '400', '5', '50']]

# def printer(lister):
#     print('---',lister)

# list(map(printer,   data))


def hello():
    global name
    name = "Narendran"
    # print(name)
    product()
    def product():
        print(name)

hello()