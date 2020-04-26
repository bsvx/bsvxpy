import bsvxpy

reader = bsvxpy.core.Reader("custom_sample.bsvx")
l = reader.read()
for i in l:
    print(i._hex_data)