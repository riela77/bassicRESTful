class Snack : 
    def __init__(self,no,s_com,s_name,s_due,s_price,s_weight):
        self.no=no
        self.s_com =s_com
        self.s_name=s_name
        self.s_due=s_due
        self.s_price=int(s_price)
        self.s_weight=int(s_weight)

    def __str__(self):
        return f"[{self.no}] {self.s_com} - {self.s_name} | {self.s_due} | {self.s_price}원, {self.s_weight}g"