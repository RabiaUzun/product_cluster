from utils import get_process_data, min_edit_distance, get_translate_table,\
    create_data_csv
from constants import *


def main():
    create_data_csv()
    translation_table = get_translate_table("ğĞıİöÖüÜşŞçÇ", "gGiIoOuUsScC")
    data = get_process_data("data.csv")
    for key in data:
        for i, value in enumerate(data[key]):
            # Convert letters
            value = value.translate(translation_table)
            for category_name in CATEGORIES.keys():
                if (min_edit_distance(category_name, value) < 5
                        and data[key] not in CATEGORIES[category_name]):
                    CATEGORIES[category_name].append(data[key])


if __name__ == "__main__":
    main()

print(CATEGORIES)
