'''
Author: Palermo Penano
Date: 2018/12/29
'''

import time
import argparse

import speedtest
import pandas as pd

def parse_args():

    parser = argparse.ArgumentParser(description="Test network connection")

    parser.add_argument('-n', '--n_test', required=True,
                        help='Number of times to run test')

    parser.add_argument('-cn', '--cafe_name', required=True,
                    help='Cafe name')

    parser.add_argument('-ca', '--cafe_addr', required=True,
                        help='Cafe address')

    return vars(parser.parse_args())


if __name__ == '__main__':

	args = parse_args()

	n = int(args['n_test'])
	cafe_name = args['cafe_name']
	cafe_address = args['cafe_addr']

	servers = []
	results = []

	for i in range(n):
		print(f"Test number {i}...")
		s = speedtest.Speedtest()

		start = time.time()
		s.get_servers(servers)
		s.get_best_server()
		s.download()
		s.upload()
		test_result = s.results.dict()
		elapsed_time = time.time() - start

		test_result['test_time'] = elapsed_time
		results.append(test_result)

	df = pd.DataFrame(results)
	data_cols =['download', 'upload', 'ping', 'test_time']

	# compute mean
	mean = df[data_cols].mean().round(2)

	# get time of first test run and make that the time of the test
	timestamp = df['timestamp'].sort_values().iloc[0]
	timestamp = timestamp.split('.', 1)[0].replace('T', '-')

	print(f"\"{cafe_name}\", \"{cafe_address}\", {timestamp},",
		  f"{mean['download'] / 1000: 0.2f}, {mean['upload'] / 1000: 0.2f},",
		  f"{mean['ping']}, {mean['test_time']}, {n}")

