// SPDX-License-Identifier: MIT

//constructor란?: 스마트 컨트랙트를 배포할 때 한 번만 실행되는 특별한 함수이다.

pragma solidity ^0.8.0;

contract MyContract {
    uint256 public myValue;

    // 생성자
    constructor(uint256 _initialValue){
        myValue = _initialValue; // 초기값 설정
    }
}