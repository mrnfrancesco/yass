# YASS, Yet Another Subdomainer Software
# Copyright 2015-2019 Francesco Marano (@mrnfrancesco) and individual contributors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def without_duplicates(args):
    """
    Removes duplicated items from an iterable.

    :param args: the iterable to remove duplicates from
    :type args: iterable
    :return: the same iterable without duplicated items
    :rtype: iterable
    :raise TypeError: if *args* is not iterable
    """
    if hasattr(args, '__iter__') and not isinstance(args, str):
        if args:
            return type(args)(set(args))
        else:
            return args
    else:
        raise TypeError("Expected iterable, got {args_type} insted".format(args_type=type(args)))
