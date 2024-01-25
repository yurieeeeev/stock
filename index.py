from uuid import UUID, uuid4
from datetime import datetime, timedelta

# a = 18.01.2024
# b = 10days
# a + b => 28.01.2024


class Stock:
    def __init__(
        self,
        stock_id: int,
        location: str,
        capacity_sq_m: float,
        owner_id: UUID,
    ):
        self.__stock_id = stock_id
        self.__location = location
        self.__capacity_sq_m = capacity_sq_m
        self.__owner_id = owner_id


class Item:
    def __init__(
        self,
        item_id: int,
        stock_id: int,
        name: str,
        size: float,
        category: str,
        description: str,
        arrive_at: datetime,
        expiration_time: timedelta,
    ):
        self.__item_id = item_id
        self.__stock_id = stock_id
        self.__name = name
        self.__size = size
        self.__category = category
        self.__description = description
        self.__arrive_at = arrive_at
        self.__expiration_time = expiration_time


class User:
    def __init__(self, user_id: UUID, phone: str, username: str, password: str):
        self.__user_id = user_id
        self.__phone = phone
        self.__username = username
        self.__password = password


class Controller:
    def __init__(self):
        self.__current_user: User = None
        self.__current_stock: Stock = None

    def signup(self):
        user_id = uuid4()
        username = input("введите ваш ник: ")
        password = input("введите ваш пароль: ")
        phone = input("введите ваш телефон: ")

        new_user = User (
            user_id =user_id,
            phone=phone,
            username=username,
            password=password
        )
        database["user"].append(new_user)
        print("вы успешно зарегались!")
   
    def auth_user(self):
        pass

    def logout(self):
        pass

    def get_stock_information(self):
        pass

    def add_items_to_stock(self):
        pass

    def remove_items_in_stock(self):
        pass

    def move_item_to_diff_stock(self):
        pass

    def search_available_item(self):
        pass


database = {
    "users": [],
    "stocks": [],
    "items": [],
}

Controller = Controller()
Controller.signup

print(database["users"])