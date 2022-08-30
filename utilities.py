import copy

def simplify_laphDiagrams(laphDiagrams):
    for d in laphDiagrams:
        d.create_baryon_blocks()
        d.combine_indices()

    # the below has no guarantee to be NC agnostic nor work for any multi meson&baryon operator
    for d in laphDiagrams:
        d.create_baryon_source()


def find_all_baryon_tensors(laphDiagrams):
    allBaryonTensors = {}
    idx=0
    for d in laphDiagrams:
        for tensor in d.commuting:
            if tensor.id() not in allBaryonTensors:
                allBaryonTensors[tensor.id()]=idx
                idx+=1
    return allBaryonTensors

