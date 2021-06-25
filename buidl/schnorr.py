from buidl.helper import sha256


def tagged_hash(tag, msg):
    tag_hash = sha256(tag)
    return sha256(tag_hash + tag_hash + msg)


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))
