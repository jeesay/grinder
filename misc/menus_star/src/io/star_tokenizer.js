import {CIF} from "./star_common.js";

/////////////////////::: T O K E N I Z E R ::://///////////////////

/**
 * mmCIF Tokenizer
 */
export const tokenize = (txt) => {

  // Predicates
  const isDataBlock = (w) => (w.slice(0,5) === 'data_');
  const isTable = (w) => (w === 'loop_');
  const isFirst = (symbol) => w => (w[0] === symbol);
  const isComment = isFirst('#');
  const isToken = isFirst('_');
  const isMultiLine = isFirst(';');
  const isString = isFirst('\'');
  const isStringDoubleQuote = isFirst('\"');
  const isNumber = (w) => (!isNaN(Number(w)));
  const isEOL = (w) => (w.match(/\n/g) || []).length >= 2;
  const isSeparator = (w) => w.split('').every( ch => [' ','\t'].includes(ch)) || w.split('').filter(ch => ch === '\n').length === 1;
  const isWord = (w) => true;
  
  // Create Basic Token
  const basicToken = (type) => (w,i,array) => [{type: type,v:w},i];
  
  // Create Numeric Token
  const numericToken = (type) => (w,i,array) => [{type: type,v:parseFloat(w)},i];
  
  // Create StringToken using Recursion
  const appendWord = (predicate,array,j,str='') => {
    let word = array[j];
    str += word;
    if (predicate(word) === false) {
      return [j,str];
    }
    return appendWord(predicate,array,j+1,str);
  }

  const stringToken = (type,predicate) => (w,i,array) => {
    let [j,str] = appendWord(predicate,array,i);
    // Remove leading delimiters
    const v = str.slice(1,str.length-1);
    return [{type,v},j];
  }

  const keywords = [
    {
      predicate: isDataBlock,
      newToken: (w,i,array) => [{type: CIF.DATABLOCK,v:w.slice(5)},i],
    },
    {
      predicate: isTable,
      newToken: basicToken(CIF.TABLE)
    },
    {
      predicate: isComment,
      newToken: stringToken(CIF.COMMENT,word => {
        if (!word) {
          return false;
        }
        else {
          return word[0] !== '\n';
        }
      })
    },
    {
      predicate: isSeparator,
      newToken: basicToken(CIF.SEPARATOR) 
    },
    {
      predicate: isEOL,
      newToken: basicToken(CIF.EOL) 
    },
    {
      predicate: isToken,
      newToken: basicToken(CIF.TOKEN)
    },
    {
      predicate: isMultiLine,
      newToken: stringToken(CIF.STRING, word => (word[0] !== ';') )
    },
    {
      predicate: isNumber,
      newToken: numericToken(CIF.NUMBER)
    },
    {
      predicate: isString,
      newToken: stringToken(CIF.STRING, word => word[word.length-1] !== '\'')
    },
    {
      predicate: isStringDoubleQuote,
      newToken: stringToken(CIF.STRING, word => word[word.length-1] !== '\"')
    },
    {
      predicate: isWord,
      newToken: basicToken(CIF.WORD) 
    }
  ];

  const setToken = (words) => (index) => {
    let w = words[index];
    // Get Token corresponding to keyword
    const toks = keywords.reduce( (accu,kw) => {
      // const newTok = iif(kw,w,index,words).newToken();
//      console.info(w);
      // HACK: EOL is replaced by SEPARATOR because tested before
      if (kw.predicate(w)) {
        accu.push(kw.newToken(w,index,words));
      }
      return accu;
    },[]);
    
    // Add new Token. Only the first one because the last one is always `CIF.WORD`
    return toks[0]; // keyword.newToken(w,index,words);
  };
  
  ///// M A I N /////
  const words = txt
    .replace(/#.*\n/g,'\n') // Replace comments by NewLine
    .split(/(\s+)/);        // Split lines

//  console.log(words[words.length - 1]);
  
  let tokens = [];
  let index = 0;
  let tok = null;
  const setTokenAt = setToken(words);

  // TODO Use (tail) recursion
  while (index < words.length) {
    [tok,index] = setTokenAt(index);
    tokens.push(tok);
    index++;
  }
  console.info(tokens);
  return tokens;
} // End of function tokenize

