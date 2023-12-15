# keyword arguments
def add_employee(**kwargs):
    print(kwargs.get("name"),kwargs.get("salary"))
add_employee(id=10,name="kirab",n_place="tvm",w_place="ekm",salary=120000)