"""
This file contains lists of basic knowledge about the Minecraft environment
represented as python code.  The code will either consist of simple hardcoded
atom insertion statements, or for more detailed knowledge, loops or functions
creating tens or hundreds of similar atoms according to some algorithm.  The
code should be broken down into a very modular format so very small chunks of
information can be fed into the atomspace one piece at a time, or read out to a
separate atomspace to compare against the atomspace of the bot to test how well
it learned grounded knowledge that we didn't tell it about.

Also, all code should try to input knowledge into the bot in the order "simple
to complex".  In this context, simple knowledge is what a typical player (for
example a 10 year old playing the game for the first time) would know going
into the game and complex are things they would only learn in game after
playing for a long time (things like the fact that creepers explode, or where
to find diamonds or redstone).  If we arrange the knowledge in this order we
can pass to each function a number representing how far along we want to teach
the bot that type of knowledge.  This will allow us to intiailize the bot to
different levels of grounded knowledge for each domain.  So we could load in
100% of the knowledge about breaking blocks, but nothing about enemies or
crafting recipes.  Then spawn a different instance of the bot that knows 50% of
all blocks, enemies, and crafting recipes; and so forth.
"""

from opencog.atomspace import types, TruthValue
from opencog.type_constructors import *
from opencog.atomspace import Atom
from atomspace_util import add_predicate

class GroundedKnowledge:

    def __init__(self, atomspace, space_server, time_server):

        self._atomspace = atomspace
        self._space_server = space_server
        self._time_server = time_server

    def load_block_knowledge(self, knowledge_level):
        """ Creates a number of atoms in atomspace which represent grounded
        knowledge about what kinds of blocks drop what resource when mined with
        a given tool.  The info is hardcoded into this python routine as a
        dictionary and then the dictionary info is converted into atomese by
        some for loops which loop over this dictionary.
        """

        print "\n\nLoading grounded knowledge: blocks and mining"
        print     "---------------------------------------------"

        """ This is a python dictionary of block types (dirt, grass, etc).  For
        each block type entry there is a second dictionary of (tool, resource)
        entries.  This is interpreted as "if a block of type B is mined with
        tool T it will yeild resource R".  Note that some combinations return
        "NOTHING" since breaking these blocks with those specific tools does
        not drop a resource that can be picked up.
        """
        block_drops = {
            "DIRT" : {"SHOVEL" : "DIRT", "HAND" : "DIRT"},
            "GRASS" : {"SHOVEL" : "DIRT", "HAND" : "DIRT"},
            "STONE" : {"PICKAXE" : "COBBLESTONE", "HAND" : "COBBLESTONE"},
            "COBBLESTONE" : {"PICKAXE" : "COBBLESTONE", "HAND" : "COBBLESTONE"},

            "WATER" : {"HAND" : "NOTHING", "SHOVEL" : "NOTHING", "PICKAXE" : "NOTHING", "SWORD" : "NOTHING", "HOE" : "NOTHING", "AXE" : "NOTHING"},
            "LAVA" : {"HAND" : "NOTHING", "SHOVEL" : "NOTHING", "PICKAXE" : "NOTHING", "SWORD" : "NOTHING", "HOE" : "NOTHING", "AXE" : "NOTHING"},
            "SAND" : {"SHOVEL" : "SAND", "HAND" : "SAND"},
            "GRAVEL" : {"SHOVEL" : "GRAVEL", "HAND" : "GRAVEL"},

            "COAL_ORE" : {"PICKAXE" : "COAL_ORE", "HAND" : "COAL_ORE"},
            "IRON_ORE" : {"STONE_PICKAXE" : "IRON_ORE", "HAND" : "NOTHING"},
            "GOLD_ORE" : {"IRON_PICKAXE" : "GOLD_ORE", "WOODEN_PICKAXE" : "NOTHING", "HAND" : "NOTHING"},
            "DIAMOND_ORE" : {"IRON_PICKAXE" : "DIAMOND", "WOODEN_PICKAXE" : "NOTHING", "HAND" : "NOTHING"},
            "LAPIS_ORE" : {"IRON_PICKAXE" : "LAPIS", "WOODEN_PICKAXE" : "NOTHING", "HAND" : "NOTHING"},
            "REDSTONE_ORE" : {"IRON_PICKAXE" : "REDSTONE_DUST", "WOODEN_PICKAXE" : "NOTHING", "HAND" : "NOTHING"},

            "OAK_WOOD" : {"AXE" : "OAK_WOOD", "HAND" : "OAK_WOOD"},
            "SPRUCE_WOOD" : {"AXE" : "SPRUCE_WOOD", "HAND" : "SPRUCE_WOOD"},
            "BIRCH_WOOD" : {"AXE" : "BIRCH_WOOD", "HAND" : "BIRCH_WOOD"},
            "JUNGLE_WOOD" : {"AXE" : "JUNGLE_WOOD", "HAND" : "JUNGLE_WOOD"},
        }

        block_type_root_atom = self._atomspace.add_node(types.ConceptNode, "BLOCK_TYPE")
        print block_type_root_atom

        # Loop over the outer dictionary of block types, storing the current type in 'block'.
        for block in block_drops.keys():
            print block

            # Create the atom for the block type itself and declare it a subtype of "BLOCK_TYPE"
            block_atom = self._atomspace.add_node(types.ConceptNode, block)
            inh_atom = self._atomspace.add_link(types.InheritanceLink, [block_atom, block_type_root_atom])
            print "The block material %s is a BLOCK_TYPE" % block
            print inh_atom
            
            # Loop over the dictionary of (tool, drops) entries for this specific block type.
            tooldict = block_drops[block]
            for tool in tooldict.keys():

                tool_atom = self._atomspace.add_node(types.ConceptNode, tool)
                drops_atom = self._atomspace.add_node(types.ConceptNode, tooldict[tool])
                pred_atom = add_predicate(self._atomspace, "MiningWithToolDrops", block_atom, tool_atom, drops_atom)

                print "If you mine a %s block with a %s you will get %s" % (block, tool, tooldict[tool])
                print pred_atom

    def load_tool_knowledge(self, knowledge_level):
        """ Creates nodes in the atomspace for each of the tools and their
        various material types.
        """

        print "\n\nLoading grounded knowledge: tools"
        print     "---------------------------------"

        tool_types = ("AXE", "SHOVEL", "PICKAXE", "HOE", "SWORD")
        special_tool_types = ("SHEARS", "FLINT_AND_STEEL")
        tool_names = []

        # Create the material variant names for the tools that are material specific.
        for tool in tool_types:
            for material in ("GOLD", "WOODEN", "STONE", "IRON", "DIAMOND"):
                atom_name = material + "_" + tool
                tool_names.append(atom_name)

        # Add on the list of tool names that only come in one variety.
        for name in special_tool_types:
            tool_names.append(name)

        # Loop over the whole list of tool names and for each name create the
        # actual atom in atomspace that represents that tool type.
        for name in tool_names:
            atom = self._atomspace.add_node(types.ConceptNode, name)
            print "Creating concept node for tool: %s" % name
            print atom

    def load_category_knowledge(self, knowledge_level):
        """ Creates inheritance links for a bunch of manually defined
        "convenience categories" which are useful for humans to interact with
        the bot, both in the python code and in chat communication.  These are
        also useful in rule learning because rules learned about something
        which is in a category with other things might also apply to those
        other things.  Having some basic categories to nudge the pattern mining
        algorithms in the right direction should make learning initial things
        about the world a bit easier.
        """

        print "\n\nLoading grounded knowledge: categories"
        print     "--------------------------------------"

        categories_dict = {
            "WOOD_BLOCK" : ("OAK_WOOD", "SPRUCE_WOOD", "BIRCH_WOOD", "JUNGLE_WOOD"),
            "STONE_BLOCK" : ("STONE", "COBBLESTONE"),
            "ORE_BLOCK" : ("COAL_ORE", "IRON_ORE", "GOLD_ORE", "DIAMOND_ORE", "LAPIS_ORE", "REDSTONE_ORE"),
            "PHYSICS_BLOCK" : ("WATER", "LAVA", "SAND", "GRAVEL"),
            "FLOWING_BLOCK" : ("WATER", "LAVA"),
            "FALLING_BLOCK" : ("SAND", "GRAVEL"),
        }

        for cat_base in categories_dict.keys():
            for subclass_object in categories_dict[cat_base]:
                base_atom = self._atomspace.add_node(types.ConceptNode, cat_base)
                subclass_atom = self._atomspace.add_node(types.ConceptNode, subclass_object)
                inh_atom = self._atomspace.add_link(types.InheritanceLink, [subclass_atom, base_atom])

                print "%s is a %s" % (subclass_object, cat_base)
                print inh_atom

