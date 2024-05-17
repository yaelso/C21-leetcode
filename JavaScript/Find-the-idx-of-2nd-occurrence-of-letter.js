function secondSymbol(s, symbol) {
  const indices = [...s].reduce((acc, element, index) => {
    if (element === symbol) acc.push(index);
    return acc;
  }, []);

  return indices[1] ?? -1;
}

// second_symbol('Hello world!!!','l') --> 3
// second_symbol('Hello world!!!', 'A') --> -1
