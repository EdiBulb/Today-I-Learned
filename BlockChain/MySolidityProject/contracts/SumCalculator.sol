// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SumCalculator {
    //상태 변수: 저장된 합계
    uint256 public sum;

    // 반복문으로 숫자 합산
    function calculateSum(uint256 n) public {
        uint256 total = 0;
        for (uint256 i = 1; i<=n; i++){
            total +=i; // 1부터 n까지의 숫자를 더한다.
        }
        sum = total;
    }

}