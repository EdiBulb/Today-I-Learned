// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Wallet{
    //주소(address) => 잔액(uint256)을 저장하는 mapping
    mapping(address => uint256) public balances;

    //이더 입금 함수
    function deposit() public payable { // payable: 함수가 이더(ether)를 받을 수 있도록 허용함
        balances[msg.sender] += msg.value; // 입금된 이더를 저장한다.
    }

    //잔액 조회 함수 (자동 새성됨, public 키워드 덕분)
    // function balances(address account) public view returns (uint256){}

    //출금함수
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        payable(msg.sender).transfer(amount);
    }
}