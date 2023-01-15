from ast import *
from copy import copy

"""
Rewrites all occurences of augmented assignments
into normal assignments.
"""


class RewriteAugAssign(NodeTransformer):
    def visit_AugAssign(self, node: AugAssign) -> Assign:
        target_cp = copy(node.target)
        target_cp.ctx = Load()
        a = Assign(
            [self.visit(node.target)],
            BinOp(
                self.visit(target_cp),
                self.visit(node.op),
                self.visit(node.value),
            ),
        )
        return a
