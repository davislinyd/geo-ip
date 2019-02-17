About:

This script is used to query bunch IPs for geo-location information in one time.

Note:
1. You should run this script on Python3 and pre-install some library it needs, like **prettytable**, **json5**.
2. Please keep all the IPs in the file line by line, otherwise, it could not parse them exactly.
3. The script will eliminate duplicated IPs which you put in the IP list file.

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
