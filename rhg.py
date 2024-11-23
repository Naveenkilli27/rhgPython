import math
import random
from collections import Counter

def generate_traffic(total_sources, total_packets, attack=False):
    traffic = []
    if attack:
        
        attack_sources = random.sample(range(1, total_sources + 1), k=3)  
        for _ in range(total_packets):
            traffic.append(random.choice(attack_sources))
    else:
        
        for _ in range(total_packets):
            traffic.append(random.randint(1, total_sources))
    return traffic

def calculate_entropy(traffic):
    packet_count = Counter(traffic)
    total_packets = len(traffic)
    entropy = -sum((count / total_packets) * math.log2(count / total_packets)
                   for count in packet_count.values())
    return entropy


def classify_traffic(entropy, threshold):
    return "DDoS Attack" if entropy < threshold else "Normal Traffic"


total_sources = 100
total_packets = 1000
entropy_threshold = 4.0  


normal_traffic = generate_traffic(total_sources, total_packets, attack=False)
attack_traffic = generate_traffic(total_sources, total_packets, attack=True)


normal_entropy = calculate_entropy(normal_traffic)
attack_entropy = calculate_entropy(attack_traffic)


print("Normal Traffic Entropy:", normal_entropy)
print("Classification:", classify_traffic(normal_entropy, entropy_threshold))

print("\nAttack Traffic Entropy:", attack_entropy)
print("Classification:", classify_traffic(attack_entropy, entropy_threshold))
