# processing an API response

# import requests

# # make an API call and check the response
# url = 'https://api.github.com/search/repositories'
# url += '?q=language:python+sort:stars+stars:>10000'

# headers = {'Accept': 'application/vnd.github.v3+json'}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# # convert the response object to a dictionary
# response_dict = r.json()

# # process results
# print(response_dict.keys())

# -------------------------------

# working with the response dictionary

# import requests

# # make an API call and check the response
# url = 'https://api.github.com/search/repositories'
# url += '?q=language:python+sort:stars+stars:>10000'

# headers = {'Accept': 'application/vnd.github.v3+json'}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# # convert the response object to a dictionary
# response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")
# print(f"Complete results: {not response_dict['incomplete_results']}")

# # Explore information about the repositories.
# repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")

# # Examine the first repository.
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)