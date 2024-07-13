weather = 'cloudy'

match weather:
    case 'sunny':
        print('sunny day')
    case 'rainy':
        print('rainy day')
    case _:
        print('stay inside')