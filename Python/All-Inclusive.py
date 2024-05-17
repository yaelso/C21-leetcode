def contain_all_rots(strng, arr):
    arr_set = set(arr)

    for i in range(len(strng)):
        rotation = strng[i:] + strng[:i]
        if rotation not in arr_set:
            return False

    return True

# ("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true)
# ("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)
