from scapy.all import sniff, IP , TCP , UDP
import time
import pandas

def extract_features(packet):
    if IP in packet:
        return {
            'size': len(packet),
            'protocol': packet.proto ,
            'time': time.time()
        }
    return None




def start_sniffing(packet_count = 10):
    print(f'Starting sniffing for {packet_count} packets.')
    packets = sniff(count=packet_count)
    feature_list = []
    for packet in packets:
        data = extract_features(packet)
        if data:
            feature_list.append(data)
    return pandas.DataFrame(feature_list)


if __name__ == '__main__':
    df = start_sniffing(5)
    print(df)