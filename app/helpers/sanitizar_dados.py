import re


class SanitizarDados:
    @staticmethod
    def sanitizar(valor: str) -> str:
        return re.sub('[^0-9]', '', valor)
