'''malnet db test'''


def genTestSample(num=5, base=0):
    data = []
    for i in range(base, base + num):
        tmp = {}
        tmp['md5'] = f'md5-{i}'
        tmp['sha1'] = f'sha1-{i}'
        tmp['sha256'] = f'sha256-{i}'
        tmp['name'] = f'sample-{i}'
        tmp['collectDomain'] = 'test.com'
        tmp['fileType'] = 'win32'
        tmp['fileSize'] = '4M'
        tmp['bucket'] = 'a/b/c'
        tmp['priority'] = i % 5
        data.append(tmp)

    if num == 1:
        return data[0]
    else:
        return data


def genTestTask(num=2, base=0):
    data = []
    for i in range(base, base + num):
        data.append({'taskName': f'task-{i}'})

    return data