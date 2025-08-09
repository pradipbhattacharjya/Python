names = ['john', 'maria', '', 'Kumar']
for name in names:
    if name == '':
        print("Empty value detected!")
        break
    print(f'Name = {name}')