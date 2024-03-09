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


def get_starting_position():
    return int(input("Wybierz skąd chciałbyś zobaczyć wiersze (1 - 3):\n1 Początek\n2 Dowolna pozycja\n3 Koniec\n"))


def main():
    file_path: str = ".\pokemon.csv"
    Program.set_file(file_path)
    # Program.show_columns()
    Program.show_n_rows()
    # Program.show_file()

    return 0


if __name__ == "__main__":
    main()
