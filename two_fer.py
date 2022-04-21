'''Solution to two Fer exercise'''
def two_fer(name):
    if name == '':
        return 'One for you, one for me'
    return f'One for {name}, one for me'

if __name__=='__main__':
    print(two_fer(name=''))
