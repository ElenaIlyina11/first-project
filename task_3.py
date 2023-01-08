files = {
    'cool_movie.avi': ['X'],
    'math_summary.docx': ['R', 'W'],
    'war_and_peace.txt': ['R', 'W', 'X']
}

matching_grants = {
    'read': 'R',
    'write': 'W',
    'execute': 'X'
}


def is_allowed(the_request):
    my_request = the_request.split(' ')
    if my_request[1] in files:
        if matching_grants[my_request[0]] in files[my_request[1]]:
            return 'OK'
        else:
            return 'Access denied'
    else:
        print('File not found')


check_list = ['execute cool_movie.avi',
              'write math_summary.docx',
              'read war_and_peace.txt',
              'read cool_movie.avi',
              'execute math_summary.docx',
              'read fake_file.txt']

for i in check_list:
    result = is_allowed(i)
    print('access for {} is: {}'.format(i, result))
