# encoding: utf-8
# module EmitMapper
# from Wms.RemotingImplementation, Version=1.25.1.4, Culture=neutral, PublicKeyToken=null
# by generator 1.145
""" NamespaceTracker represent a CLS namespace. """
# no imports

# no functions
# classes

class Mapper():
    # no doc
    @staticmethod
    def MapTo(source, dest, config=None):
        """
        MapTo[(TSource, TDestination)](source: TSource, dest: TDestination) -> TDestination
        MapTo[(TSource, TDestination)](source: TSource, dest: TDestination, config: IMappingConfigurator) -> TDestination
        """
        pass

    @staticmethod
    def MapToNew(source, config=None):
        """
        MapToNew[(TSource, TDestination)](source: TSource) -> TDestination
        MapToNew[(TSource, TDestination)](source: TSource, config: IMappingConfigurator) -> TDestination
        """
        pass

    __all__ = [
        'MapTo',
        'MapToNew',
    ]

    Instance = Mapper()
    """hardcoded/returns an instance of the class"""

