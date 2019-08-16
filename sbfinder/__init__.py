import main
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument("-key", "--key", dest="apiKey",
                    help="Input Yelp fusion api key")


args = parser.parse_args()

if args.apiKey == None:
	apiKey = raw_input("Yelp API Key: ")
else:
	apiKey = args.apiKey

main.set_api_key(apiKey)

print """
** SMALL BUSINESS FINDER 2.0 **
\nThis script uses the Yelp fusion API to find
nearby small businesses with no online presence\n\n
"""
threads = raw_input("Number of threads [Default 20]: ")
search_term = raw_input("Search Term: ")
location = raw_input("City: ")
state = raw_input("State: ")
saveAs = raw_input("CSV Filename [leave blank for stdout only]: ")
print("\n\n")
if len(saveAs) == 0:
	main.search(search_term, int(threads), location + " " + state)
else:
	main.search(search_term, int(threads), location + " " + state, saveAs)