/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function (a, b) {
    let result = '';
    let carry = 0;
    let indexA = a.length - 1;
    let indexB = b.length - 1;
    while (indexA >= 0 || indexB >= 0 || carry > 0) {
        let sum = carry;
        if (indexA >= 0) {
            sum += a[indexA] - '0';
            indexA -= 1;
        }
        if (indexB >= 0) {
            sum += b[indexB] - '0';
            indexB -= 1;
        }
        result = (sum & 1) + result;
        carry = sum >> 1;
    }
    return result;
};
