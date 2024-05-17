using System;
using System.Collections.Generic;

public class Solution
{
    public int[] TwoSum(int[] nums, int target)
    {
        Dictionary<int, int> values = new Dictionary<int, int>();

        for (int i = 0; i < nums.Length; i++)
        {
            if (values.ContainsKey(target - nums[i]))
            {
                return new int[] { values[target - nums[i]], i };
            }
            else
            {
                values[nums[i]] = i;
            }
        }
        return null;
    }

    // Main method for testing
    public static void Main(string[] args)
    {
        Solution solution = new Solution();
        int[] nums = { 2, 7, 11, 15 };
        int target = 9;
        int[] result = solution.TwoSum(nums, target);
        Console.WriteLine($"[{result[0]}, {result[1]}]");
    }
}
