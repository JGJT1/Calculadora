"""
calculator.py

Funções para avaliar expressões matemáticas de forma segura usando `ast`.

Função principal: eval_expr(expr: str) -> int|float
"""

import ast
import operator as op
from typing import Union

# Operadores binários permitidos
_ALLOWED_BINOPS = {
    ast.Add: op.add,
    ast.Sub: op.sub,
    ast.Mult: op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.Mod: op.mod,
}

# Operadores unários permitidos
_ALLOWED_UNARYOPS = {
    ast.UAdd: op.pos,
    ast.USub: op.neg,
}


def _eval(node: ast.AST) -> Union[int, float]:
    """Avalia recursivamente um nó AST limitado a operações numéricas.

    Levanta ValueError para nós não permitidos.
    """
    if isinstance(node, ast.Expression):
        return _eval(node.body)

    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError(f"Constante não suportada: {node.value!r}")

    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        func = _ALLOWED_BINOPS.get(op_type)
        if func is None:
            raise ValueError(f"Operador binário não permitido: {op_type}")
        return func(left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        func = _ALLOWED_UNARYOPS.get(op_type)
        if func is None:
            raise ValueError(f"Operador unário não permitido: {op_type}")
        return func(_eval(node.operand))

    # Rejeitamos chamadas de função, nomes, atribuições e atributos
    if isinstance(node, (ast.Call, ast.Name, ast.Assign, ast.AugAssign, ast.Lambda, ast.FunctionDef, ast.Attribute)):
        raise ValueError(f"Construto não permitido na expressão: {type(node).__name__}")

    raise ValueError(f"Expressão não suportada: {ast.dump(node)}")


def eval_expr(expr: str) -> Union[int, float]:
    """Avalia uma expressão aritmética segura.

    Exemplo: eval_expr("2 + 3*(4-1)/5") -> 4.0
    """
    if not isinstance(expr, str):
        raise ValueError("A expressão deve ser uma string")

    try:
        parsed = ast.parse(expr, mode="eval")
    except SyntaxError as e:
        raise ValueError(f"Sintaxe inválida: {e.msg}") from e

    # Verificações rápidas: rejeitar nomes, atribuições e atributos
    for node in ast.walk(parsed):
        if isinstance(node, ast.Name):
            raise ValueError(f"Uso de nomes não permitido: {node.id}")
        if isinstance(node, (ast.Assign, ast.AugAssign, ast.Lambda, ast.FunctionDef, ast.Attribute)):
            raise ValueError("Construto não permitido na expressão")

    return _eval(parsed)


if __name__ == "__main__":
    while True:
        try:
            s = input("expressao> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not s:
            continue
        try:
            print(eval_expr(s))
        except Exception as e:
            print("Erro:", e)
