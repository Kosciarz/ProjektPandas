import pandas as pd


class Program:
    file = None

    @staticmethod
    def set_file(file_path: str):
        df = pd.read_csv(file_path)
        Program.file = df

    @staticmethod
    def show_file():
        print(Program.file)

    @staticmethod
    def show_n_rows():
        starting_position: int = get_starting_position()
        number_of_rows: int = int(input("Podaj liczbę wierszy\n"))
        match starting_position:
            case 1:
                print(Program.file.head(number_of_rows))
            case 2:
                starting_row: int = int(input("Podaj wiersz, od którego chcesz zacząć\n"))
                print(Program.file.iloc[starting_row:starting_row + number_of_rows])
            case 3:
                print(Program.file.tail(number_of_rows))

    @staticmethod
    def show_columns():
        column_names = Program.file.columns.tolist()
        column_names.pop(0)
        print("Nazwy wszystkich kolumn: ")
        for index, name in enumerate(column_names, start=1):
            print(f"{index}. {name}")

    @staticmethod
    def sort_by_column(df):
        while True:
            print("Wybierz kolumnę, według której chcesz posortować dane:")
            Program.show_columns()
            column_name = input().capitalize().strip()
            if column_name in df.columns:
                break
            else:
                print(f"Nie ma kolumny o nazwie '{column_name}'. Spróbuj ponownie.")

        print(df.sort_values(by=column_name))


def get_starting_position():
    return int(input("Wybierz skąd chciałbyś zobaczyć wiersze (1 - 3):\n1 Początek\n2 Dowolna pozycja\n3 Koniec\n"))


def show_menu():
    print("\nMenu:")
    print("1. Pokaż wszystkie wiersze")
    print("2. Pokaż określoną liczbę wierszy")
    print("3. Sortuj dane według kolumny")
    print("4. Wyświetl wybrane kolumny")
    print("5. Wyjdź")


def choice_selection(choice):
    match choice:
        case 1:
            Program.show_file()
        case 2:
            Program.show_n_rows()
        case 3:
            Program.show_columns()
        case 4:
            Program.show_selected_columns()
        case 5:
            exit(0)
        case _:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")


def main():
    file_path: str = ".\pokemon.csv"
    Program.set_file(file_path)

    while True:
        show_menu()
        choice = int(input("Wybierz opcję: "))
        choice_selection(choice)


if __name__ == "__main__":
    main()