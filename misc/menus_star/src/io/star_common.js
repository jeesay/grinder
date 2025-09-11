/*
 * mmCIF Parser
 * Jean-Christophe Taveau
 * 2021/11/15
 */

  // Constants for state
export const CIF = {
    NONE: 0,
    SEPARATOR: 1,
    COMMENT: 2,
    DATABLOCK: 3,
    TOKEN: 4,
    TABLE: 5,
    HEADER: 6,
    STRING: 7,
    WORD: 8,
    NUMBER: 9,
    EOL: 10
  };
  Object.freeze(CIF);
  
