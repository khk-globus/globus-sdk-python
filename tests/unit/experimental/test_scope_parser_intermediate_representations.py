from globus_sdk.experimental.scope_parser._parser import (
    ScopeTreeNode,
    parse_scope_graph,
)


def test_graph_str_single_node():
    g = parse_scope_graph("foo")
    assert (
        str(g)
        == """\
digraph scopes {
  rankdir="LR";

  foo


}"""
    )


def test_graph_str_single_optional_node():
    g = parse_scope_graph("*foo")
    assert (
        str(g)
        == """\
digraph scopes {
  rankdir="LR";

  *foo


}"""
    )


def test_graph_str_single_dependency():
    g = parse_scope_graph("foo[bar]")
    assert (
        str(g)
        == """\
digraph scopes {
  rankdir="LR";

  foo

  foo -> bar;

}"""
    )


def test_graph_str_optional_dependency():
    g = parse_scope_graph("foo[bar[*baz]]")
    assert (
        str(g)
        == """\
digraph scopes {
  rankdir="LR";

  foo

  foo -> bar;
  bar -> baz [ label = "optional" ];

}"""
    )


def test_treenode_repr():
    t = ScopeTreeNode("foo", optional=False)
    assert repr(t) == "ScopeTreeNode('foo')"

    t = ScopeTreeNode("foo", optional=True)
    assert repr(t) == "ScopeTreeNode('foo', optional=True)"

    t = ScopeTreeNode("foo", optional=False)
    t.dependencies = [ScopeTreeNode("bar", optional=False)]
    assert (repr(t)) == "ScopeTreeNode('foo', dependencies=[ScopeTreeNode('bar')])"
