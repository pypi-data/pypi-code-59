# """
# :meth:`sphinx.addnodes` allows the user to create additional node types as I understand it.
# """
# from docutils import nodes
#
# from docutils.parsers.rst import Directive, directives
#
# from sphinx.directives import ObjectDescription
# from sphinx.domains import Domain
# from sphinx import addnodes
#
# # from sphinx.locale import _
# # from sphinx.util.docutils import SphinxDirective
# #
# # class dbtable(nodes.Admonition, nodes.Element):
# #     pass
# #
# # def visit_dbtable_node(self, node):
# #     self.visit_admonition(node)
# #
# # def depart_dbtable_node(self, node):
# #     self.depart_admonition(node)
#
# # class dbfield(nodes.Admonition, nodes.Element):
# #     pass
# #
# # def visit_dbfield(self, node):
# #     self.visit_admonition(node)
# #
# # def depart_dbfield(self, node):
# #     self.depart_admonition(node)
#
# class TableDirective(ObjectDescription):
#     """Database Table Directive
#
#     This provides a directive for documenting the fields of a database table"""
#
#     has_content=True       #: Indicates that the directive is likely to have content.
#     required_arguments = 1 #: Indicates that there is one required argument, the table name.
#     option_spec = {
#         "schema" : directives.unchanged_required,
#     }
#
#     def handle_signature(self, sign, node):
#         """
#
#         I believe this sets up the signature/container node for the Database table
#
#         :param sign: The value for the signature
#         :param node: The current node for the signature
#         :return:     The value for sign
#         """
#         node += addnodes.desc_name(text=sign)
#         return sign
#
#     def add_target_and_index(self, name, sign, node):
#         """
#
#         :param name:
#         :param sign: The value for the signature
#         :param node: The current node for the signature
#         """
#         node['ids'].append('table' + '-' + sign)
#         # if 'noindex' not in self.options:
#         #     ingredients = [
#         #         x.strip() for x in self.options.get('contains').split(',')]
#         #
#         #     recipes = self.env.get_domain('recipe')
#         #     recipes.add_recipe(sign, ingredients)
#
#     # def run(self):
#     #     paragraph_node = nodes.paragraph(text='Hello World!')
#     #     return [paragraph_node]
#
# # class TodolistDirective(Directive):
# #
# #     def run(self):
# #         return [todolist('')]
#
# class DatabaseDomain(Domain):
#
#     name = 'database'
#     label = 'Database'
#     # roles = {
#     #     'ref': XRefRole()
#     # }
#     directives = {
#         'dbtable': TableDirective,
#     }
#     # indices = {
#     #     RecipeIndex,
#     #     IngredientIndex
#     # }
#     # initial_data = {
#     #     'recipes': [],  # object list
#     #     'recipe_ingredients': {},  # name -> object
#     # }
#
#     def get_full_qualified_name(self, node):
#         return '{}.{}'.format('database', node.arguments[0])
#
# def setup(app):
#     print("Loaded the Database extention")
#
#     app.add_domain(DatabaseDomain)
#     # app.add_directive("dbtable", TableDirective)
#
#     # app.add_node(dbfield,
#     #              html =(visit_dbfield, depart_dbfield),
#     #              latex=(visit_dbfield, depart_dbfield),
#     #              text =(visit_dbfield, depart_dbfield))
#     # app.add_node(dbtable,
#     #              html =(visit_dbtable_node, depart_dbtable_node),
#     #              latex=(visit_dbtable_node, depart_dbtable_node),
#     #              text =(visit_dbtable_node, depart_dbtable_node))
#
#     return {
#         'version': '0.1',
#         'parallel_read_safe': True,
#         'parallel_write_safe': True,
#     }

from collections import defaultdict

from docutils.parsers.rst import directives

from sphinx import addnodes
from sphinx.directives import ObjectDescription
from sphinx.domains import Domain
from sphinx.domains import Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode


class RecipeDirective(ObjectDescription):
    """A custom directive that describes a recipe."""

    has_content = True
    required_arguments = 1
    option_spec = {
        'contains': directives.unchanged_required,
    }

    def handle_signature(self, sig, signode):
        signode += addnodes.desc_name(text=sig)
        return sig

    def add_target_and_index(self, name_cls, sig, signode):
        signode['ids'].append('recipe' + '-' + sig)
        if 'noindex' not in self.options:
            ingredients = [
                x.strip() for x in self.options.get('contains').split(',')]

            recipes = self.env.get_domain('recipe')
            recipes.add_recipe(sig, ingredients)


class IngredientIndex(Index):
    """A custom index that creates an ingredient matrix."""

    name = 'ingredient'
    localname = 'Ingredient Index'
    shortname = 'Ingredient'

    def generate(self, docnames=None):
        content = defaultdict(list)

        recipes = {name: (dispname, typ, docname, anchor)
                   for name, dispname, typ, docname, anchor, _
                   in self.domain.get_objects()}
        recipe_ingredients = self.domain.data['recipe_ingredients']
        ingredient_recipes = defaultdict(list)

        # flip from recipe_ingredients to ingredient_recipes
        for recipe_name, ingredients in recipe_ingredients.items():
            for ingredient in ingredients:
                ingredient_recipes[ingredient].append(recipe_name)

        # convert the mapping of ingredient to recipes to produce the expected
        # output, shown below, using the ingredient name as a key to group
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for ingredient, recipe_names in ingredient_recipes.items():
            for recipe_name in recipe_names:
                dispname, typ, docname, anchor = recipes[recipe_name]
                content[ingredient].append(
                    (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class RecipeIndex(Index):
    """A custom index that creates an recipe matrix."""

    name = 'recipe'
    localname = 'Recipe Index'
    shortname = 'Recipe'

    def generate(self, docnames=None):
        content = defaultdict(list)

        # sort the list of recipes in alphabetical order
        recipes = self.domain.get_objects()
        recipes = sorted(recipes, key=lambda recipe: recipe[0])

        # generate the expected output, shown below, from the above using the
        # first letter of the recipe as a key to group thing
        #
        # name, subtype, docname, anchor, extra, qualifier, description
        for name, dispname, typ, docname, anchor, _ in recipes:
            content[dispname[0].lower()].append(
                (dispname, 0, docname, anchor, docname, '', typ))

        # convert the dict to the sorted list of tuples expected
        content = sorted(content.items())

        return content, True


class RecipeDomain(Domain):

    name = 'recipe'
    label = 'Recipe Sample'
    roles = {
        'ref': XRefRole()
    }
    directives = {
        'recipe': RecipeDirective,
    }
    indices = {
        RecipeIndex,
        IngredientIndex
    }
    initial_data = {
        'recipes': [],  # object list
        'recipe_ingredients': {},  # name -> object
    }

    def get_full_qualified_name(self, node):
        return '{}.{}'.format('recipe', node.arguments[0])

    def get_objects(self):
        for obj in self.data['recipes']:
            yield(obj)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node,
                     contnode):
        match = [(docname, anchor)
                 for name, sig, typ, docname, anchor, prio
                 in self.get_objects() if sig == target]

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            return make_refnode(builder, fromdocname, todocname, targ,
                                contnode, targ)
        else:
            print('Awww, found nothing')
            return None

    def add_recipe(self, signature, ingredients):
        """Add a new recipe to the domain."""
        name = '{}.{}'.format('recipe', signature)
        anchor = 'recipe-{}'.format(signature)

        self.data['recipe_ingredients'][name] = ingredients
        # name, dispname, type, docname, anchor, priority
        self.data['recipes'].append(
            (name, signature, 'Recipe', self.env.docname, anchor, 0))


def setup(app):
    app.add_domain(RecipeDomain)

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
