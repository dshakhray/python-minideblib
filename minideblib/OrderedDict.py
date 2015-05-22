# -*- coding: UTF-8 -*-
# OrderedDict.py
#
# This class functions almost exactly like UserDict.  However, when using
# the sequence methods, it returns items in the same order in which they
# were added, instead of some random order.
#
# Copyright 2001 Adam Heath <doogie@debian.org>
#
# This file is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from UserDict import UserDict


class OrderedDict(UserDict):
    __order = []

    def __init__(self, dictionary=None):
        UserDict.__init__(self)
        self.__order = []
        if dictionary is not None and dictionary.__class__ is not None:
            self.update(dictionary)

    def __cmp__(self, dictionary):
        if isinstance(dictionary, OrderedDict):
            ret = cmp(self.__order, dictionary.__order)
            if not ret:
                ret = UserDict.__cmp__(self, dictionary)
            return ret
        else:
            return UserDict.__cmp__(self, dictionary)

    def __setitem__(self, key, value):
        if key not in self:
            self.__order.append(key)
        UserDict.__setitem__(self, key, value)

    def __delitem__(self, key):
        if key in self:
            del self.__order[self.__order.index(key)]
        UserDict.__delitem__(self, key)

    def clear(self):
        self.__order = []
        UserDict.clear(self)

    def copy(self):
        if self.__class__ is OrderedDict:
            return OrderedDict(self)
        import copy
        return copy.copy(self)

    def keys(self):
        return self.__order

    def items(self):
        return map(lambda x, self=self: (x, self.__getitem__(x)), self.__order)

    def values(self):
        return map(lambda x, self=self: self.__getitem__(x), self.__order)

    def update(self, dictionary):
        for k, v in dictionary.items():
            self.__setitem__(k, v)

# vim:ts=4:sw=4:et:
