from src.logger_config import logger


def get_mask_card_number(numbers_card: int) -> str:
    """Получаем номер карты, возвращаем замаскированный"""
    str_number = str(numbers_card)
    try:
        mask_number = str_number[0:4] + " " + str_number[4:6] + "** ****" + " " + str_number[-4:]
        logger.info(f"Замаскированный номер карты: {mask_number}")
        return mask_number
    except Exception as e:
        logger.error(f"Неправильный номер карты, ошибка: {e}")
        return "Ошибка"


def get_mask_account(numbers_account: int) -> str:
    """Получаем номер счёта, возвращаем замаскированный"""
    str_number = str(numbers_account)
    try:
        mask_account = "**" + str_number[-4:]
        logger.info(f"Замаскированный номер счёта: {mask_account}")
        return mask_account
    except Exception as e:
        logger.error(f"Неправильнй номер карты, ошибка: {e}")
        return "Ошибка"
