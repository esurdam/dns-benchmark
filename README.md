# DNS Benchmark Tool

This is a simple command-line DNS benchmark tool written in Python. It allows you to measure and compare the performance of different DNS servers for a given domain.

## Features

- Benchmark multiple DNS servers simultaneously
- Measure average, minimum, and maximum query times
- Easy to use command-line interface
- Works on macOS (and other Unix-like systems)

## Requirements

- Python 3.6+
- dnspython library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/esurdam/dns-benchmark.git
   cd dns-benchmark
   ```

2. Install the required Python library:
   ```
   pip3 install dnspython
   ```

3. Make the script executable:
   ```
   chmod +x dns_benchmark.py
   ```

## Usage

Run the script from the command line with the following syntax:

```
./dns_benchmark.py <domain> <dns_server1> [dns_server2] ...
```

For example:

```
./dns_benchmark.py example.com 8.8.8.8 1.1.1.1 9.9.9.9
```

This will benchmark the DNS servers 8.8.8.8 (Google), 1.1.1.1 (Cloudflare), and 9.9.9.9 (Quad9) for the domain example.com.

## Output

The script will output the average, minimum, and maximum query times for each DNS server. For example:

```
DNS Benchmark Results:
----------------------
8.8.8.8: Avg: 0.0534s, Min: 0.0412s, Max: 0.0701s
1.1.1.1: Avg: 0.0234s, Min: 0.0189s, Max: 0.0312s
9.9.9.9: Avg: 0.0634s, Min: 0.0534s, Max: 0.0823s
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).