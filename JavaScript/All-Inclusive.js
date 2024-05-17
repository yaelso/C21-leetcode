const containAllRots = (strng, arr) =>
  [...strng]
    .map((_, idx) => strng.slice(idx) + strng.slice(0, idx))
    .every((rot) => arr.includes(rot));

// ("bsjq", ["bsjq", "qbsj", "sjqb", "twZNsslC", "jqbs"]) -> true)
// ("Ajylvpy", ["Ajylvpy", "ylvpyAj", "jylvpyA", "lvpyAjy", "pyAjylv", "vpyAjyl", "ipywee"]) -> false)
