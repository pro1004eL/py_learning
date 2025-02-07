class User:
    def __init__(self, name, password, site_url):

        self.name = name
        self.password = password
        self.site_url = site_url

    def login(self):
        print(f'User {self.name} was logged in {self.site_url}')

    def logout(self):
        print(f'User {self.name} was logged out {self.site_url}')


dev_user = User('dev_Anton', 'dev_password', 'http://dev-something.com') # створення інстанса

dev_user.login() # поверне атрибут (властивість)
dev_user.logout()

print(dev_user.name) # виконає метод (функцію)




stage_user = User('stage_user', 'stage_password', 'http://stage-something.com')
prod_user = User('prod_user', 'prod_password', 'http://prod-something.com')




