import pickle
from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must be 10 digits.")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        phone_to_remove = self.find_phone(phone)
        if phone_to_remove:
            self.phones.remove(phone_to_remove)

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            self.remove_phone(old_phone)
            self.add_phone(new_phone)
        else:
            raise ValueError(f"Phone number {old_phone} not found.")

    def find_phone(self, phone):
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        phones_str = "; ".join(p.value for p in self.phones)
        return f"Contact name: {self.name.value}, phones: {phones_str}"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())

    def save_to_file(self, filename="addressbook.pkl"):
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def load_from_file(cls, filename="addressbook.pkl"):
        try:
            with open(filename, "rb") as file:
                return pickle.load(file)
        except (FileNotFoundError, EOFError):
            return cls()


def save_data(book, filename="addressbook.pkl"):
    book.save_to_file(filename)


def load_data(filename="addressbook.pkl"):
    return AddressBook.load_from_file(filename)


def main():
    # Завантаження даних з файлу
    book = load_data()

    # Приклад роботи з адресною книгою
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("Поточні записи в книзі:")
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print("Після редагування:")
        print(john)

    # Видалення запису Jane
    book.delete("Jane")
    print("\nПісля видалення Jane:")
    print(book)

    # Збереження даних перед виходом з програми
    save_data(book)


if __name__ == "__main__":
    main()
