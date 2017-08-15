from api.models import User, NetWorthLeaderboard, Stock



# --------------------------------------- USERS -----------------------------------------------------

# User(username, email, country, current_balance, user_type, current_net_worth)


user_seed_list = []
user_seed_list.append(User('vinit', 'vinit@gmail.com', 'Canada', 100, 1, 100))
user_seed_list.append(User('bobby', 'bobby@gmail.com', 'Canada', 200, 1, 200))
user_seed_list.append(User('ryan', 'ryan@gmail.com', 'Canada', 250, 1, 250))
user_seed_list.append(User('john', 'john@gmail.com', 'Canada', 300, 1, 300))

user_seed_list.append(User('gary', 'gary@gmail.com', 'Canada', 110, 1, 110))
user_seed_list.append(User('jerry', 'jerry@gmail.com', 'Canada', 220, 1, 230))
user_seed_list.append(User('jimmy', 'jimmy@gmail.com', 'Canada', 301, 1, 400))
user_seed_list.append(User('robert', 'robert@gmail.com', 'Canada', 300, 1, 300))

user_seed_list.append(User('karen', 'karen@gmail.com', 'Canada', 111, 1, 123))
user_seed_list.append(User('jasmine', 'jasmine@gmail.com', 'Canada', 312, 1, 412))
user_seed_list.append(User('hetal', 'hetal@gmail.com', 'Canada', 152, 1, 745))
user_seed_list.append(User('sejal', 'sejal@gmail.com', 'Canada', 24, 1, 152))

user_seed_list.append(User('harry', 'harry@gmail.com', 'Canada', 152, 1, 285))
user_seed_list.append(User('rahul', 'rahul@gmail.com', 'Canada', 651, 1, 794))
user_seed_list.append(User('david', 'david@gmail.com', 'Canada', 846, 1, 1000))
user_seed_list.append(User('salman', 'salman@gmail.com', 'Canada', 101, 1, 142))


# NET WORTH RANK SEEDER

nwLb_seed_list = []
nwLb_seed_list.append(NetWorthLeaderboard(0, 1, 'vinit'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 2, 'bobby'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 3, 'ryan'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 4, 'john'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 5, 'gary'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 6, 'jerry'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 7, 'jimmy'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 8, 'robert'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 9, 'karen'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 10, 'jasmine'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 11, 'hetal'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 12, 'sejal'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 13, 'harry'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 14, 'rahul'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 15, 'david'))
nwLb_seed_list.append(NetWorthLeaderboard(0, 16, 'salman'))


# STOCKS SEEDER

stock_seed_list = []

stock_seed_list.append(Stock('Google', 'vinit'))
stock_seed_list.append(Stock('Google', 'sejal'))
stock_seed_list.append(Stock('Google', 'vinit'))
stock_seed_list.append(Stock('Google', 'sejal'))

stock_seed_list.append(Stock('Facebook', 'vinit'))
stock_seed_list.append(Stock('Facebook', 'gary'))
stock_seed_list.append(Stock('Facebook', 'hetal'))
stock_seed_list.append(Stock('Facebook', 'salman'))

stock_seed_list.append(Stock('Amazon', 'vinit'))
stock_seed_list.append(Stock('Amazon', 'rahul'))
stock_seed_list.append(Stock('Amazon', 'david'))
stock_seed_list.append(Stock('Amazon', 'john'))




