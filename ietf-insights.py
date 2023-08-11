import argparse
import requests
import threading
import time
import itertools
import sys

# Create the parser
parser = argparse.ArgumentParser(description='Process IETF data.',
                                 formatter_class=argparse.RawTextHelpFormatter)

# Add the arguments
parser.add_argument('-m', '--meeting', type=str,
                    help='The specific meeting to process. Required when using -s/--stats, -n/--name, -c/--company, or -g/--group.\n'
                         'Example: python3 ietf-insights.py -m "ietf117"')
parser.add_argument('-n', '--name', type=str,
                    help='The specific name to filter on. Requires -m/--meeting.\n'
                         'Example: python3 ietf-insights.py -n "John Doe" -m "ietf117"')
parser.add_argument('-c', '--company', type=str,
                    help='The specific company to filter on. Requires -m/--meeting.\n'
                         'Example: python3 ietf-insights.py -c "ericsson" -m "ietf117"')
parser.add_argument('-g', '--group', type=str,
                    help='The specific group to filter on. Requires -m/--meeting.\n'
                         'Example: python3 ietf-insights.py -g "core" -m "ietf117"\n'
                         'Example: python3 ietf-insights.py -c "itron" -m "ietf117" -g "core"')
parser.add_argument('-s', '--stats', action='store_true',
                    help='Display statistics. Requires -m/--meeting.\n'
                         'Example: python3 ietf-insights.py -s -m "ietf117"')
parser.add_argument('-H', '--historical-stats', action='store_true',
                    help='Display historical statistics. Can be used alone or with -n/--name or -g/--group.\n'
                         'Example: python3 ietf-insights.py -H')
parser.add_argument('--country', type=str,
                    help='The specific country to filter on. Requires -m/--meeting.\n'
                         'Example: python3 ietf-insights.py --country "ES" -m "ietf117"')
parser.add_argument('--not-attending', type=str,
                    help='The company to find non-attending groups for. Requires -m/--meeting.\n'
                         'Example: python3 ietf-insights.py --not-attending "itron" -m "ietf117"')
parser.add_argument('--debug', action='store_true', help='Use the debug server. Must lunch the server first.')
args = parser.parse_args()

# Convert the arguments to a dictionary and remove None values
params = vars(args)
params = {k: v for k, v in params.items() if v is not None}

class RequestThread(threading.Thread):
    def __init__(self, params, debug):
        threading.Thread.__init__(self)
        self.params = params
        self.debug = debug
        self.response = None

    def run(self):
        url = 'http://127.0.0.1:80/query' if self.debug else 'http://ietf-participation-insights.onrender.com:80/query'
        try:
            self.response = requests.get(url, params=self.params, timeout=25)
        except requests.exceptions.Timeout:
            print("\nThe request timed out. It is possible that render is currently deploying this app. Try again in a minute.")
        except requests.exceptions.RequestException as e:
            # handle other types of exceptions
            print(f"\nAn error occurred: {e}")

# Start the request in a separate thread
request_thread = RequestThread(params, args.debug)
request_thread.start()

spinner = itertools.cycle(['-', '\\', '|', '/', '+', 'x', '*', '.'])

# Wait for the request to complete, and print a message if it takes too long
start_time = time.time()
while request_thread.is_alive():
    if time.time() - start_time > 2:  # If more than 2 seconds have passed
        sys.stdout.write(next(spinner))  # write the next character
        sys.stdout.flush()  # flush stdout buffer (actual character display)
        time.sleep(0.1)
        sys.stdout.write('\b')  # erase the last written character

# Print the response text
if request_thread.response is not None:
    print(request_thread.response.text)
else:
    print("No response received from the server.")