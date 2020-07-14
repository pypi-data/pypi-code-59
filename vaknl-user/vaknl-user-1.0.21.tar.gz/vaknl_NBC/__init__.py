import pickle


class NBC(object):
    """
    Singleton NBC class

    This means there is always only one instance of this object.
    When the NBC class is created it will load the NBC data from the NBC.pkl file.
    """
    __instance = None
    __nbc_data = None

    def __new__(cls):
        if NBC.__instance is None:
            NBC.__instance = object.__new__(cls)
            with open('vaknl_NBC/NBC.pkl', 'rb') as output:
                cls.__nbc_data = pickle.load(output)

        return NBC.__instance

    def get_by_giata_id(self, giata_id):
        return self.__nbc_data.get(giata_id)


if __name__ == '__main__':
    nbc = NBC()
    print(nbc.get_by_giata_id(18878))
    print(nbc.get_by_giata_id(123))
