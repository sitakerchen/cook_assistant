import dataDefine


def M(data):
    """

    :param data: dataDefine.Food()
    :return:
    """
    while (True):
        a = dataDefine.Food()
        print('quit : 1 \nsearch : 2')
        option = eval(input('input a operate number\n'))
        if option == 1:
            break
        elif option == 2:
            m = input('materials1;m2;m3...')
            materials = m.split(';')
            for food in data:
                ok = True
                for item in materials:
                    if item not in food.material:
                        ok = False
                        break
                if ok:
                    print(food.name+' '+food.web)
                else:
                    pass

            print('search end\n')
        else:
            print('opc error\n')