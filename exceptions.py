class BaseError(Exception):
    """
    Base exception for project.
    """
    def __init__(self, msg=None, logger=None, telegram_update=None, telegram_msg=None):
        if msg is None:
            msg = "Неизвестная ошибка"

        if telegram_msg is None:
            telegram_msg = ('Что то пошло не так, попробуйте отменить текущее действие /cancel' +
                            'и ознакомиться с инструкцией по эксплуатации /help')

        if logger:
            logger.warn(msg)

        if telegram_update:
            telegram_update.message.reply_text(telegram_msg)

        super(BaseError, self).__init__(msg)


# class IncorrectValueError(BaseError):
#     def __init__(self, value, user_info, *args, **kwargs):
#
#         super().__init__(
#             *args, **kwargs,
#             msg="User (%s: %s %s) ввел некорректное значение для списания даты\n(%s)" % (
#                 user_info.id, user_info.first_name, user_info.last_name, value)
#         )
#
#
# class IncorrectDateError(BaseError):
#     def __init__(self, dt, user_info, *args, **kwargs):
#
#         super().__init__(
#             *args, **kwargs,
#             msg="User (%s: %s %s) ввел некорректную дату\n(%s)" % (
#                 user_info.id, user_info.first_name, user_info.last_name, dt)
#         )
