import pandas as pd


def show_position_menu():
    print("\nWybierz skąd chciałbyś zobaczyć wiersze:")
    print("1. Początek")
    print("2. Dowolna pozycja")
    print("3. Koniec")


def get_starting_position() -> int:
    starting_position: int = int(input("Wybierz opcję: "))
    if 1 <= starting_position <= 3:
        return starting_position
    print("\nNieprawidłowy wybór. Spróbuj ponownie.")
    get_starting_position()


def format_column_name(column_name: str) -> str:
    column_name = column_name.strip().capitalize()
    match column_name:
        case "Hp":
            return column_name.upper()
        case "Sp. atk" | "Sp atk":
            return "Sp. Atk"
        case "Sp. def" | "Sp def":
            return "Sp. Def"
        case _:
            return column_name


def sorting_order():
    print("\nW jakiej kolejności chcesz posortować kolumny?")
    while True:
        order: str = input("(rosnąco - True / malejąco - False): ")
        order = order.strip().capitalize()
        match order:
            case "True":
                return True
            case "False":
                return False
            case _:
                print("Nie poprawna kolejność. Spróbuj ponownie.")
                break


class File:
    df = None

    @staticmethod
    def set_df(file_path: str) -> None:
        File.df = pd.read_csv(file_path)

    @staticmethod
    def show_file() -> None:
        print(File.df.to_string())

    @staticmethod
    def show_columns():
        column_names: list = File.df.columns.tolist()
        column_names.pop(0)
        print("\nNazwy wszystkich kolumn: ")
        print(File.df.columns.tolist())

    @staticmethod
    def show_n_rows() -> None:
        show_position_menu()
        starting_position: int = get_starting_position()
        number_of_rows: int = int(input("\nPodaj liczbę wierszy: "))
        match starting_position:
            case 1:
                print(File.df.head(number_of_rows))
            case 2:
                starting_row: int = int(input("Podaj wiersz, od którego chcesz zacząć: "))
                print(File.df.iloc[starting_row:starting_row + number_of_rows])
            case 3:
                print(File.df.tail(number_of_rows))

    @staticmethod
    def sort_by_column():
        File.show_columns()
        while True:
            column_name: str = input("Wybierz kolumnę: ").split(",")
            column_name = column_name[0]
            column_name = format_column_name(column_name)
            if column_name in File.df.columns:
                break
            else:
                print(f"\nNie ma kolumny o nazwie '{column_name}'. Spróbuj ponownie.")

        order: bool = sorting_order()
        print(File.df.sort_values(by=column_name, ascending=order).to_string())

    @staticmethod
    def show_selected_columns():
        File.show_columns()
        selected_columns: list = []
        while True:
            column_names: list = input("Wybierz kolumny (oddziel je przecinkiem): ").split(",")
            for column_name in column_names:
                column_name = format_column_name(column_name)
                if column_name in File.df.columns:
                    selected_columns.append(column_name)
                else:
                    print(f"Nie znaleziono kolumny {column_name}.")
            break

        print(File.df[selected_columns].to_string())
