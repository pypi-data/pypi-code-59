"""malnet db utils"""


def md52Bucket(md5: str) -> str:
    if len(md5) != 32:
        raise ValueError("valid md5 value")

    bucket = "{}/{}/{}/{}/{}/{}".format(md5[0:4], md5[4:8], md5[8:12],
                                        md5[12:16], md5[16:20], md5[20:24])
    return bucket


def md52Object(md5: str) -> str:
    if len(md5) != 32:
        raise ValueError("valid md5 value")

    object_name = "{}/{}".format(md52Bucket(md5), md5)
    return object_name