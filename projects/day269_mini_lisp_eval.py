"""Day 269: Mini Lisp Evaluator."""

def tokenize(chars: str):
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(tokens):
    if not tokens:
        raise SyntaxError("unexpected EOF")
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(parse(tokens))
        tokens.pop(0)
        return L
    elif token == ')':
        raise SyntaxError("unexpected )")
    else:
        try: return int(token)
        except ValueError:
            try: return float(token)
            except ValueError: return token

def evaluate(x, env=None):
    if env is None:
        env = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b
        }
    if isinstance(x, str):
        return env[x]
    elif not isinstance(x, list):
        return x
    op = evaluate(x[0], env)
    args = [evaluate(arg, env) for arg in x[1:]]
    return op(*args)

if __name__ == "__main__":
    tokens = tokenize("(+ 10 (* 2 3))")
    ast = parse(tokens)
    assert evaluate(ast) == 16
    print("Day 269 Mini Lisp tests passed!")
