new_dict = {
    'tuple': ('black', 'white', 'yellow', 'green', 'red'),
    'list': ['apple', 'banana', 'cherry', 'peach', 'lemon'],
    'dict': {'Japan': 'Tokyo', 'Italy': 'Rome', 'Germany': 'Berlin', 'France': 'Paris', 'Ireland': 'Dublin'},
    'set': {1, 2, 3, 4, 5}
}
print(new_dict['tuple'][-1])
new_dict['list'].append('grapes')
new_dict['list'].pop(2)
new_dict['dict']['i am a tuple'] = 'new'
new_dict['dict'].pop('Ireland')
new_dict['set'].add(2.5)
new_dict['set'].pop()

