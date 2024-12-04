// SPDX-License-Identifier: MIT

//수업 시간에 한 것
pragma solidity ^0.8.27; // Solidity 버전을 지정한다.

contract Identity
{
    string name;
    uint age;

    constructor(){
        name = "MSE";
        age = 24;
    }

    function getname() view public returns(string memory)
    {
        return name;
    }

    function getage() view public returns(uint)
    {
        return age;
    }
}