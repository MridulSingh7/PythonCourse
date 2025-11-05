class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
#static methods do not need object creation to be used, they can be used normally like this