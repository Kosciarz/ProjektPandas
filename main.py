from File import File


def show_main_menu():
    print("\nMenu:")
    print("1. Wyświetl wszystkie wiersze")
    print("2. Wyświetl określoną liczbę wierszy")
    print("3. Sortuj dane według kolumny")
    print("4. Wyświetl wybrane kolumny")
    print("5. Wyświetl stosunek siły do defensywy Pokemonów")
    print("6. Wyświetl top 10 Pokemonów z największą ilością punktów życia")
    print("7. Wyjdź")


def choice_selection():
    choice: int = int(input("Wybierz opcję: "))
    match choice:
        case 1:
            File.show_file()
        case 2:
            File.show_n_rows()
        case 3:
            File.sort_by_column()
        case 4:
            File.show_selected_columns()
        case 5:
            File.plot_attack_defense_distribution()
        case 6:
            File.show_most_hp_pokemons()
        case 7:
            exit(0)
        case _:
            print("\nNieprawidłowy wybór. Spróbuj ponownie.")
            choice_selection()


def main():
    file_path: str = "./pokemon.csv"
    File.set_df(file_path)

    while True:
        show_main_menu()
        choice_selection()


if __name__ == "__main__":
    main()
