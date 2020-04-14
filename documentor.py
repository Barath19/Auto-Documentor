import os
import sys
from graphviz import Digraph


file = sys.argv[1]

dot = Digraph(comment='Pixplot')
functions = []
func_argu = {}
with open(file, 'r') as f:
    full_code = f.read()

with open(file, 'r') as f:
    code = f.readlines()

[functions.append(function_name.split(' ')[1].split('(')[0]) for function_name in code if function_name[:3]=='def' ]

funct_id ={}
for idx, func in enumerate(functions):
    funct_id[func] = str(idx)

print("Total Functions: ",len(functions))
func_sub_code = []
split_code = full_code.split("def ")
[func_sub_code.append(x) for x in split_code[1:]]

def Sort_Tuple(tup):
    return(sorted(tup, key = lambda x: x[2]))
    return tup

func_name_code = {}
for idx,func in enumerate(functions):
    func_name_code[func] = func_sub_code[idx]

#print(re.search("^'''.*'''$", str(code_of)).group(0))

relation = []
relations = []
for key, value in func_name_code.items():
    print(f"Function Name: {key}")
    if "'''" in value:
        print("Decription of function: ",value.split("'''")[1])
    else:
        print("No description")

    cnt = 0
    for func_name in functions:
        if func_name == key:
            continue
        if func_name+'(' in value:
            cnt +=1

            #print(cnt," : ",func_name)
            relation.append((key, func_name, value.index(func_name)))


    relations.append(relation)
    relation = []

    print("***************************")



for idx, func in enumerate(functions):
    dot.node(str(idx), func)

print(relations)

from graphviz import Digraph

u = Digraph('unix', filename='unix.gv',
            node_attr={'color': 'lightblue2', 'style': 'filled'})
u.attr(size='100,100')

for relation in relations:
    sorted_relation = Sort_Tuple(relation)
    for idx, tup in enumerate(sorted_relation):

        from_, to_, _ = tup
        u.edge(from_, to_, label=str(idx+1))

u.view()
