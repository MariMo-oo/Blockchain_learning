import hashlib


def sha256d(data: bytes) -> bytes:
    """
    Perform double SHA-256 hashing.
    """
    return hashlib.sha256(hashlib.sha256(data).digest()).digest()


def build_merkle_root(tx_list):
    """
    Compute the Merkle Root from a list of transaction IDs (hex strings).
    Returns the Merkle Root as a hexadecimal string.
    """

    if not tx_list:
        return None
    current_level = [
        sha256d(bytes.fromhex(tx))
        for tx in tx_list
    ]
    
    while len(current_level) > 1:

        if len(current_level) % 2 == 1:
            current_level.append(current_level[-1])

        next_level = []

        for i in range(0, len(current_level), 2):
            parent = sha256d(current_level[i] + current_level[i + 1])
            next_level.append(parent)

        current_level = next_level

    return current_level[0].hex()

if __name__ == "__main__":
    test_input = ["11", "22", "33", "44", "55"]
    root = build_merkle_root(test_input)
    print("Merkle Root:", root)
