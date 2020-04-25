import bsvxpy

reader = bsvxpy.core.Reader("sample.bsvx")
l = reader.read()
for i in l:
    print(i._hex_data)