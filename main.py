#import myfun as mf
from myfun import StructPrg

prg = StructPrg()
print("prg.folder_project =", prg.folder_project)
print('prg.struct =', prg.struct_prg)
prg.creat_project("sample")
print(prg.struct_prg)
prg.creat_file("sample", "example")
prg.creat_file("sample", "example001")
print(prg.struct_prg)