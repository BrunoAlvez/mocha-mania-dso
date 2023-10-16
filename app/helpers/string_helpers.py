class StringHelpers:
    @staticmethod
    def snake_to_camel_case(string: str) -> str:
        return ''.join(palavra.title() for palavra in string.split('_'))
