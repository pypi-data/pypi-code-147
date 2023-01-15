"""
Tests for the Intermediate Representation produced by the SQLalchemy parsers
"""

import ast
from copy import deepcopy
from unittest import TestCase

import cdd.parse.sqlalchemy
from cdd.tests.mocks.ir import (
    intermediate_repr_no_default_sql_doc,
    intermediate_repr_node_pk,
)
from cdd.tests.mocks.sqlalchemy import (
    config_decl_base_ast,
    config_decl_base_str,
    config_tbl_with_comments_ast,
    config_tbl_with_comments_str,
    foreign_sqlalchemy_tbls_mod,
    foreign_sqlalchemy_tbls_str,
    node_pk_tbl_ass,
)
from cdd.tests.utils_for_tests import run_ast_test, unittest_main


class TestParseSqlAlchemy(TestCase):
    """
    Tests whether the intermediate representation is consistent when parsed from different inputs.

    IR is a dictionary of form:
        {  "name": Optional[str],
           "type": Optional[str],
           "doc": Optional[str],
           "params": OrderedDict[str, {'typ': str, 'doc': Optional[str], 'default': Any}]
           "returns": Optional[OrderedDict[Literal['return_type'],
                                           {'typ': str, 'doc': Optional[str], 'default': Any}),)]] }
    """

    def test_from_sqlalchemy_table(self) -> None:
        """
        Tests that `parse.sqlalchemy_table` produces `intermediate_repr_no_default_sql_doc` properly
        """

        # Sanity check
        run_ast_test(
            self,
            config_tbl_with_comments_ast,
            gold=ast.parse(config_tbl_with_comments_str).body[0],
        )

        for variant in (
            config_tbl_with_comments_str,
            config_tbl_with_comments_str.replace(
                "config_tbl =", "config_tbl: Table =", 1
            ),
            config_tbl_with_comments_str.replace("config_tbl =", "", 1).lstrip(),
        ):
            ir = cdd.parse.sqlalchemy.sqlalchemy_table(ast.parse(variant).body[0])
            self.assertEqual(ir["name"], "config_tbl")
            ir["name"] = None
            self.assertDictEqual(ir, intermediate_repr_no_default_sql_doc)

    maxDiff = None

    def test_from_sqlalchemy(self) -> None:
        """
        Tests that `parse.sqlalchemy` produces `intermediate_repr_no_default_sql_doc` properly
        """

        # Sanity check
        run_ast_test(
            self,
            config_decl_base_ast,
            gold=ast.parse(config_decl_base_str).body[0],
        )

        ir = cdd.parse.sqlalchemy.sqlalchemy(deepcopy(config_decl_base_ast))
        self.assertEqual(ir["name"], "config_tbl")
        ir["name"] = None
        self.assertDictEqual(ir, intermediate_repr_no_default_sql_doc)

    def test_from_sqlalchemy_with_foreign_rel(self) -> None:
        """Test from SQLalchemy with a foreign key relationship"""
        # Sanity check
        run_ast_test(
            self,
            foreign_sqlalchemy_tbls_mod,
            gold=ast.parse(foreign_sqlalchemy_tbls_str),
        )
        ir = cdd.parse.sqlalchemy.sqlalchemy_table(deepcopy(node_pk_tbl_ass))
        self.assertDictEqual(ir, intermediate_repr_node_pk)


unittest_main()
