from napalm import get_network_driver

driver = get_network_driver('ios')

# optional_args = {'secret': 'cisco'}
ios = driver('10.10.10.1', 'gozzki', 'cisco',)

ios.open()

ios.load_merge_candidate('acl.txt')


diff = ios.compare_config()
#print(diff)

if len(diff):
    answer = input('Commit changes? y/n ')
    if answer == 'y':
        print('Committing changes...')
        ios.commit_config()
        print('Done')
    else:
        print('No changes made.')
        ios.discard_config()


# print('Rolling back...')
# config = ios.get_config()
# print(config['running'])
# print('Done')


ios.close()