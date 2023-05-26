/**
 * @param {number[]} nums
 * @return {number}
 */
var minimizeArrayValue = function(nums) {
    let maximum = 0;
    let sum = 0;

    for(let i=0; i < nums.length; i++){
        sum+=nums[i];
        let a = Math.ceil(sum / (i + 1));
        maximum = Math.max(a, maximum);
    }

    return maximum
};