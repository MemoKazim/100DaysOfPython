logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)

bid_log = []
repeat = 'yes'

while repeat == 'yes':
    key_name = input("Type your name:\t")
    key_bid = input("Type your bid:\t$")

    bid_dict = {}
    bid_dict["name"] = key_name
    bid_dict["bid"] = key_bid

    bid_log.append(bid_dict)
    repeat = input("Other biders? ('yes' or 'no')\n:")


max = bid_log[0]['bid']
for i in range (len(bid_log)):
    if max < bid_log[i]['bid']:
        max = bid_log[i]['bid']
        name = bid_log[i]['name']

print(f'Winner is {name} with {max}$')
