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

function test(fn, x, expected) {
    if (fn(x) != expected) {
        console.log('Error, expected ' + expected + ' for x=' + x + ', got ' + fn(x));
    }
}

function runTests() {
    // 9 -> 0b1001, smaller is 0b0110 (5), larger is 0b1010 (10)
    // 7 -> 0b111, smaller is null, larger is 0b1110 (14)
    // 0 -> 0b0, smaller is null, larger is null
    // 37 -> 0b0100101, smaller is 0b0011100 (28), larger is 0b0100110 (38)
    // 2^15 -> smaller is 2^14, larger is 2^16
    // 2^31 -> smaller is 2^30, larger is overflow
    var vals = [
        [0b1001, 0b0110, 0b1010],
        [0b111, null, null],
        [0, null, null],
        [Math.pow(2, 15), Math.pow(2, 14), Math.pow(2, 16)],
        [Math.pow(2, 31), Math.pow(2, 30), null]
    ];
    for (var i = 0; i < vals.length; i++) {
        var x = vals[i][0];
        var smaller = vals[i][1];
        var larger = vals[i][2];
        test(findSmaller, x, smaller);
        test(findLarger, x, larger);
    }
}
