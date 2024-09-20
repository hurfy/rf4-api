from re import findall


class DataProcessor:
    def convert_to_kg(self, text: str) -> float:
        text = self.rm_html_chars(text)

        if "кг" in text and "." not in text:
            return float(findall(r"\d+", text)[0])

        return float(
            int("".join([i for i in findall(r"\d+", text)])) / 1000
        )

    def serialize_date(self, text: str) -> str:
        text    = self.rm_html_chars(text)
        d, m, y = text.split(".")

        return f"20{y}-{m}-{d}"

    @staticmethod
    def rm_html_chars(text: str) -> str:
        return text.replace("\xa0", "")