from modules.admin import Admin

alex = Admin('alex', 'towe', 'alextowe@example.com', 'alextowe', '39807!^*_65@u209*(&(*795)$#%^&')
privileges = ["can add post", "can delete post", "can ban user"]
alex.privileges.privileges = privileges
alex.privileges.show_privileges()