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
        # Перевірка, що значення складається з 10 цифр
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Номер телефону повинен містити 10 цифр.")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone_number):
        self.phones.append(Phone(phone_number))

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def remove_phone(self, phone_number):
        phone = self.find_phone(phone_number)
        if phone:
            self.phones.remove(phone)

    def edit_phone(self, old_phone, new_phone):
        phone_to_edit = self.find_phone(old_phone)
        if phone_to_edit:
            self.add_phone(new_phone) #phone_to_edit.value = new_phone
            #Використовуємо існуючий метод для видалення старого телефону.
            self.remove_phone(old_phone)
        else:
            raise ValueError("Номер телефону не знайдено.")

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]

    def __str__(self):
        records = [str(record) for record in self.data.values()]
        return '\n'.join(records)

# Приклади використання
if __name__ == '__main__':
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    print("--- Усі записи в книзі ---")
    print(book)

    # Знаходження та редагування телефону для John
    print("\n--- Редагування телефону John ---")
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
    print(john)

    # Пошук конкретного телефону у записі John
    print("\n--- Пошук телефону 5555555555 для John ---")
    if john:
        found_phone = john.find_phone("5555555555")
        print(f"{john.name}: {found_phone}")

    # Видалення запису Jane
    print("\n--- Видалення запису Jane ---")
    book.delete("Jane")

    # Перевірка, що Jane видалено
    print("\n--- Перевірка всіх записів після видалення ---")
    print(book)