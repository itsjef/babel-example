# flake8: NOQA
from enum import Enum
from typing import Any


# See: https://docs.python.org/3.8/library/gettext.html#deferred-translations
def N_(message: Any) -> Any:
    return message


class StrEnum(str, Enum):
    pass


class NinjaError(StrEnum):
    __slots__ = "_value_", "code"

    def __new__(cls, template, code):
        obj = str.__new__(cls, template)
        obj._value_ = template
        obj.code = code
        return obj

    PASSWORD_TOO_SHORT = (
        N_("Password must be longer than %(min_length)s characters"),
        "E00073",
    )
    INVALID_USERNAME = (
        N_("Username cannot contain special characters"),
        "E00074",
    )

    def __str__(self):
        return self.value


def test_print_translation():
    import gettext
    import os

    LOCALES = os.listdir(os.path.join(os.path.dirname(__file__), "translations"))
    locale = os.getenv("LOCALE")

    if locale in LOCALES:
        lang = gettext.translation(
            "messages", localedir="translations", languages=[locale]
        )
        _ = lang.gettext
    else:
        _ = gettext.gettext

    print(_(NinjaError.PASSWORD_TOO_SHORT) % {"min_length": 8})
    print(_(NinjaError.INVALID_USERNAME))
    print(_("Hello World"))

    # Not translated on purpose, the original "Thank you" string will be printed
    print(_("Thank you!"))


# def test_store_enum():
#     from sqlalchemy import Column, MetaData, Table, create_engine
#     from sqlalchemy.types import Enum as EnumType
#
#     engine = create_engine("sqlite:///./database.db")
#     meta = MetaData()

#     t = Table("data", meta, Column("value", EnumType(NinjaError)))
#     meta.create_all(engine)

#     with engine.begin() as connection:
#         connection.execute(t.insert(), {"value": NinjaError.INVALID_USERNAME})
#         assert connection.scalar(t.select()) is NinjaError.INVALID_USERNAME


def main():
    test_print_translation()
    # test_store_enum()


if __name__ == "__main__":
    main()
