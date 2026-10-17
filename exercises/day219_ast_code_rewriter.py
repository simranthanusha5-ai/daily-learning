"""Day 219: AST NodeTransformer."""
import ast

class MultiplyToAddTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        self.generic_visit(node)
        if isinstance(node.op, ast.Mult):
            return ast.BinOp(left=node.left, op=ast.Add(), right=node.right)
        return node

def transform_source(source):
    tree = ast.parse(source)
    transformed = MultiplyToAddTransformer().visit(tree)
    ast.fix_missing_locations(transformed)
    code = compile(transformed, filename="<ast>", mode="eval")
    return eval(code)

if __name__ == "__main__":
    res = transform_source("5 * 3")
    assert res == 8
    print("Day 219 AST Transformer tests passed!")
