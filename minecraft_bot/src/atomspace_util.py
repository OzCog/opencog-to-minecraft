from opencog.atomspace import types, get_refreshed_types
from opencog.bindlink import bindlink
from opencog.type_constructors import *
types = get_refreshed_types()
from opencog.atomspace import Atom


def add_predicate(atomspace, predicatestr, *atoms):
    if len(atoms) == 1:
        target_atom = atoms[0]
    elif len(atoms) > 1:
        target_atom = atomspace.add_link(types.ListLink, atoms)
    else:
        raise RuntimeError('atomspace_util.add_predicate: atom list is empty!')
    return atomspace.add_link(types.EvaluationLink, [
        atomspace.add_node(types.PredicateNode, predicatestr),
        target_atom])


def add_location(atomspace, targetnode, maphandle, pos):
    return atomspace.add_link(types.AtLocationLink, [
        targetnode, maphandle,
        atomspace.add_link(types.ListLink, [
            atomspace.add_node(types.NumberNode, str(pos[0])),
            atomspace.add_node(types.NumberNode, str(pos[1])),
            atomspace.add_node(types.NumberNode, str(pos[2]))])])


def get_predicate(atomspace, predicate_name, target_node, num_of_val):
    if num_of_val == 1:
        var = VariableNode("$x")
    elif num_of_val > 1:
        var_nodes = []
        for i in range(num_of_val):
            var_nodes.append(VariableNode(str(i)))
        var = VariableList(*var_nodes)
    else:
        return None
    result_set = bindlink(atomspace,
                          BindLink(
                              var,
                              EvaluationLink(
                                  PredicateNode(predicate_name),
                                  ListLink(
                                      target_node,
                                      var
                                  )
                              ),
                              var
                          )
                          )
    try:
        result_set_out = result_set.out[0]
        if result_set_out.type == types.ListLink:
            result_list = result_set_out.out
            return result_list
        else:
            return result_set_out
    except IndexError as e:
        print "get predicate err: get no result %s" % e
        return None
# TODO


def get_most_recent_pred_val(
        atomspace, time_server, predicate_name, target_node, num_of_val):
    return [0] * num_of_val
