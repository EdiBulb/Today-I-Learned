// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27; // Solidity 버전을 지정한다.

contract Lock {
    //상태변수 : 블록체인에 저장되는 값
    uint256 public unlockTime; // 잠금 해제 시간 (Unix 타임스탬프)

    //생성자 : 스마트 컨트랙트를 배포할 때 실행
    constructor(uint256 _unlockTime) {
        unlockTime = _unlockTime;
    }
}
