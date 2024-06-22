import os
import logging

# создаем логгер с уровнем логирования INFO; имя логгера выбираем отличное от логгера для модуля utils
masks_logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="../data/masks_log_file.log",  # записываем логи в файл
    filemode="w",
)  # метка 'w' означает перезапись лога в файл при каждом запуске
masks_handler = logging.FileHandler("../data/masks_log_file.log")
masks_logger.addHandler(masks_handler)

card_number: str = "2222333344445555"


def get_card_mask(card_number: str) -> str:
    """Функция для маскирования номера карты по шаблону XXXX XX** **** XXXX"""
    # str_output:str = ""
    masks_logger.info("Function for masking card number has started")
    if card_number.isspace is True:
        str_output = card_number[0:7] + "** **** " + card_number[15:20]
    else:
        str_output = (
            card_number[0:4] + " " + card_number[4:6] + "** **** " + card_number[12:16]
        )
    masks_logger.info(
        f"Function for masking card number has finished and returned a result of {len(str_output)} char."
    )

    return str_output


print(f"Маскированный номер карты: {get_card_mask(card_number)}")

acc_number: str = "73654108430135874305"


def get_acc_mask(acc_number: str) -> str:
    """Функция маск-ия номера сч. по шабл. **3587 (2 звездочки и последние 4 цифры)"""
    acc_mask = "**" + acc_number[12:16]
    masks_logger.info(
        f"Function for getting **XXXX has finished and returned a result of {len(acc_mask)} char."
    )
    return acc_mask


print(f"Маскированный номер счета: {get_acc_mask(acc_number)}")

# здесь пишем функцию для задания дополнительного
print()
# curr_dirct: str = input("Input a directory path: ")


def file_dir_dict(curr_dir: str) -> dict:
    """Функция возвращает словарь с кол-вом файлов и папок в данном каталоге"""
    count_files: int = 0
    count_dirs: int = 0
    dict_output: dict = {}

    if curr_dir == "":
        curr_dir = os.getcwd()
        masks_logger.info('Directory has not been provided; used the current dir')
    if os.path.isdir(curr_dir) is not True:
        masks_logger.info('A nonexistent directory has been provided; used the current dir')
        curr_dir = os.getcwd()
        new_list = os.scandir(curr_dir)
        pass
    else:
        new_list = os.scandir(curr_dir)
    for entry in new_list:
        if os.path.isfile(entry) is True:
            count_files += 1
        elif os.path.isdir(entry) is True:
            count_dirs += 1
    dict_output["files"] = count_files
    dict_output["folders"] = count_dirs
    masks_logger.info(f'Result of file_dir_dict func.: {count_dirs} fldrs and {count_dirs} files in the dir. in question')
    return dict_output

# пишем принты для разных сценариев работы функции file_dir_dict,
# чтобы проверить работу логгера в разных условиях

# print(file_dir_dict(""))
# print(file_dir_dict("../src"))
print(file_dir_dict('dddddd'))
