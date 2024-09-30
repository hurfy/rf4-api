from re import findall


class DataProcessor:
    def to_kg(self, text: str) -> float:
        text = self.clean(text)

        if "кг" in text and "." not in text:
            return float(findall(r"\d+", text)[0])

        return float(
            int("".join([i for i in findall(r"\d+", text)])) / 1000
        )

    def serialize(self, text: str) -> str:
        text    = self.clean(text)
        d, m, y = text.split(".")

        return f"20{y}-{m}-{d}"

    @staticmethod
    def clean(text: str) -> str:
        return text.replace("\xa0", "")