import time
import hashlib
import random
import csv
import matplotlib.pyplot as plt

def sha256_hash(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()

def mine_block(parent_hash, k, measure_time=False):
    timestamp = int(time.time())
    nonce = 0
    target = "0" * k

    start_time = time.time()

    while True:
        header_string = parent_hash + str(timestamp) + str(nonce)
        block_hash = sha256_hash(header_string)
        if block_hash.startswith(target):
            end_time = time.time()

            if measure_time:
                return block_hash, end_time - start_time
            else:
                return block_hash, timestamp, nonce

        nonce += 1
        # nonce = random.randint(0, 2**32 - 1) # Just to experiment 

# Not part of the assignemnt
def run_difficulty_parameter_experiment(): 
    difficulties = [1, 2, 3, 4, 5]
    avg_times = []

    for k in difficulties:
        parent_hash = "0" * 64
        total_time = 0

        for _ in range(5):
            parent_hash, time_taken = mine_block(parent_hash, k, measure_time=True)
            total_time += time_taken

        avg_times.append(total_time / 5)

    return difficulties, avg_times

# Not part of the assignemnt
def plot_graph(difficulties, avg_times):
    plt.figure()
    plt.plot(difficulties, avg_times, marker='o')
    plt.xlabel("Difficulty Level (k)")
    plt.ylabel("Average Time to Mine (seconds)")
    plt.title("Proof-of-Work Difficulty vs Mining Time")
    plt.grid(True)
    plt.show()

def generate_blockchain(num_blocks, filename, k):

    with open(filename, "w", newline="") as file:
        
        writer = csv.writer(file)
        writer.writerow(["block_height", "parent_hash", "timestamp", "nonce"])
        parent_hash = "0" * 64

        for height in range(num_blocks):
            block_hash, timestamp, nonce = mine_block(parent_hash, k)

            writer.writerow([height, parent_hash, timestamp, nonce])
            parent_hash = block_hash

            time.sleep(1) # to show increasing timestamp



if __name__ == "__main__":
    NUM_BLOCKS = 10
    k = int(input("Enter a positive integer for k(difficulty parameter): "))
    filename = "blockchain.csv"

    run_experiment = input("""Do you want to run the experiment with incrementing k in range[1...5]? Enter Y/N: """).upper()
    
    if k<=0:
        print("Enter a value greater than zero!!!")
        exit()
    
    if run_experiment not in ("Y","N"):
        print("Please choose either Y or N!!!")
        exit()

    print("Generating blockchain.csv file...")
    blockchain = generate_blockchain(NUM_BLOCKS,filename,k)
    print("blockchain.csv file generated")
    print("Please wait graph is being plotted...")

    if run_experiment == "Y":
        difficulties, avg_times = run_difficulty_parameter_experiment()
        plot_graph(difficulties, avg_times)
        print("Done!")
