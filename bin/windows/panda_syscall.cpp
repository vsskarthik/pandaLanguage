#include<bits/stdc++.h>

using namespace std;

int main(int argc,char** argv){

  if (argc == 2){

    //string cmd = "python ../../src/converter/read_write.py";
    string cmd = "python ../../src/converter/read_write.py ";
    cmd += argv[1];

    const char *command = cmd.c_str();
    system(command);
  }
  else{

    cout << "[ERROR] Invalid number of arguments provided.";

  }

  return 0;

}
