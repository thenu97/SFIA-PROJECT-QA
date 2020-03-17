import urllib3

def test_home():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/')
    assert 200 == r.status

def test_about():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/about')
    assert 200 == r.status

def test_create():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/create')
    assert 200 == r.status

def test_addtag():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/tag')
    assert 200 == r.status

def test_view():
    http = urllib3.PoolManager()
    r = http.request('GET', 'http://35.230.137.31:5000/blog/2')
    assert 200 == r.status
