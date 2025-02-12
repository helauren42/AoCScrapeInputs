#include <iostream>
#include <fstream>
#include "../../Printer/Printer.hpp"

using namespace std;

string readFile(const string filename="input.txt") {
    ifstream inputFile(filename);
    if (!inputFile) {
        Out::stdErr("File could not open: ", filename);
        exit(1);
    }
    string line;
    string content;
    while(std::getline(inputFile, line)) {
        content += line;
    };
    inputFile.close();
    return content;
}

int main() {
    
}
