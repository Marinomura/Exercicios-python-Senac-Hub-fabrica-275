while True:
    try:
        a=int(input('digite uma palavra = '))
    except ValueError:
        print('digite apenas numeros')
        continue
    except:
        print('erro desconhecido')
    finally:
        print('final do algoritimo')