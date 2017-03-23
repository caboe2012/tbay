#code for project
from tbay import User, Item, Bid, session

# create 3 users
rachel = User(username = 'stern', password = 'abc')
drew = User(username = 'droopie', password = '123')
chad = User(username = 'aboe', password = 'xyz')

# create 1 item
baseball = Item(name = 'ball', description = 'round')

# have one user auction the item
chad.auction_items.append(baseball)

# have two users bid on the item
bid1 = Bid(price = 1, users = drew, item = baseball)
bid2 = Bid(price = 2, users = drew, items = baseball)
bid3 = Bid(price = 3, users = rachel, items = baseball)
bid4 = Bid(price = 4, users = rachel, items = baseball)    
session.add_all([chad, drew, rachel, baseball, bid1, bid2, bid3, bid4])
session.commit()

# find the highest bidder
max_bid = -1
highest_bidder = 'foobar'
for each in session.query(Bid).all():
    if each.price > max_bid:
        max_bid = each.price
        highest_bidder = each.user_id
print(session.query(User.username).filter(User.id == highest_bidder).all())