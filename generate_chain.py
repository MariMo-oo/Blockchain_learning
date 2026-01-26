import time
import hashlib
import random

def sha256(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


def create_block(parent_hash):
    timestamp = int(time.time())
    nonce = random.randint(0, 2**32 - 1)

    return parent_hash, timestamp, nonce


def generate_blockchain(num_blocks):
    #Todo write logic to store as csv
    blockchain = []

    parent_hash = "0" * 64
    for i in range(num_blocks):
        parent_hash, timestamp, nonce = create_block(parent_hash)
        
        header_string = parent_hash + str(timestamp) + str(nonce)

        block_hash = sha256(header_string)

        block = {
            "block_num": i+1,
            "parent_hash": parent_hash,
            "timestamp":timestamp,
            "nonce": nonce,
            "hash": block_hash
        }

        blockchain.append(block)

        parent_hash = block_hash

    return blockchain

if __name__ == "__main__":
    NUM_BLOCKS = 10  # minimum required

    blockchain = generate_blockchain(NUM_BLOCKS)

    for block in blockchain:
        print(f"Block {block['block_num']}")
        print(f"Parent Hash : {block['parent_hash']}")
        print(f"Timestamp   : {block['timestamp']}")
        print(f"Nonce       : {block['nonce']}")
        print(f"Hash        : {block['hash']}")

