use std::collections::HashMap;

pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut values = HashMap::new();

        for (i, &val) in nums.iter().enumerate() {
            if let Some(&index) = values.get(&(target - val)) {
                return vec![index, i as i32];
            }
            values.insert(val, i as i32);
        }

        vec![]
    }
}

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;
    let result = Solution::two_sum(nums, target);
    println!("[{}, {}]", result[0], result[1]);
}
