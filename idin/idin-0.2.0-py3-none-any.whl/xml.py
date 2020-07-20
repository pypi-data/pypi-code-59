import base64
import typing

import xmlsec
from lxml import etree

xmlsec.enable_debug_trace()


class VerificationError(IOError):
    pass


def load(content) -> etree._Document:
    parser = etree.XMLParser(resolve_entities=False)
    return etree.fromstring(content.strip(), parser=parser)


def sign(element, key: xmlsec.Key) -> None:
    """Sign the given element with the given key"""

    # Create the Signature node.
    signature = xmlsec.template.create(
        element, xmlsec.Transform.EXCL_C14N, xmlsec.Transform.RSA_SHA256,
    )
    ref = xmlsec.template.add_reference(signature, xmlsec.Transform.SHA256, uri="")
    xmlsec.template.add_transform(ref, xmlsec.Transform.ENVELOPED)
    xmlsec.template.add_transform(ref, xmlsec.Transform.EXCL_C14N)

    key_info = xmlsec.template.ensure_key_info(signature)
    xmlsec.template.add_key_name(key_info, key.name)

    element.append(signature)

    # Perform the actual signing.
    ctx = xmlsec.SignatureContext()
    ctx.key = key
    ctx.sign(signature)


def verify(
    element,
    key: typing.Optional[xmlsec.Key],
    id_elements: typing.List[etree._Element] = [],
) -> None:
    for id_elm in id_elements:
        xmlsec.tree.add_ids(id_elm, ["ID"])

    # We don't use the xmlsec.tree.find_node() call here since we first want to
    # look for signatures which are a direct child of the given element and
    # only after that search through the subchilds. Otherwise the incorrect
    # part gets verified. The latter occurs in xml documents with nested
    # signatures (e.g. the AcquirerStatesRes message)
    elements = element.xpath(
        "xmldsig:Signature",
        namespaces={"xmldsig": "http://www.w3.org/2000/09/xmldsig#"},
    )
    if len(elements) > 1:
        raise VerificationError(
            "Expected exactly only Signature element, found %d" % len(elements)
        )
    elif len(elements) < 1:
        signature = xmlsec.tree.find_node(element, xmlsec.constants.NodeSignature)
    else:
        signature = elements[0]

    if not key:
        key = read_x509_key(signature)

    ctx = xmlsec.SignatureContext()
    ctx.key = key

    try:
        ctx.verify(signature)
    except xmlsec.VerificationError as exc:
        raise VerificationError("Failed to verify XML message") from exc
    except xmlsec.InternalError as exc:
        raise VerificationError("Failed to verify XML message")


def encrypt(
    element, key: xmlsec.Key, recipient: typing.Optional[str] = None
) -> etree._Element:
    manager = xmlsec.KeysManager()
    manager.add_key(key)

    enc_data = xmlsec.template.encrypted_data_create(
        element,
        xmlsec.constants.TransformAes256Cbc,
        type=xmlsec.constants.TypeEncElement,
        ns="xenc",
    )
    key_info = xmlsec.template.encrypted_data_ensure_key_info(enc_data, ns="dsig")

    enc_key = xmlsec.template.add_encrypted_key(
        node=key_info, method=xmlsec.Transform.RSA_OAEP, recipient=recipient
    )

    xmlsec.template.encrypted_data_ensure_cipher_value(enc_key)
    xmlsec.template.encrypted_data_ensure_cipher_value(enc_data)

    enc_ctx = xmlsec.EncryptionContext(manager)
    enc_ctx.key = xmlsec.Key.generate(
        xmlsec.constants.KeyDataAes, 256, xmlsec.constants.KeyDataTypeSession
    )
    return enc_ctx.encrypt_xml(enc_data, element)


def decrypt(element, key: xmlsec.Key) -> etree._Element:
    encrypted_elm = xmlsec.tree.find_child(
        element, "EncryptedData", xmlsec.constants.EncNs
    )

    manager = xmlsec.KeysManager()
    manager.add_key(key)

    ctx = xmlsec.EncryptionContext(manager)
    decrypted = ctx.decrypt(encrypted_elm)
    return decrypted


def read_x509_key(signature: etree._Element) -> typing.Optional[xmlsec.Key]:
    elements = signature.xpath(
        "ds:KeyInfo/ds:X509Data/ds:X509Certificate",
        namespaces={"ds": "http://www.w3.org/2000/09/xmldsig#"},
    )
    if len(elements) == 0:
        return None

    certificate_data = base64.b64decode(elements[0].text)
    return xmlsec.Key.from_memory(certificate_data, xmlsec.KeyFormat.CERT_DER)
