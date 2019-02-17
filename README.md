How to:
```
localhost$ python3 geo-ip.py ips.txt
+-------------+---------------+-----------------+
| CountryCode | Country       | IP              |
+-------------+---------------+-----------------+
| AU          | Australia     | 1.1.1.1         |
| TW          | Taiwan        | 61.31.1.1       |
| TW          | Taiwan        | 101.101.101.101 |
| TW          | Taiwan        | 168.95.1.1      |
| US          | United States | 8.8.8.8         |
| US          | United States | 8.8.4.4         |
+-------------+---------------+-----------------+
>>> This script will eliminate all duplicated IP from the source file.
```
