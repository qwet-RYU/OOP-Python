from hero import Hero

class Monster(Hero):
    def __init__(self, name, hp, ):
        super().__init__(name, hp, job="Monster")

    #fungsi status
    def __str__(self):
        status = "❤  HIDUP"
        return (f"[Monster] | {self.name} HP : {self.hp} | {status}")
        if self.hp ==0:
            status =" ☠  MATI"
    
    