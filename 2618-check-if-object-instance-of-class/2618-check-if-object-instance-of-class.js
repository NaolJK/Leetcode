/**
 * @param {any} obj
 * @param {any} classFunction
 * @return {boolean}
 */
var checkIfInstanceOf = function(obj, classFunction) {
    if(obj === null || obj === undefined || typeof classFunction !== 'function'){
        return false;
    }
    
    let p = Object.getPrototypeOf(obj);
    
    while(p){
        if(p === classFunction.prototype){
            return true;
        }
        
        p = Object.getPrototypeOf(p)
    }
    
    return false;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */