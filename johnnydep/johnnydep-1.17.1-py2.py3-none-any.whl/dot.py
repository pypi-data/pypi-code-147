from anytree.exporter import DotExporter

from johnnydep.compat import dict


def nodenamefunc(node):
    return node._name_with_extras(attr="project_name")


def edgeattrfunc(parent, child):
    spec = child.req.specifier
    if spec:
        return 'label="{}"'.format(spec)


def jd2dot(dist, comment="generated by https://github.com/wimglenn/johnnydep"):
    """exports johnnydist to graphviz DOT language
    https://graphviz.org/doc/info/lang.html
    nodes are the project name [+extras]
    edges will be labeled with any requirement constraints
    """
    dot_exporter = DotExporter(
        dist,
        name=str(dist.project_name).replace("-", "_"),
        nodenamefunc=nodenamefunc,
        edgeattrfunc=edgeattrfunc,
    )
    lines = []
    if comment:
        lines.append("# " + comment)
    lines += list(dict.fromkeys(dot_exporter))  # order preserving de-dupe
    result = "\n".join(lines)
    return result
