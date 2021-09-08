from re import sub
from django.shortcuts import render


# Create your views here.


def calc(request, *args, **kwargs):
    if not len(kwargs):
        return render(request, 'calc.html')

    elif len(kwargs) <= 2:
        kwargs['second_num'] = kwargs['first_num']

        if not 'operation' in kwargs:
            kwargs['operation'] = '+'

        else:
            kwargs['operation'] = sub('[^-+/*%]', '', kwargs['operation'])
            if kwargs['operation'] == '':
                kwargs['operation'] = '+'
            else:
                kwargs['operation'] = list(kwargs['operation'])[0]
    print(kwargs)
    if len(kwargs['operation']) > 2:
        kwargs['operation'] = kwargs['operation'][:2]

    if kwargs['operation'] == '%':
        kwargs['operation'] = '/'
    elif kwargs['operation'] == '^':
        kwargs['operation'] = '**'

    kwargs['crutch'] = '='
    try:
        kwargs['finish_num'] = eval(f"{kwargs['first_num']}{kwargs['operation']}{kwargs['second_num']}")

    except ZeroDivisionError:
        kwargs['finish_num'] = 'Dividing by Zero'
    except:
        kwargs['finish_num'] = 'Wrong operator'

    return render(request, 'calc.html', kwargs)
