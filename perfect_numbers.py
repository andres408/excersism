def classify(number):
        if number > 0:    
            l=[i for i in range(number-1,0,-1) if number%i == 0]
            if sum(l) == number:
                return 'Perfect'
            if sum(l) > number:
                return 'Abundant'
            if sum(l) < number:
                return 'Deficient'

        else:
            raise ValueError('Classification is only possible for positive integers.')
if __name__=='__main__':
    number=int(input('Ingrese su numero\n'))
    print(classify(number))
