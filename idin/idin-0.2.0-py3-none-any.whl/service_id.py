class ServiceID:
    """

    See 5.3.1 iDIN Requested- and DeliveredServiceID
    """

    ConsumerID = 16384
    Name = 4096
    Address = 1024
    DateOfBirth = 448
    Is18orOlder = 64
    Gender = 16
    Signing = 8
    Telephone = 4
    Email = 2

    @classmethod
    def all(cls):
        """Enable all information

        Note that this excludes `Signing` since this is not supported yet in
        IDIN.
        """
        return (
            cls.ConsumerID
            | cls.Name
            | cls.Address
            | cls.DateOfBirth
            | cls.Gender
            | cls.Telephone
            | cls.Email
        )
