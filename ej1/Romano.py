class Romano:

    numaromanizar=int()
    
    def __init__(self,numaromanizar:int):
        
        self.numaromanizar=numaromanizar

    def romanizar(self):

        roman=str("")

        while self.numaromanizar>0:

            if self.numaromanizar>=1000:

                roman=f"{roman}M"

                self.numaromanizar=int(self.numaromanizar-1000)

            elif self.numaromanizar>=900:

                roman = f"{roman}CM"

                self.numaromanizar = int(self.numaromanizar - 900)

            elif self.numaromanizar>=500:

                roman=f"{roman}D"

                self.numaromanizar=int(self.numaromanizar-500)

            elif self.numaromanizar>=400:

                roman = f"{roman}CD"

                self.numaromanizar = int(self.numaromanizar - 400)

            elif self.numaromanizar>=100:

                roman=f"{roman}C"

                self.numaromanizar=int(self.numaromanizar-100)

            elif self.numaromanizar>=90:

                roman = f"{roman}XC"

                self.numaromanizar = int(self.numaromanizar - 90)

            elif self.numaromanizar>=50:

                roman=f"{roman}L"

                self.numaromanizar=int(self.numaromanizar-50)

            elif self.numaromanizar>=40:

                roman = f"{roman}XL"

                self.numaromanizar = int(self.numaromanizar - 40)

            elif self.numaromanizar>=10:

                roman=f"{roman}X"

                self.numaromanizar=int(self.numaromanizar-10)

            elif self.numaromanizar>=9:

                roman = f"{roman}IX"

                self.numaromanizar = int(self.numaromanizar - 9)

            elif self.numaromanizar>=5:

                roman=f"{roman}V"

                self.numaromanizar=int(self.numaromanizar-5)

            elif self.numaromanizar>=4:

                roman = f"{roman}IV"

                self.numaromanizar = int(self.numaromanizar - 4)

            elif self.numaromanizar>=1:

                roman=f"{roman}I"

                self.numaromanizar=int(self.numaromanizar-1)

        return roman