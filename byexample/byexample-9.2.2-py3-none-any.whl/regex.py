import regex as _regex

try:
    import cPickle as pickle
except ImportError:
    import pickle


class RegexEngine:
    def _compile(self, pattern, flags=0, **kargs):
        ''' Compile a pattern into a regex object. '''
        return _regex.compile(pattern, flags, kargs)

    def _unserialize(self, re_obj):
        return pickle.dumps(re_obj)

    def compile(self, pattern, flags=0, **kargs):
        ''' Compile a pattern into a regex object.

            If the regex object was created before and it is in the
            cache, return it directly, otherwise create it
            and save it in the cache.
        '''
        re_obj = self.cache.get((pattern, flags), None)

        if re_obj is None:
            re_obj = self._compile(pattern, flags, kargs)

        elif isinstance(re_obj, bytes):
            re_obj = self._unserialize(re_obj)

        self.update_entry((pattern, flags), re_obj)
        return re_obj
