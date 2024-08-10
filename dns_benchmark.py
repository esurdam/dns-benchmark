#!/usr/bin/env python3

import dns.resolver
import time
import sys

def benchmark_dns(servers, domain, num_queries=10):
    results = {}
    
    for server in servers:
        resolver = dns.resolver.Resolver(configure=False)
        resolver.nameservers = [server]
        
        query_times = []
        for _ in range(num_queries):
            start_time = time.time()
            try:
                resolver.resolve(domain, 'A')
                end_time = time.time()
                query_times.append(end_time - start_time)
            except dns.exception.DNSException:
                query_times.append(None)
        
        results[server] = query_times
    
    return results

def print_results(results):
    print("\nDNS Benchmark Results:")
    print("----------------------")
    for server, times in results.items():
        valid_times = [t for t in times if t is not None]
        if valid_times:
            avg_time = sum(valid_times) / len(valid_times)
            print(f"{server}: Avg: {avg_time:.4f}s, Min: {min(valid_times):.4f}s, Max: {max(valid_times):.4f}s")
        else:
            print(f"{server}: All queries failed")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python3 dns_benchmark.py <domain> <dns_server1> [dns_server2] ...")
        sys.exit(1)

    domain = sys.argv[1]
    dns_servers = sys.argv[2:]

    results = benchmark_dns(dns_servers, domain)
    print_results(results)