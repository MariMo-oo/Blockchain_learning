import csv
from generate_chain import sha256_hash

def validate_blockchain(filename):
    
    with open(filename, "r") as file:
        reader = list(csv.DictReader(file))

        for i in range(1,len(reader)):
            prev = reader[i-1]
            curr = reader[i]

            header_string = (
                prev["parent_hash"] + prev["timestamp"] + prev["nonce"]
            )

            prev_block_hash = sha256_hash(header_string)

            if curr["parent_hash"] != prev_block_hash:
                print(f"Invalid block at height {i}")
                return

    print("Blockchain is valid")
        

if __name__ == "__main__":
    filename = "blockchain.csv"
    validate_blockchain(filename)
