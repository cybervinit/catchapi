from api.models import User



# --------------------------------------- USERS -----------------------------------------------------

# User(username, email, country, current_balance, user_type, current_net_worth)

#def addUser(user1):
#	db.session.add(user1)
#	db.session.commit()

userList = []
userList.append(User('vinit', 'vinit@gmail.com', 'Canada', 100, 1, 100))
userList.append(User('bobby', 'bobby@gmail.com', 'Canada', 200, 1, 200))
userList.append(User('ryan', 'ryan@gmail.com', 'Canada', 250, 1, 250))
userList.append(User('john', 'john@gmail.com', 'Canada', 300, 1, 300))

userList.append(User('gary', 'gary@gmail.com', 'Canada', 110, 1, 110))
userList.append(User('jerry', 'jerry@gmail.com', 'Canada', 220, 1, 230))
userList.append(User('jimmy', 'jimmy@gmail.com', 'Canada', 301, 1, 400))
userList.append(User('robert', 'robert@gmail.com', 'Canada', 300, 1, 300))

userList.append(User('karen', 'karen@gmail.com', 'Canada', 111, 1, 123))
userList.append(User('jasmine', 'jasmine@gmail.com', 'Canada', 312, 1, 412))
userList.append(User('hetal', 'hetal@gmail.com', 'Canada', 152, 1, 745))
userList.append(User('sejal', 'sejal@gmail.com', 'Canada', 24, 1, 152))

userList.append(User('harry', 'harry@gmail.com', 'Canada', 152, 1, 285))
userList.append(User('rahul', 'rahul@gmail.com', 'Canada', 651, 1, 794))
userList.append(User('david', 'david@gmail.com', 'Canada', 846, 1, 1000))
userList.append(User('salman', 'salman@gmail.com', 'Canada', 101, 1, 142))

#for user in userList:
#	addUser(user)





