class Link:

    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(
            rest, Link), "Link does not follow proper structure"
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'
    
def count_targets(link, targets):
    return count_targets_iterative(link,targets)

def count_targets_iterative(link, targets):
    l = link
    out_dict = {}
    while l.rest != Link.empty:
        if l.first in targets:
            if l.first in out_dict.keys():
                out_dict[l.first] += 1
            else:
                out_dict[l.first] = 1
        l = l.rest
    if l.first in targets:
        if l.first in out_dict.keys():
            out_dict[l.first] += 1
        else:
            out_dict[l.first] = 1
    return out_dict

def count_targets_recursive(link, targets):
    out_dict = {}
    def count_helper(link, targets):
        nonlocal out_dict
        if isinstance(link, tuple):
            return
        if link.rest == Link.empty:
            if link.first in targets:
                if link.first in out_dict.keys():
                    out_dict[link.first] += 1
                else:
                    out_dict[link.first] = 1
                return
            else:
                return
        if link.first in targets:
            if link.first in out_dict.keys():
                out_dict[link.first] += 1
            else:
                out_dict[link.first] = 1
        return count_helper(link.rest, targets)
    
    count_helper(link, targets)
    return out_dict

def remove_targets(link, targets):
    if isinstance(link, tuple):
        return Link.empty
    if isinstance(link.rest, Link.empty):
        if link.first not in targets:
            return link.first
        else:
            return Link.empty
    
    if link.first not in targets:
        return Link(link.first, remove_targets(link.rest, targets))
    else:
        return remove_targets(link.rest, targets)

link = Link('c', Link(2, Link(2, Link('a', Link('b', Link(4, Link('t', Link(2, Link('s', Link(4))))))))))
print(count_targets_recursive(link, [2, 4, 'b']))