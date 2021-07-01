class Task:
    def __init__(self, title, description, expiration_date, priority):
        self.__title = title
        self.__description = description
        self.__expiration_date = expiration_date
        self.__priority = priority

    # === title === #
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    # === description === #
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    # === expiration_date === #
    @property
    def expiration_date(self):
        return self.__expiration_date

    @expiration_date.setter
    def expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date

    # === priority === #
    @property
    def priority(self):
        return self.__priority

    @priority.setter
    def priority(self, priority):
        self.__priority = priority
