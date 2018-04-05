from idl import readsav

for j in range(20):
    s = readsav('struct_arrays_byte_idl80.sav', verbose=False)
    print(j, s.y.x[0])
