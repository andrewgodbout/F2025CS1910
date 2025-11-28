from otter.test_files import test_case

OK_FORMAT = False

name = "q1"
points = 2

@test_case(points=1, hidden=False)
def t1():
    pb = {}
    ph1 = "902-555-5555"
    add_contact(pb, "andrew", ph1)
    ph2 = get_contact(pb, "andrew")
    assert ph1 == ph2

t1()
@test_case(points=1, hidden=False)
def t2():
    pb = {}
    ph1 = "902-555-5554"
    add_contact(pb, "sally", ph1)
    add_contact(pb, "george", "999-999-9999")
    save(pb, "a.txt")
    pb2 = load_contacts("a.txt")
    ph2 = get_contact(pb2,"sally")
    assert ph1 == ph2

t2()
