from idin import ServiceID


def test_usage():
    assert ServiceID.ConsumerID | ServiceID.Address | ServiceID.Name == 21504
    assert (
        ServiceID.ConsumerID
        | ServiceID.Name
        | ServiceID.Address
        | ServiceID.DateOfBirth
        | ServiceID.Gender
        | ServiceID.Signing
        | ServiceID.Telephone
        | ServiceID.Email
        == 21982
    )


def test_all():
    assert ServiceID.all() == 21974
