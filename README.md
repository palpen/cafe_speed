# Get Wifi Speed
Short script to get network performance and print result to standard output which can then be copied and pasted into a spreadsheet.

Goal is to get network performance of all the cafes in my neighborhood to know which one I should visit more frequently.

Pasting into Google Sheets:
* https://webapps.stackexchange.com/a/100790

### Usage

```bash
python get_speed.py -n NUM_RUN_TEST -cn CAFE_NAME -ca CAFE_ADDRESS
```

### Units of measurement
	download: in bytes
	upload: in bytes
	test_time: time elapsed during iteration in seconds
	ping: in ms
	timestamp: ISO format UTC time zone

### Dependencies
* python 3.7
* pandas
* speedtest

### To do:
* Export raw data into a json file
