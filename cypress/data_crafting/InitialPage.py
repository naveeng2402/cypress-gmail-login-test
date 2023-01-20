import csv
import random
from string import ascii_letters, ascii_lowercase, ascii_uppercase, digits, punctuation
from typing import List, Dict

DATA: List[List[str]] = list()


def empty_first_name():
    first_name = last_name = ""
    username = "".join([random.choice(ascii_letters + digits) for _ in range(15)])
    password = confirmPassword = "".join(
        [random.choice(ascii_letters + digits) for i in range(15)]
    )

    DATA.append(
        [
            "Empty Names",
            first_name,
            last_name,
            username,
            password,
            confirmPassword,
            "N",
            "Enter first name and surname",
        ]
    )


def already_taken_username():
    USER_NAMES = [
        "naveeng2402",
        "rishikasv1505",
        "naveenacademics",
        "payamma.krishna",
        "h26058549",
    ]

    for user_name in USER_NAMES:
        first_name = last_name = "".join(
            [random.choice(ascii_lowercase) for _ in range(random.randint(5, 11))]
        )
        username = user_name
        password = confirmPassword = "".join(
            [random.choice(ascii_letters + digits) for _ in range(15)]
        )

        DATA.append(
            [
                "Already taken Usernames",
                first_name,
                last_name,
                user_name,
                password,
                confirmPassword,
                "UN",
                "username is taken",
            ]
        )


def invalid_username():
    first_name = last_name = "".join(
        [random.choice(ascii_lowercase) for _ in range(random.randint(5, 11))]
    )
    user_name = "".join(
        [
            random.choice(ascii_letters + digits)
            + random.choice(punctuation.replace(".", ""))
            for _ in range(5, 9)
        ]
    )
    password = confirmPassword = "".join(
        [random.choice(ascii_letters + digits) for _ in range(15)]
    )

    DATA.append(
        [
            "Invalid Usernames",
            first_name,
            last_name,
            user_name,
            password,
            confirmPassword,
            "UN",
            "only letters",
        ]
    )


def empty_confirm_password():
    first_name = last_name = "".join(
        [random.choice(ascii_lowercase) for _ in range(random.randint(5, 11))]
    )
    user_name = "".join([random.choice(ascii_letters + digits) for _ in range(10, 16)])
    password = "".join([random.choice(ascii_letters + digits) for _ in range(15)])
    confirmPassword = ""

    DATA.append(
        [
            "Empty Password Confirmation",
            first_name,
            last_name,
            user_name,
            password,
            confirmPassword,
            "P",
            "Confirm your password",
        ]
    )


def password_small():
    first_name = last_name = "".join(
        [random.choice(ascii_lowercase) for _ in range(random.randint(5, 11))]
    )
    user_name = "".join([random.choice(ascii_letters + digits) for _ in range(10, 16)])
    password = confirmPassword = "".join(
        [random.choice(ascii_letters + digits) for _ in range(random.randint(5, 8))]
    )

    DATA.append(
        [
            "Small Password",
            first_name,
            last_name,
            user_name,
            password,
            confirmPassword,
            "P",
            "8 characters",
        ]
    )


def password_mismatch():
    first_name = last_name = "".join(
        [random.choice(ascii_lowercase) for _ in range(random.randint(5, 11))]
    )
    user_name = "".join([random.choice(ascii_letters + digits) for _ in range(16)])
    password = "".join(
        [random.choice(ascii_letters + digits) for _ in range(random.randint(8, 15))]
    )
    confirmPassword = "".join(
        [random.choice(ascii_letters + digits) for _ in range(random.randint(8, 15))]
    )

    DATA.append(
        [
            "Password Mismatch",
            first_name,
            last_name,
            user_name,
            password,
            confirmPassword,
            "P",
            "didn’t match",
        ]
    )


if __name__ == "__main__":
    for i in range(5):
        empty_first_name()
    for i in range(5):
        invalid_username()
    for i in range(5):
        empty_confirm_password()
    for i in range(5):
        password_small()
    for i in range(5):
        password_mismatch()

    already_taken_username()

    with open("../csv/InitialData.csv", "w") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "title",
                "firstName",
                "lastName",
                "userName",
                "password",
                "confirmPassword",
                "err_type",
                "err_text",
            ]
        )
        w.writerows(DATA)
