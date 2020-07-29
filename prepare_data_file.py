from utils import get_process_data, min_edit_distance, get_translate_table
from constants import *
import csv


products = [
    "supurge", "elektrikli supurge", "çay makınası", "kulaklık", "Telefon",
    "kablosuz kulaklık", "bebek arabası", "oyuncu laptop", "gaming bilgisayar",
    "Akilli telefon", "Süoürge",  "dizüstü bilgisayar", "telfon",
    "Çay Makinesi", "süpürge", "oyuncu monitor", "televizyon", "akıllı tv",
    "kulakiçi kulaklık", "bebek maması", "bebk bezi", "oyuncu klavye",
    "kedi maması"
]


def create_data_csv():
    """
    Create a csv file for products with ids.
    """
    ids = enumerate(products, 1)
    with open("data.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(list(ids))


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
