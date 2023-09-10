class Personal:

    def __init__(self, name, cell_phone, identification_num, birthday, email):
        self.name = name
        self.cell_phone = cell_phone
        self.identification_num = identification_num
        self.birthday = birthday
        self.email = email

    def to_string(self):
        print(f"[Current Personal] name: {self.name}, cell_phone {self.cell_phone}, birthday: {self.birthday}"
              + f", identification_num: {self.identification_num}, email: {self.email}")