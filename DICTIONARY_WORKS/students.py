students=[
    {"id":1,"name":"jhon","skills":["c","c++"],"exp":2,"qualification":"mca"},
    {"id":1,"name":"jain","skills":["python","js"],"exp":0,"qualification":"btec"},
    {"id":1,"name":"vijin","skills":["c","java","python"],"exp":4,"qualification":"mca"},
    {"id":1,"name":"tinu","skills":["r","java"],"exp":3,"qualification":"mtech"},
    {"id":1,"name":"roy","skills":["python","css","js"],"exp":0,"qualification":"bca"},
    {"id":1,"name":"vijil","skills":["js","r","css"],"exp":1,"qualification":"mtech"},
    {"id":1,"name":"ravi","skills":["java","python"],"exp":3,"qualification":"btec"},
    {"id":1,"name":"tom","skills":["java","css","r","sql"],"exp":4,"qualification":"bca"},
    {"id":1,"name":"ryan","skills":["c","css","python"],"exp":0,"qualification":"mca"},
]
#total number of students
# print("TOTAL NUMBER OF STUDENTS IS ",len(students))
# for st in students:
    # print(st.get("name"))
# all_student_name=[st.get("name") for st in students]
# print(all_student_name)
# student_name_exp_grt_one=[st.get("name") for st in students if st.get("exp")>1]
# print(student_name_exp_grt_one)
# for st in students:
#     if "java" in st.get("skills") and "python" in st.get("skills"):
#         print(st.get("name"))
# mca_students=[st.get("name") for st in students if st.get("qualification")=="mca"]
# print(mca_students)
# most_exp_student=max(students,key=lambda st:st.get("exp"))
# print(most_exp_student)
# highest_exp=most_exp_student.get("exp")
# exp_student=[st.get("name") for st in students if st.get("exp")==highest_exp]
# print(exp_student)
# sted=[st.get("name") for st in students if len(st.get("skills"))>2]
# print(sted)
# for st in students:
#     if st.get("name").startswith("j"):
#         print(st.get("name"))
sc={}
for st in students:
    skills=st.get("skills")
    for sk in skills:
        if sk in sc:
            sc[sk]+=1
        else:
            sc[sk]=1
print(sc)