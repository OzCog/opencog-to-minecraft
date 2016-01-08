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

class ToolKnowledge:

    tool_types = ("HAND", "AXE", "SHOVEL", "PICKAXE", "HOE", "SWORD", "SHEARS")

class GroundedKnowledge:

    def __init__(self, atomspace, space_server, time_server):

        self._atomspace = atomspace
        self._space_server = space_server
        self._time_server = time_server

    def load_block_knowledge(self, knowledge_level):

        print "\n\nLoading grounded knowledge: blocks and mining"
        print     "---------------------------------------------"

        block_drops = {
            "DIRT" : {"SHOVEL" : "DIRT", "HAND" : "DIRT"},
            "OAK_WOOD" : {"AXE" : "OAK_WOOD", "HAND" : "OAK_WOOD"},
        }

        for block in block_drops.keys():
            print block
            
            tooldict = block_drops[block]
            for tool in tooldict.keys():

                print "If you mine a %s block with a %s you will get %s" % (block, tool, tooldict[tool])
