//
//  main.cpp
//  GameOfThrees
//
//  Created by Alan Pham on 12/5/15.
//  Copyright © 2015 Alan Pham. All rights reserved.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    int num;
    std::cout << "Input a number: ";
    std::cin >> num;
    
    while (num != 1){
        if (num % 3 == 0){
            std::cout << num << " 0" << std::endl;
        }
        else if ((num) % 3  == 1){
            std::cout << num << " -1" << std::endl;
            num -= 1;
        }
        else if ((num) % 3 == 2) {
            std::cout << num << " 1" << std::endl;
            num += 1;
        }
        num /= 3;
    }
    std::cout << num << std::endl;
    return 0;
}
