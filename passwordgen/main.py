#!/usr/bin/env python3
import argparse
import secrets
import string
from typing import List


AMBIGUOUS = set("Il1O0|`~'\"[]{}()<>;:,./\\")
DEFAULT_LENGTH = 16


def build_charset(use_lower: bool, use_upper: bool, use_digits: bool, use_symbols: bool,
                  no_ambiguous: bool, exclude: str) -> str:
    """Constroi o conjunto de caracteres conforme as preferências."""
    charset = set()
    if use_lower:
        charset.update(string.ascii_lowercase)
    if use_upper:
        charset.update(string.ascii_uppercase)
    if use_digits:
        charset.update(string.digits)
    if use_symbols:
        # Símbolos comuns e estáveis (string.punctuation pode variar). Ajuste conforme necessidade.
        charset.update("!@#$%^&*+=?-_")
    if no_ambiguous:
        charset -= AMBIGUOUS
    if exclude:
        charset -= set(exclude)

    final = ''.join(sorted(charset))
    if not final:
        raise ValueError("Conjunto de caracteres vazio. Revise suas opções (exclusões ou flags).")
    return final


def count_classes(password: str) -> int:
    """Conta quantas classes distintas a senha possui (lower, upper, digits, symbols)."""
    classes = 0
    if any(c.islower() for c in password):
        classes += 1
    if any(c.isupper() for c in password):
        classes += 1
    if any(c.isdigit() for c in password):
        classes += 1
    if any(c in "!@#$%^&*+=?-_" for c in password):
        classes += 1
    return classes


def generate_one(length: int, charset: str, require_classes: int) -> str:
    """Gera uma senha e tenta satisfazer a diversidade mínima de classes."""
    # Geração principal
    while True:
        pwd = ''.join(secrets.choice(charset) for _ in range(length))
        if require_classes <= 1:
            return pwd
        if count_classes(pwd) >= require_classes:
            return pwd
        # Se não atingiu a diversidade, reamostra (simples e eficiente para charsets razoáveis).


def generate_batch(n: int, length: int, charset: str, require_classes: int) -> List[str]:
    return [generate_one(length, charset, require_classes) for _ in range(n)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Gerador de senhas sem GUI (criptograficamente seguro, usa secrets)."
    )
    parser.add_argument("-l", "--length", type=int, default=DEFAULT_LENGTH,
                        help=f"Comprimento da senha (padrão: {DEFAULT_LENGTH}).")
    parser.add_argument("-n", "--number", type=int, default=1,
                        help="Quantidade de senhas a gerar (padrão: 1).")
    parser.add_argument("--no-lower", action="store_true", help="Não usar letras minúsculas.")
    parser.add_argument("--no-upper", action="store_true", help="Não usar letras maiúsculas.")
    parser.add_argument("--no-digits", action="store_true", help="Não usar dígitos.")
    parser.add_argument("--no-symbols", action="store_true", help="Não usar símbolos.")
    parser.add_argument("--no-ambiguous", action="store_true",
                        help="Evitar caracteres ambíguos (ex.: Il1O0, []{}()<> etc.).")
    parser.add_argument("--exclude", type=str, default="",
                        help="Caracteres adicionais a excluir (string).")
    parser.add_argument("--require-classes", type=int, default=2,
                        help="Diversidade mínima de classes na senha (1–4).")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.length < 4:
        raise SystemExit("Comprimento mínimo recomendado é 4.")

    if not (1 <= args.require_classes <= 4):
        raise SystemExit("Parâmetro --require-classes deve estar entre 1 e 4.")

    # Flags de inclusão (por padrão tudo ativo)
    use_lower = not args.no_lower
    use_upper = not args.no_upper
    use_digits = not args.no_digits
    use_symbols = not args.no_symbols

    # Ajuste automático: se todas as classes forem desativadas, aborta.
    if not any([use_lower, use_upper, use_digits, use_symbols]):
        raise SystemExit("Todas as classes foram desativadas. Ative pelo menos uma.")

    # Se require-classes exige mais classes do que as ativadas, ajusta/avisa.
    active_classes = sum([use_lower, use_upper, use_digits, use_symbols])
    if args.require_classes > active_classes:
        print(f"Aviso: --require-classes={args.require_classes} > classes ativas ({active_classes}). "
              f"Ajustando para {active_classes}.")
        require_classes = active_classes
    else:
        require_classes = args.require_classes

    charset = build_charset(
        use_lower=use_lower,
        use_upper=use_upper,
        use_digits=use_digits,
        use_symbols=use_symbols,
        no_ambiguous=args.no_ambiguous,
        exclude=args.exclude,
    )

    passwords = generate_batch(args.number, args.length, charset, require_classes)
    for p in passwords:
        print(p)


if __name__ == "__main__":
    main()
