//SPDX-License-Identifier: MIT

pragma solidity ^0.8.27; // 이 코드는 Solidity 컴파일러 ㅓ전 0.8.0 이상에서 동작한다.

//이름이 Voting인 스마트 계약을 정의함 - 모든 로직과 데이터는 이 안에 포함된다.
contract Voting{
    //상태변수
    //uint256 데이터타입 : unsigned integer of 256 bits : 256비트 크기의 부호 없는 정수 
    uint256 public yesVotes; // 찬성 투표 수 저장
    uint256 public noVotes; // 반대 투표 수 저장

    // 투표 기록
    //mapping : solidity의 자료구조로, 특정 키에 대한 값을 저장한다. - mapping으로 사용자가 중복 투표 못하게 함
    mapping(address => bool) public hasVoted; // hasVoted : 사용자가 투표를 했는지 여부를 저장함 - 

    // 찬성 투표 함수
    function voteYes() public {
        //require : 조건문 
        require(!hasVoted[msg.sender], "You have already voted");
        yesVotes++;
        hasVoted[msg.sender] = true;
    }

    function voteNo() public {
        require(!hasVoted[msg.sender], "You have already voted");
        noVotes++;
        hasVoted[msg.sender] = true;
    }
    // 현재 투표 현황 조회
    function getVotes() public view returns (uint256, uint256){
        return (yesVotes, noVotes);
    }
}