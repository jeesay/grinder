import {CIF} from "./star_common.js";


/////////////////////::: P A R S E R ::://///////////////////

/**
 * Parsers
 */
const parseComment = (tok,obj) => {
  // Reset if CIF.TABLE
  if (obj._admin_.state === CIF.TABLE) {
    obj._admin_.next = [CIF.TOKEN,CIF.TABLE];
    obj._admin_.state = CIF.NONE;
    obj._admin_.current = null;
  }
}

const parseEOL = (tok,obj) => {
  console.log('parseEOL');
  // Reset 
  obj._admin_.next = [CIF.DATABLOCK,CIF.TOKEN,CIF.TABLE];
  obj._admin_.state = CIF.NONE;
  obj._admin_.current = null;
  return obj;
}

const parseSeparator = (tok,obj) => {
  // Reset
  obj._admin_.next = [CIF.STRING,CIF.NUMBER,CIF.TOKEN,CIF.WORD,CIF.EOF,CIF.EOL];
  return obj;
}


/**
 * Parse nothing - Use for skipping token(s)
 *
 * @param {Token} - `tok` a token composed of 
 * @param {Object} - `obj` the Data Structure
 * @returns {object} - The UNmodified Data Structure
 *
 * @author Jean-Christophe Taveau
 */
 const parseNothing = (tok,obj) => obj;

/**
 * Set mmCIF Category
 *
 * @param {Token} - `tok` a token composed of 
 * @param {Object} - `obj` the Data Structure
 * @returns {object} - The modified Data Structure
 *
 * @author Jean-Christophe Taveau
 */
const setCategory = (cat,attr,obj) => {
  //
  let obj_block = obj._admin_.datablock;
  // Create object if needed
  if (cat in obj_block === false) {
    obj_block[cat] = {};
  }
  if (!attr) {
    obj_block[cat] = 0;
  }
  else {
    obj_block[cat][attr] = 0;
  }

  obj._admin_.next = [CIF.NUMBER,CIF.STRING,CIF.WORD];
  obj._admin_.current = cat;
  obj._admin_.attr = attr;
  return obj;
}

/**
 * Parse mmCIF Token: parseHead or parseCat depending of context (CIF.TABLE or CIF.TOKEN)
 *
 * @param {Object} - `tok` a token composed of a type `type` and a value `v`.
 * @param {Object} - `obj` the Data Structure.
 * @returns {object} - The modified Data Structure.
 *
 * @author Jean-Christophe Taveau
 */
const parseToken = (tok,obj) => {
  // Remove the leading underscore `_` and Split `category` and `attribute` 
  let [cat,attr] = tok.v.slice(1).split('.');
  console.log('cat,attr',cat,attr);
  if (!attr && obj._admin_.state === CIF.TABLE) {
    attr = cat;
    cat = 'table';
  }
  return (obj._admin_.state === CIF.TABLE) ? setHeader(cat,attr,obj) : setCategory(cat,attr,obj);
}

/**
 * Parse mmCIF Value in Token parseValue
 *
 * @param {Object} - `tok` a token composed of a type `type` and a value `v`.
 * @param {Object} - `obj` the Data Structure.
 * @returns {object} - The modified Data Structure.
 *
 * @author Jean-Christophe Taveau
 */
const setTokenValue = (tok,obj) => {
  let obj_block = obj._admin_.datablock;
//  console.log(obj._admin_.next,tok);
  if (!obj._admin_.attr) {
    obj_block[obj._admin_.current] = tok.v;
  }
  else {
    obj_block[obj._admin_.current][obj._admin_.attr] = tok.v;
  }

  obj._admin_.current = null;
  obj._admin_.attr = null;
  obj._admin_.next = [CIF.STRING,CIF.WORD,CIF.NUMBER, CIF.EOL,CIF.SEPARATOR];
  return obj;
}

/**
 * Parse Value
 *
 *
 * @param {Token} - `tok` a token composed of 
 * @param {Object} - `obj` the Data Structure
 * @returns {object} - The UNmodified Data Structure
 *
 * @author Jean-Christophe Taveau
 */
const parseValue = (tok,obj) => {
  return (obj._admin_.state === CIF.TABLE) ? setRowValue(tok,obj) : setTokenValue(tok,obj);
}


const setHeader = (cat,attr,obj) => {
  let obj_block = obj._admin_.datablock;
  console.log(`create Table ${cat}`);
  if (cat in obj_block === false) {
    // Create Table
    obj_block[cat] = {
      header: [],
      rows: [[]]
    };
  }
  obj_block[cat].header.push(attr);
  obj._admin_.current = cat; // Current Category to fill in
  obj._admin_.next = [CIF.TOKEN,CIF.NUMBER,CIF.STRING,CIF.WORD];
  return obj;
}

/**
 * Parse mmCIF Value in Token or in Table: setRowValue or parseCat depending of context (CIF.TABLE or CIF.TOKEN)
 *
 * @param {Object} - `tok` a token composed of a type `type` and a value `v`.
 * @param {Object} - `obj` the Data Structure.
 * @returns {object} - The modified Data Structure.
 *
 * @author Jean-Christophe Taveau
 */
const setRowValue = (tok,obj) => {
  let obj_block = obj._admin_.datablock;

  const table = obj_block[obj._admin_.current];
  let last = table.rows.length-1;
  if (table.rows[last].length >= table.header.length) {
    table.rows.push([]); // Add a new row in the table
    last++; // Update
  }
  table.rows[last].push(tok.v);
  obj._admin_.next = [CIF.STRING,CIF.WORD,CIF.NUMBER, CIF.EOL,CIF.SEPARATOR];
  return obj;
}

/**
 * Parse mmCIF Table
 *
 * @param {Object} - `tok` a token composed of a type `type` and a value `v`.
 * @param {Object} - `obj` the Data Structure.
 * @returns {object} - The modified Data Structure.
 *
 * @author Jean-Christophe Taveau
 */
const parseTable = (tok,obj) => {
  obj._admin_.state = CIF.TABLE;
  obj._admin_.next = [CIF.TOKEN];
  console.log(obj._admin_.state,'parseTable',tok);
  return obj;
}

/**
 * Parse mmCIF DataBlock
 *
 * @param {Object} - `tok` a token composed of a type `type` and a value `v`.
 * @param {Object} - `obj` the Data Structure.
 * @returns {object} - The modified Data Structure.
 *
 * @author Jean-Christophe Taveau
 */
const parseDataBlock = (tok,obj) => {
  console.log('new DB',tok.v);
  const id = (tok.v.length > 1) ? tok.v : 'default';
  obj._admin_.next = [CIF.TOKEN,CIF.TABLE]; // TOKEN, TABLE
  const db = {id};
  obj.datablocks[id] = db;
  obj._admin_.datablock = db;
  obj._admin_.current = null;
  obj._admin_.attr = null;

  console.log(obj);
  return obj;
}

/**
 * Parsers for the following tokens:
 *  - NONE: 0 ,
 *  - SEPARATOR: 1,
 *  - COMMENT: 2,
 *  - DATABLOCK: 3,
 *  - TOKEN: 4,
 *  - TABLE: 5,
 *  - HEADER: 6,
 *  - STRING: 7,
 *  - WORD: 8,
 *  - NUMBER: 9
 *  - EOL: 10
 */
export const parse_star = (toks) => {
  const  setters = [parseNothing,parseSeparator,parseComment,parseDataBlock,parseToken,parseTable,parseNothing,parseValue,parseValue,parseValue,parseEOL];

  const model = toks.reduce( (accu,tok) => {
    if (accu._admin_.next.includes(tok.type)) {
      return setters[tok.type](tok,accu);
    }
    return accu;
  },{_admin_: {next: [CIF.DATABLOCK],state: CIF.NONE}, datablocks: {}});

  return model;
}

/**
 * mmCIF Parser
 */
const parseSTAR = (txt) => {

  // First Pass
  const tokens = tokenize(txt);
  // Second Pass - Parse
  let structure = parser(tokens);
  delete structure._admin_;
  console.log(structure);
  console.info('End');
  return structure;
}


