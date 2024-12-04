// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ArraySum {
    uint256[] public numbers; // 숫자 배열

    // 배열에 숫자 추가
    function addNumber(uint256 num) public {
        numbers.push(num);
    }

    // 배열의 합계 계산
    function calculateSum() public view returns (uint256){
        uint256 total = 0;
        for (uint256 i =0;i<numbers.length;i++){
            total +=numbers[i];
        }
        return total;
    }
}