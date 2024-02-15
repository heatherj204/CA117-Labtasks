#!/usr/bin/env python3

def swap_keys_values(d):
    new_dict = {k[1] : k[0] for k in d.items()}
    return new_dict
