# YASS, Yet Another Subdomainer Software
# Copyright 2015 Francesco Marano (@mrnfrancesco) and individual contributors.
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

import inspect

from yass.models import PluginMeta, PluginBase
import yass.plugins


def iter_plugins(predicate=None):
    base_predicate = lambda cls: isinstance(cls, PluginMeta) and cls != PluginBase
    _predicate = base_predicate

    if predicate is not None and hasattr(predicate, '__call__'):
        _predicate = lambda cls: base_predicate(cls) and predicate(cls)

    plugins = inspect.getmembers(yass.plugins, _predicate)
    return [cls for name, cls in plugins]
