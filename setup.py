
#
# Tencent is pleased to support the open source community by making QTA available.
# Copyright (C) 2016THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the BSD 3-Clause License (the "License"); you may not use this 
# file except in compliance with the License. You may obtain a copy of the License at
# 
# https://opensource.org/licenses/BSD-3-Clause
# 
# Unless required by applicable law or agreed to in writing, software distributed 
# under the License is distributed on an "AS IS" basis, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific language
# governing permissions and limitations under the License.
#
#
# Auto generated by process_to_open.py
#

from setuptools import setup, find_packages

if __name__ == "__main__":
    
    setup(
      version="5.0.125",
      name="qtaf",
      packages=find_packages(),
      py_modules=["__main__", "qtaf_settings"],
      package_data={'':['*.lib', '*.txt', '*.TXT', '*.exe', '*.lib'], },
      data_files=[(".", ["requirements.txt", "LICENSE.TXT"])],
      author="Tencent",
      license="Copyright(c)2010-2017 Tencent All Rights Reserved. ",
      requires=['PIL', 'ply'],   
      entry_points={'console_scripts': ['qta-manage = testbase.management:qta_manage_main'], },
      )
      
      
