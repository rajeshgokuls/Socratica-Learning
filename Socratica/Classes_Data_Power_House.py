import datetime
print(dir(datetime))

class User:
    """A member of Friend Dace, for now we are
        only storing their name and birthday.
        But soon we will store an uncomfortable amount of use information"""
    def __init__(self, full_name, birthday):

        self.name = full_name
        self.birthday = birthday  #yyyymmdd


        #Extract first and last name
        name_pieces = full_name.split(" ")
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

#help(User)
    def age(self):
        """Return the age of the user in years"""
        # since we use date, we import date time module

        # convert the birthday string into a date object, there is a way to do this in a single line but we focus on how to do in a general way..

        # we extract month, year and day as integers
        today = datetime.date(2001, 5, 12)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        # date object for user's birthday
        dob = datetime.date(yyyy, mm, dd)  # Date of birth
        # if you compute the difference between today and dob, you get a time delta object
        # the time delta object has field called days

        age_in_days = (today - dob).days
        # ignoring leap years, we can now compute age and year by dividing into 365

        age_in_years = age_in_days / 365
        # return age as integers

        # to test this method, create a user object once more

        return int(age_in_years)

user = User("Dave Bowman", "19710315")
print(user.age())











