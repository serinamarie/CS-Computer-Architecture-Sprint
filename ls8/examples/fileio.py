import sys

if (len(sys.argv)) != 2:
        print('remember to pass the second file name')
        print('usage: python fileio.py <second_filename.py>')
        sys.exit()

try: 
    with open(sys.argv[1]) as f:
        for line in f:
            possible_binary = line[:line.find('#')]
            # if no comment on line
            if possible_binary == '':
                continue # passes rest of loop
            denary_int = int(possible_binary, 2)
            print(denary_int)
            
except FileNotFoundError:
    print(f'Error from {sys.argv[0]}: {sys.argv[1]} not found ')
    sys.exit()