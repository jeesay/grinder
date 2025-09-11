import {CIF} from "./io/star_common.js";
import {tokenize} from './io/star_tokenizer.js'
import {parse_star} from './io/star_parser.js'

class Block {
  constructor(b) {
    this.block = b;
  }
  
  get id() {
    return this.block.id;
  }
  
  raw_table(name) {
    const tablename = (name == null) ? 'table' : name;
    return this.block[tablename];
  }
  
  table(name) {
    const tab = this.raw_table(name);
    if (tab) {
      return tab.rows.map( (row) => {
        let obj = {};
        for (let h in tab.header) {
          obj[tab.header[h]] = row[h];
        }
        return obj;
      });
    }
    return null;
  }
}

export class StarGate {
    constructor() {
        this.db = {};
    }

    blocks() {
        return this.db
    }
    
    fetch_mmcif(pdbid) {
        // TODO
        pass
    }
    
    datablock(blockname) {
      const _block = this.db.datablocks[blockname]
      if (_block) {
        console.info(_block);
        return new Block(_block);
      }
      return null;
    }
    
    table_of(blockname) {
      for (db of this.db['datablocks']) {
        if (db['id'] == blockname && db['table']) {
          return db;
        }
      }
      return null;
    }

    parseSTAR(txt) {
      //// First Pass
      const tokens = tokenize(txt);
      //// Second Pass - Parse
      this.db = parse_star(tokens);
      delete this.db._admin_;
      console.info(this.db);
    }
}



    
