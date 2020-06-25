#Import cool stuffs under Python (OS,HARDWARE, OR PYTHON ITSELF)
from platform import platform, machine, processor, system, version,\
python_implementation, python_version_tuple

print(platform(1))
print(platform(1, 1))
print(machine())
print(processor())
print(system())
print(version())
print(python_implementation())
print(python_version_tuple())
#python version tuple go as following(major version, minor part, patch level)

# https://docs.python.org/3/py-modindex.html Official modules.