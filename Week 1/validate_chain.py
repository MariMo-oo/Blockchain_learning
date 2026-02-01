import csv
from generate_chain import sha256_hash

def validate_blockchain(filename):
    
    with open(filename, "r") as file:
        reader = list(csv.DictReader(file))

        for i in range(len(reader)):
            block = reader[i]

            if i == 0 and int(block["block_height"]) != 0:
                print(f"Genesis block height not equal to zero")
                return
            
            if int(block["block_height"]) != i:
                print(f"Invalid block at {i}, block height not previous block height + 1")
                return

            if i>0:
                prev = reader[i-1]

                if int(block["timestamp"]) <= int(prev["timestamp"]):
                    print(f"Timestamp error at block {i}, timestamp not strictly increasing")
                    return
                header_string = (
                    prev["parent_hash"] + prev["timestamp"] + prev["nonce"]
                )

                prev_block_hash = sha256_hash(header_string)

                if block["parent_hash"] != prev_block_hash:
                    print(f"Invalid block at height {i}, hash mismatch")
                    return

    print("Blockchain is valid")
        

if __name__ == "__main__":
    filename = "blockchain.csv"
    validate_blockchain(filename)
