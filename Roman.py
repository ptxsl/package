class Romano:
    @staticmethod
    def num_to_rom(num):
        string = ""
        if num == 0:
            return "N"

        roman_numerals = [
            ("M", 1000), ("CM", 900), ("D", 500), ("CD", 400),
            ("C", 100), ("XC", 90), ("L", 50), ("XL", 40),
            ("X", 10), ("IX", 9), ("V", 5), ("IV", 4), ("I", 1)
        ]

        for roman, value in roman_numerals:
            while num >= value:
                string += roman
                num -= value

        return string

num=int(input("Inserta un número: "))
print(Romano.num_to_rom(num))
