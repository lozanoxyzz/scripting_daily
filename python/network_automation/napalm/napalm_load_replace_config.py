from napalm import get_network_driver

driver = get_network_driver('ios')

optional_args = {'secret': 'cisco'}
ios = driver('10.10.10.1', 'gozzki', 'cisco', optional_args=optional_args)

ios.open()

ios.load_replace_candidate(filename='config.txt')

diff = ios.compare_config()

if len(diff):
    print(diff)
    print("Committing changes...")
    ios.commit_config()
    print('Done')
else:
    print('No changes found.')
    ios.discard_config()

ios.close()