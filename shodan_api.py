from shodan import Shodan
from shodan.cli.helpers import get_api_key

api = Shodan(get_api_key())

limit = 500
counter = 0
for banner in api.search_cursor('35.205.134.49'):
    # Perform some custom manipulations or stream the results to a database
    # For this example, I'll just print out the "data" property
    print(banner['data'])

    # Keep track of how many results have been downloaded so we don't use up all our query credits
    counter += 1
    if counter >= limit:
        break
