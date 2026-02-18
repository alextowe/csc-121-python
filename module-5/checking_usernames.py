current_users = ['admin', 'Alex', 'Ivy', 'lemon', 'dexter']
new_users = ['ALEX', 'james', 'Ivy', 'brandon']

current_users_lower = [user.lower() for user in current_users] 

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user} is unavailable.")
    else:
        print(f"{new_user} is available.")