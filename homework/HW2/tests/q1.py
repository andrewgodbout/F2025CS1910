OK_FORMAT = True

test = {   'name': 'q1',
    'points': 0,
    'suites': [   {   'cases': [   {'code': ">>> q1_data[0].strip().replace(' ', '') == '(0,0)'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> q1_data[1].strip()[0] == 'E'\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> int(q1_data[2].strip()) == 0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> q1_data[3].strip() == 'initial_heading'\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
