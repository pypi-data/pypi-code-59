import sys
import argparse
from .asos import main

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='A Scheduler of Stuff.')
	parser.add_argument("--storage-plugin", "-s", dest="storage_plugin", required=True, type=str, help="Storage plugin name")
	parser.add_argument("--instance-uuid", "-u", dest="instance_uuid", required=True, type=str, help="Current instance name")
	args = parser.parse_args(sys.argv[1:])
	main(storage_plugin=args.storage_plugin, instance_uuid=instance_uuid)
