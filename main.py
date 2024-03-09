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
    def show_columns():
        column_names = Program.file.columns.tolist()
        column_names.pop(0)
        print("Nazwy wszystkich kolumn: ")
        for index, name in enumerate(column_names, start=1):
            print(f"{index}. {name}")


def main():
    file_path: str = ".\pokemon.csv"
    Program.set_file(file_path)
    Program.show_columns()
    # Program.show_file()

    return 0


if __name__ == "__main__":
    main()
