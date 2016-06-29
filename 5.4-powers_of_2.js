// This should print nothing when complete.
function verifyPowersOf2Test() {
  for (var i = 0; i < 4096; i++) {
    var test1 = ((i & (i-1)) == 0);
	var test2 = (Math.pow(2, Math.floor(Math.log2(i))) == i);
	if (test1 !== test2) {
      console.log('' + i + '\t' + test1 + '\t' + test2);
    }
  }
}