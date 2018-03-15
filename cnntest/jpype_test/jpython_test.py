#!/usr/bin/env python

import jpype

jvmPath = jpype.getDefaultJVMPath()
print(jvmPath)
jvmPath = r'D:\jre-8u161-windows-x64\jre1.8.0_161\bin\server\jvm.dll'
# print(jvmPath)
jpype.startJVM(jvmPath)
jpype.java.lang.System.out.println("hello world!")
jpype.shutdownJVM()