from validate_docbr import CPF


def normalizar_cpf(cpf: str) -> str:
    return "".join(caractere for caractere in cpf if caractere.isdigit())


def cpf_valido(cpf: str) -> bool:
    return CPF().validate(cpf)
