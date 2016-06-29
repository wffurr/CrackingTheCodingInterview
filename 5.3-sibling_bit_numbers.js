function findSmaller(x) {
    var result = x;
    var mask = 1 << Math.floor(Math.log2(x));;
    result &= ~mask;
    while (mask > 0) {
        mask = mask >> 1;
        if ((result | mask) !== result) {
            return result | mask;
        }
    }
    return null;
}

function findLarger(x) {
    var result = x;
    var flipped = false;
    var mask = 1;
    while (mask > 0) {
        if (flipped) {
            if ((result | mask) !== result) {
                return result | mask;
            }
        } else {
            if ((result & ~mask) !== result) {
                result &= ~mask;
                flipped = true;
            }
        }
        mask = mask << 1;
    }
    return null;
}

function runTests() {
    // 9 -> 0x1001, smaller is 0x0101 (5), larger is 0x1010 (10)
    // 7 -> 0x111, smaller is null, larger is 0x1110 (14)
    // 0 -> 0x0, smaller is null, larger is null
    // 2^15 -> smaller is 2^14, larger is 2^16
    // 2^31 -> smaller is 2^30, larger is overflow
    var vals = [9, 7, 0, Math.pow(2, 15), Math.pow(2, 31)]
    for (var i = 0; i < vals.length; i++) {
        console.log(findSmaller(vals[i]));
        console.log(findLarger(vals[i]));
    }
}