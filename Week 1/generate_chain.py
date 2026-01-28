import time
import hashlib
import random
import csv

def sha256_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


def create_block(parent_hash):
    timestamp = int(time.time())
    nonce = random.randint(0, 2**32 - 1)

    return parent_hash, timestamp, nonce


def generate_blockchain(num_blocks, filename):

    with open(filename, "w", newline="") as file:
        
        writer = csv.writer(file)
        writer.writerow(["block_height", "parent_hash", "timestamp", "nonce"])

        parent_hash = "0" * 64
        for height in range(num_blocks):
            parent_hash, timestamp, nonce = create_block(parent_hash)

            writer.writerow([height, parent_hash, timestamp, nonce])
            
            header_string = parent_hash + str(timestamp) + str(nonce)
            block_hash = sha256_hash(header_string)


            parent_hash = block_hash

            time.sleep(1) # to show increasing timestamp



if __name__ == "__main__":
    NUM_BLOCKS = 10
    filename = "blockchain.csv"

    blockchain = generate_blockchain(NUM_BLOCKS,filename)

    print("blockchain.csv file generated")

