class Customer:
    def __init__(self, first_name, family_name, age=None):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    """
    料金の計算ルール
    こども料金(20歳未満): 1000円
    おとな料金(20歳以上65歳未満): 1500円
    シニア料金(65歳以上): 1200円
    """

    def entry_fee(self):
        fee_child = 1000
        fee_adult = 1500
        fee_senior = 1200

        if self.age < 20:
            return fee_child

        if 20 <= self.age <= 65:
            return fee_adult

        if self.age >= 65:
            return fee_senior

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"


if __name__ == "__main__":

    # C-1
    ken = Customer(first_name="Ken", family_name="Tanaka")
    ken.full_name()  # "Ken Tanaka" という値を返す
    print(ken.full_name())

    tom = Customer(first_name="Tom", family_name="Ford")
    tom.full_name()  # "Tom Ford" という値を返す
    print(tom.full_name())

    # C-2
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    ken.age  # 15 という値を返す
    print(ken.age)

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    tom.age  # 57 という値を返す
    print(tom.age)

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    ieyasu.age  # 73 という値を返す
    print(ieyasu.age)

    # C-3
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    ken.entry_fee()  # 1000 という値を返す
    print(ken.entry_fee())

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    tom.entry_fee()  # 1500 という値を返す
    print(tom.entry_fee())

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    ieyasu.entry_fee()  # 1200 という値を返す
    print(ieyasu.entry_fee())

    # C-4
    ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
    ken.info_csv()  # "Ken Tanaka,15,1000" という値を返す
    print(ken.info_csv())

    tom = Customer(first_name="Tom", family_name="Ford", age=57)
    tom.info_csv()  # "Tom Ford,57,1500" という値を返す
    print(tom.info_csv())

    ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
    ieyasu.info_csv()  # "Ieyasu Tokugawa,73,1200" という値を返す
    print(ieyasu.info_csv())
